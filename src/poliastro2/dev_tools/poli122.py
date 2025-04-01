"""
Converts the user codebase from the old poliastro to poliastro2 import patterns.

NOTE: Order matters; Complete and Exact match matters
"""

import libcst as cst
import os
import re
import json

def get_mapping_from_json(path, old_parent="poliastro", new_parent="poliastro2") -> dict:
    """
    Load the JSON directory mapping file, replace keys containing 'poliastro' with 'old_parent',
    and replace values containing 'poliastro2' with 'new_parent'.

    Parameters
    ----------
    path : str
        Path to the JSON file.
    old_parent : str
        The string to replace 'poliastro' in keys.
    new_parent : str
        The string to replace 'poliastro2' in values.

    Returns
    -------
    dict
        Transformed dictionary.
    """
    with open(path, "r") as file:
        data = json.load(file)

    mapping = {}
    for key, value in data.items():
        new_key = key.replace("poliastro", old_parent)
        if isinstance(value, str):
            new_value = value.replace("poliastro2", new_parent)
        else:
            new_value = value
        mapping[new_key] = new_value

    return mapping

def get_subdir_exact_mapping(old_parent = "poliastro", new_parent = "poliastro2") -> dict:
    """
    Mapping of the old "from A import B as C" statements to new ones by finding the exact match.

    Parameters
    ----------
        old_parent (str): The old parent directory name. optional, default is "poliastro"
        new_parent (str): The new parent directory name. optional, default is "poliastro2"

    Returns
    -------
        exact_mapping (dict): A dictionary where keys are old subdirectory names
        and values are new subdirectory names.
    
    Note
    ----
    Ordering in this dictionary matters.
    The first match will be used for replacement.
    """
    exact_mapping = {
        (f"{old_parent}.twobody.orbit", "Orbit"): 
            f"from {new_parent}.core.orbit import Orbit",
        (f"{old_parent}.twobody", "Orbit"): 
            f"from {new_parent}.core.orbit import Orbit",
        (f"{old_parent}.core.twobody", "Orbit"):
            f"from {new_parent}.core.orbit import Orbit",
        (f"{old_parent}.core", "iod"): 
            f"from {new_parent}.math.iod import base_iod as iod",
        (f"{old_parent}.math.threebody.cr3bp_char_quant", "SystemChars"): 
            f"from {old_parent}.core.threebody.cr3bp_char_quant import SystemChars",
    }
    return exact_mapping

def find_python_files(directory):
    """Recursively find all Python files in a directory."""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                python_files.append(file_path)
    
    # Remove the current file from the list if it exists
    current_file = os.path.abspath(__file__)
    if current_file in python_files:
        python_files.remove(current_file)
    
    return python_files

class ImportTransformer(cst.CSTTransformer):
    def __init__(self, mapping: dict):
        self.mapping = mapping
        self.modified = False

    def leave_Import(self, original_node: cst.Import, updated_node: cst.Import) -> cst.Import:
        new_names = []
        for alias in updated_node.names:
            module_name = alias.name.value
            if module_name in self.mapping:
                print(f"Replacing import: {module_name} -> {self.mapping[module_name]}")
                self.modified = True
                new_alias = alias.with_changes(name=cst.parse_expression(self.mapping[module_name]))
                new_names.append(new_alias)
            else:
                new_names.append(alias)
        return updated_node.with_changes(names=new_names)

    def leave_ImportFrom(self, original_node: cst.ImportFrom, 
                         updated_node: cst.ImportFrom) -> cst.ImportFrom:
        if updated_node.module is not None and isinstance(updated_node.module, cst.Name):
            module_name = updated_node.module.value
            if module_name in self.mapping:
                print(f"Replacing from-import: {module_name} -> {self.mapping[module_name]}")
                self.modified = True
                new_module = cst.parse_expression(self.mapping[module_name])
                return updated_node.with_changes(module=new_module)
        return updated_node

    def leave_Attribute(self, original_node: cst.Attribute, 
                        updated_node: cst.Attribute) -> cst.BaseExpression:
        # Helper to reconstruct the dotted name from an attribute chain.
        def get_dotted_name(node):
            parts = []
            while isinstance(node, cst.Attribute):
                parts.append(node.attr.value)
                node = node.value
            if isinstance(node, cst.Name):
                parts.append(node.value)
            return ".".join(reversed(parts))
        
        dotted_name = get_dotted_name(original_node)
        # Check if the dotted name starts with any of the keys in the mapping.
        for old_key, new_key in self.mapping.items():
            if dotted_name == old_key or dotted_name.startswith(old_key + "."):
                suffix = dotted_name[len(old_key):]
                new_dotted_name = new_key + suffix
                print(f"Replacing attribute chain: {dotted_name} -> {new_dotted_name}")
                self.modified = True
                return cst.parse_expression(new_dotted_name)
        return updated_node

def transform_code(source: str, dir_mapping: dict, exact_mapping: dict = None) -> str:
    module = cst.parse_module(source)
    transformer_general = ImportTransformer(dir_mapping)
    
    for i in range(5):
        modified_module = module.visit(transformer_general)
        if not transformer_general.modified: break
    return modified_module.code

def replace_exact_imports(source: str, exact_mapping: dict) -> str:
    """
    Process the source code line-by-line and replace lines that exactly match
    the pattern "from <module> import <name>" with the corresponding new statement.
    NOTE: There are better ways to do this using AST, but this is a quick solution.
    """
    # This regex matches lines that:
    # - start with "from" (possibly with leading spaces)
    # - followed by one or more whitespace characters
    # - then a module name (alphanumeric, underscores, or dots)
    # - followed by whitespace, the literal "import", whitespace,
    # - then an imported name (alphanumeric or underscore)
    # - and nothing else (except possible trailing spaces)
    pattern = re.compile(r"^(from)\s+([A-Za-z0-9_.]+)\s+(import)\s+([A-Za-z0-9_]+)\s*$")
    # TODO: to include tests
    # @mock.patch("{new_parent}.ephem.Horizons"': f'@mock.patch("{new_parent}.core.ephem.Horizons"',
    # in test_ephem.py
    new_lines = []
    for line in source.splitlines(keepends=True):
        # Try to match the pattern on the stripped line.
        match = pattern.match(line.strip())
        if match:
            module_name = match.group(2)
            imported_name = match.group(4)
            key = (module_name, imported_name)
            if key in exact_mapping:
                new_line = exact_mapping[key] + "\n"
                print(f"Replacing exact import: '{line.strip()}' -> '{new_line.strip()}'")
                new_lines.append(new_line)
                continue
        new_lines.append(line)
    return "".join(new_lines)

def convert_122(target_dir: str, json_path = "122mapping.json", old_parent="poliastro", new_parent="poliastro2"):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Path to the JSON file
    json_path = os.path.join(current_dir, json_path)
    # Load the JSON file and get the mapping of old subdirectory names to new ones
    dir_mapping = get_mapping_from_json(json_path, old_parent, new_parent)

    # exact matches from A to B form
    exact_mapping = get_subdir_exact_mapping(old_parent="poliastro", new_parent="poliastro2")

    # Get all Python files in the target directory and its subdirectories
    python_files = find_python_files(target_dir)

    # Update each Python file with the new import statements
    for filepath in python_files:
        with open(filepath, "r") as file:
            content = file.read()

        # exact matches have to be checked and replaced before general mappings
        # as there is a final catch term in the general mapping that is going to 
        # convert all old_parent to new_parent

        # check exact matches
        new_content = replace_exact_imports(content, exact_mapping)

        # module name level transformations
        new_content = transform_code(new_content, dir_mapping)
        
        # Write the modified content back to the file
        with open(filepath, "w") as file:
            file.write(new_content)
        print(f"Updated imports in {filepath}")
    
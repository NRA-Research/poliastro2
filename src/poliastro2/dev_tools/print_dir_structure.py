import os

def list_files(startpath, output_file):
    with open(output_file, "w") as file:
        for root, dirs, files in os.walk(startpath):
            # Skip __pycache__ directories
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            level = root.replace(startpath, "").count(os.sep)
            indent = " " * 4 * level
            file.write(f"{indent}{os.path.basename(root)}/\n")
            subindent = " " * 4 * (level + 1)
            for f in files:
                file.write(f"{subindent}{f}\n")

if __name__ == "__main__":
    # Generate structure starting from the current directory
    parent_dir = os.getcwd()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_filename = "directory_structure.txt"

    list_files(f'{parent_dir}', f'{current_dir}/{output_filename}')
    print(f"Directory structure saved to {output_filename}")

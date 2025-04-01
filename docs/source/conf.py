import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

# -- Project information -----------------------------------------------------
project = 'poliastro2'
copyright = '2025 (Poliastro2) Xiyuan Li; ' \
    '2013-2023, (Poliastro) Juan Luis Cano Rodríguez and the poliastro development team'
author = 'Xiyuan Li (Poliastro2); '\
    '(Poliastro) Juan Luis Cano Rodríguez and the poliastro development team'

version = '0.2.dev0'

# GitHub role config
github_default_org_project = ("nra-research", "poliastro2")
extensions = [
   'sphinx.ext.duration',
   'sphinx.ext.doctest',
   'sphinx.ext.autodoc',
   'sphinx.ext.autosummary',
   'sphinx.ext.napoleon'
]
# Autodoc
autodoc_default_options = {
    # Autodoc members
    "members": True,
    # Autodoc undocumented memebers
    "undoc-members": False, 
    # Autodoc private memebers
    "private-members": True
    }

autosummary_generate = True
autosummary_generate_overwrite = True  # Optional, regenerates the files on each build
autosummary_imported_members = False
autodoc_typehints = 'description'
html_theme = "nature"


html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
mathjax2_config = {
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "processEscapes": True,
        "ignoreClass": "document",
        "processClass": "math|output_area",
    }
}
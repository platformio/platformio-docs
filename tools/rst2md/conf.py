# Sphinx configuration used only by the RST -> Markdown converter.

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

project = "PlatformIO"
master_doc = "index"
source_suffix = ".rst"
extensions = ["markdown_builder"]
exclude_patterns = [
    "_build",
    "build",
    "docs",
    "node_modules",
    "tools",
    ".docusaurus",
]
suppress_warnings = ["toc.not_included"]
smartquotes = False

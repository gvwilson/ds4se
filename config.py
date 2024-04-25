"""Ark configuration file."""
title = "Data Science for Software Engineers"
slug = "ds4se"
repo = f"https://github.com/gvwilson/{slug}"
site = f"https://gvwilson.github.io/{slug}/"
author = {
    "name": "Greg Wilson",
    "email": "gvwilson@third-bit.com",
    "site": "https://third-bit.com/",
}
lang = "en"
highlight = "tango.css"
# plausible = f"gvwilson.github.io/{slug}"

chapters = [
    "intro",
    "tools",
    "finale",
]

appendices = [
    "license",
    "conduct",
    "contrib",
    "bib",
    "glossary",
    "author",
    "colophon",
    "contents",
]

# Files to copy
copy = [
    "*.out",
    "*.png",
    "*.py",
    "*.sh",
    "*.svg",
]

# Files and directories to skip
exclude = {}

# Theme information.
theme = "mccole"
src_dir = "src"
out_dir = "docs"
extension = "/"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}

# Show theme.
if __name__ == "__main__":
    print(theme)

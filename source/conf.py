# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Lochana's Letters"
copyright = '2025, Lochana Perera'
author = 'Lochana Perera'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'sphinx_design'
]
myst_enable_extensions = [
    "html_image",
    "html_admonition",
    "colon_fence"
]

myst_allow_html = True


templates_path = []
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = "Lochana's Letters"
html_theme_options = {
    "sidebar_hide_name": True,
    "top_of_page_button": "edit",
}
html_static_path = ['_static']

# Add at end of file
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'django-currency-updater'
copyright = '2024, medaminerjb'
author = 'medaminerjb'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', ]

templates_path = ['_templates']
exclude_patterns = []

root_doc = 'index'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',  # Add this line for Markdown support
}
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Set the base URL for your site
html_baseurl = "https://medaminerjb.github.io/django-currency-update/build/html"

# Ensure the static path is included correctly
html_static_path = ['_static']

import sphinx_theme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Introduction to Quantum Chemistry'
copyright = '2023, Shane M. Parker'
author = 'Shane M. Parker'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinxcontrib.bibtex', 'sphinxcontrib.youtube', 'sphinx.ext.mathjax', 'sphinx_subfigure' ]

mathjax3_config = {
  "loader": { "load": ['[tex]/mhchem']},
  "tex": { "packages": {'[+]': ['mhchem']}}
}

templates_path = ['_templates']
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

# -- Other configuration ---------------------------------------------------
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'plain'
bibtex_reference_style = 'super'

# -- MyST configuration ---------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html

#myst_enable_extensions = [ "deflist", "html_image", "replacements", "smartquotes", "substitution", "tasklist", "colon_fence" ]
myst_enable_extensions = [ "dollarmath", "amsmath", "deflist", "html_image", "replacements", "smartquotes", "substitution", "tasklist", "colon_fence" ]
myst_dmath_double_inline = True
myst_update_mathjax = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'stanford_theme'
html_theme_path = [sphinx_theme.get_html_theme_path()]
html_static_path = ['_static']

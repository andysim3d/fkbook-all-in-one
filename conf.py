# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
fk_repo_path = os.path.abspath('.')


# -- Project information -----------------------------------------------------

project = '新月杀'
copyright = '2024, Qsgs-Fans'
author = 'Qsgs-Fans'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.doctest',
  'sphinx.ext.intersphinx',
  'sphinx.ext.todo',
  'sphinx.ext.coverage',
  'sphinx.ext.mathjax',
  'sphinx.ext.ifconfig',
  'sphinx.ext.githubpages',
  'sphinx.ext.imgconverter',
  'sphinxcontrib.luadomain',
  'sphinxcontrib.plantuml',
  'sphinx_lua',

]

lua_source_path = [
  fk_repo_path + "/freekill-core/lua",
  fk_repo_path + "/freekill-core/standard",
  fk_repo_path + "/freekill-core/standard_cards",
  fk_repo_path + "/freekill-core/maneuvering",
  #fk_repo_path + "/FreeKill/packages",
]

lua_source_encoding = 'utf8'
lua_source_comment_prefix = '---'
lua_source_use_emmy_lua_syntax = True
lua_source_private_prefix = '_'
plantuml_output_format = 'svg_img'
plantuml_latex_output_format = 'png'
plantuml_syntax_error_image = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
  '.venv/*',
  'FreeKill/*',
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_favicon = 'favicon.ico'
html_logo = 'favicon.ico'

# PDF option
latex_engine = 'xelatex'
latex_elements = {
  'papersize': 'a4paper',
  'pointsize': '12pt',
  'fontpkg': r'''
''',
  'fncychap': r'\usepackage[Sonny]{fncychap}',
  'preamble': r'''
''',
  'figure_align': 'H',
  'classoptions':',oneside',
}

latex_documents = [
  ('index', 'book.tex', '新月之书',
   'Qsgs-Fans', 'book', False),
]


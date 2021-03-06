# -*- coding: utf-8 -*-

# -- General configuration -----------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'Blanc Basic News'
copyright = u'2012-2015, Blanc Ltd'

# The short X.Y version.
version = '0.3'
# The full version, including alpha/beta/rc tags.
release = '0.3'

exclude_patterns = ['_build']
pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'blanc-basic-newsdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_documents = [
    ('index', 'blanc-basic-news.tex', 'Blanc Basic News Documentation',
     'Blanc Ltd', 'manual'),
]

# -- Options for manual page output --------------------------------------------

man_pages = [
    ('index', 'blanc-basic-news', 'Blanc Basic News Documentation',
     ['Blanc Ltd'], 1)
]

# -- Options for Texinfo output ------------------------------------------------

texinfo_documents = [
    ('index', 'blanc-basic-news', 'Blanc Basic News Documentation',
     'Blanc Ltd', 'blanc-basic-news', 'One line description of project.',
     'Miscellaneous'),
]


# -- intersphinx ---------------------------------------------------------------

intersphinx_mapping = {
    'django': ('https://docs.djangoproject.com/en/1.7/',
               'https://docs.djangoproject.com/en/1.7/_objects/'),
}
intersphinx_cache_limit = 90  # days

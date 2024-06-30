import os
import sys
import django

# Add your project root and settings to the path
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../LabProject'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'LabProject.settings'
django.setup()

# Add extensions for autodoc
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]


# The master toctree document.
master_doc = 'index'

# Add arc42 documentation path
sys.path.insert(0, os.path.abspath('../source/arc42'))

# General configuration
project = 'Django Shop'
author = 'Your Name'
release = '0.1'
html_theme = 'alabaster'
html_static_path = ['_static']

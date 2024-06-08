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
    'sphinx.ext.napoleon',  # If you use Google or NumPy style docstrings
]

# The master toctree document.
master_doc = 'index'

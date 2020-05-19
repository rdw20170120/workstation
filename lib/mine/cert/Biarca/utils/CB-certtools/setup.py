#!/usr/bin/env python

from setuptools import setup, find_packages

import os
import glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

config = {
    'name': 'certtools',
    'description': 'API for managing and running couchbase exam items.',
    'author': 'biarca',
    'maintainer': 'biarca',
    'author_email': 'support@biarca.com',
    'url': 'https:',
    'version': '0.1',
    'tests_requires': ['nose'],
    'zip_safe': False,
    'include_package_data': True,
    'packages': find_packages(),
    'scripts': [],
}

setup(**config)


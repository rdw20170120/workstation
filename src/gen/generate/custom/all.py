#!/usr/bin/env false
"""Generate all source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)
from .document.all import generate as generate_all_document
from .script.all import generate as generate_all_script


def generate(directory):
    generate_all_document(directory)
    generate_all_script(directory)


"""DisabledContent
"""

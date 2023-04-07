#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)
from .document.all import generate as generate_document
from .script.all import generate as generate_script


def generate(config, directory):
    generate_document(config, directory)
    generate_script(config, directory)


"""DisabledContent
"""

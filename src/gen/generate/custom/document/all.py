#!/usr/bin/env false
"""Generate all custom source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)
from .markdown.all import generate as generate_all_markdown


def generate(directory):
    generate_all_markdown(directory)


"""DisabledContent
"""

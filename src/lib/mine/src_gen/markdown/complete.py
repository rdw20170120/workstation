#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.markdown.source import generate
from src_gen.markdown.structure import *

# Project modules   (relative references, NOT packaged, in project)


def _document():
    return [
        h1("TODO"),
    ]


def generate_document(directory, filename):
    generate(_document(), directory, filename)


"""DisabledContent
"""

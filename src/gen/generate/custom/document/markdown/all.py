#!/usr/bin/env false
"""Generate all Markdown documents."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.document.markdown.complete import generate_document as document

# Project modules   (relative references, NOT packaged, in project)


def _generate_doc(dir_):
    sub = dir_


def generate(directory):
    _generate_doc(directory / "doc")


"""DisabledContent
"""

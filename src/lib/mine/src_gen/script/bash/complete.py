#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.source import generate
from src_gen.script.bash.structure import *

# Project modules   (relative references, NOT packaged, in project)


def _sourced():
    return [
        header_sourced(),
        todo("DESCRIPTION"),
        line(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def generate_sourced(directory, filename):
    generate(_sourced(), directory, filename)


"""DisabledContent
"""

#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.bash.source import generate
from src_gen.bash.structure import *

# Project modules   (relative references, NOT packaged, in project)


def _activation():
    return [
        header_activation(),
        todo("DESCRIPTION"),
        disable_tracing_unless_maximal(),
        line(),
        todo("CONTENT"),
        line(),
        enable_tracing_unless_minimal(),
        disabled_content_footer(),
    ]


def _sourced():
    return [
        header_sourced(),
        todo("DESCRIPTION"),
        line(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def generate_activation(directory, filename):
    generate(_activation(), directory, filename)


def generate_sourced(directory, filename):
    generate(_sourced(), directory, filename)


"""DisabledContent
"""

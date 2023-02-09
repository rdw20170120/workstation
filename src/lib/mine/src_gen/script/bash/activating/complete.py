#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.activating.structure import *

# Project modules   (relative references, NOT packaged, in project)


def sourced():
    return [
        header_sourced(),
        todo("DESCRIPTION"),
        line(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


"""DisabledContent
def activation():
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


"""

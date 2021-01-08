#!/usr/bin/env false
"""Generate all Bash scripts."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)
from .briteonyx.all import generate as generate_all_briteonyx


def generate(directory):
    # NOTE: There should NOT exist any custom Bash scripts
    # Any Bash scripts should be shared,
    # or they should be BriteOnyx scripts instead.
    generate_all_briteonyx(directory)


"""DisabledContent
"""

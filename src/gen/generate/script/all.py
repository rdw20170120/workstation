#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)
from .bash.all import generate as generate_bash
from .python.all import generate as generate_python


def generate(config, directory):
    generate_bash(config, directory)
    generate_python(config, directory)


"""DisabledContent
"""

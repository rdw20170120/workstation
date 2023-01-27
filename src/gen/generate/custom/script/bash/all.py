#!/usr/bin/env false
"""Generate all custom Bash scripts."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.complete import generate_activation as activation

# Project modules   (relative references, NOT packaged, in project)
from .briteonyx.all import generate as generate_all_briteonyx


def _generate_bin(dir_):
    sub = dir_
    _generate_bin_lib(sub / "lib")


def _generate_bin_lib(dir_):
    sub = dir_
    activation(sub, "configure-Anaconda.bash")
    activation(sub, "declare.bash")


def generate(directory):
    # NOTE: Typically,
    # there should NOT exist
    # any custom Bash scripts.
    # Any Bash scripts
    # should be shared,
    # or they should be
    # BriteOnyx scripts
    # instead.
    generate_all_briteonyx(directory)
    _generate_bin(directory / "bin")


"""DisabledContent
"""

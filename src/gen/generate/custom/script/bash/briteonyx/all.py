#!/usr/bin/env false
"""Generate all BriteOnyx Bash scripts."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.briteonyx.complete import (
    generate_executed as executed,
)
from src_gen.script.bash.briteonyx.complete import generate_sourced as sourced

# Project modules   (relative references, NOT packaged, in project)


def _generate_bin(dir_):
    sub = dir_
    _generate_bin_lib(sub / "lib")


def _generate_bin_lib(dir_):
    sub = dir_
    sourced(sub, "declare.bash")


def generate(directory):
    _generate_bin(directory / "bin")


"""DisabledContent
"""

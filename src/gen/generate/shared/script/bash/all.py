#!/usr/bin/env false
"""Generate all BASH scripts."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.complete import generate_sourced as sourced

# Project modules   (relative references, NOT packaged, in project)
from .activate import generate as generate_activate
from .briteonyx.all import generate as generate_all_briteonyx
from .set_path import generate as generate_set_path


def _generate_briteonyx(dir_):
    sub = dir_ / "bin" / "lib"
    sourced(sub, "alias-common.bash")
    sourced(sub, "alias-git.bash")
    sourced(sub, "configure-Python.bash")
    sourced(sub, "declare-base.bash")
    sourced(sub, "declare-common.bash")
    sourced(sub, "declare-require.bash")
    sourced(sub, "declare.bash")
    sourced(sub, "pve-activate.bash")
    generate_set_path(sub)


def _generate_project(dir_):
    sub = dir_
    sourced(sub, "alias.bash")
    sourced(sub, "context.bash")
    generate_activate(sub)
    sub = dir_ / "cfg" / "sample"
    sourced(sub, "alias.bash")
    sourced(sub, "context.bash")


def generate(directory):
    _generate_briteonyx(directory / "BriteOnyx")
    _generate_project(directory)
    generate_all_briteonyx(directory)


"""DisabledContent
"""

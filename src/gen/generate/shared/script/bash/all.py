#!/usr/bin/env false
"""Generate all BASH scripts."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.complete import generate_activation as activation

# Project modules   (relative references, NOT packaged, in project)
from .activate import generate as generate_activate
from .briteonyx.all import generate as generate_all_briteonyx
from .set_path import generate as generate_set_path


def _generate_briteonyx(dir_):
    sub = dir_ / "bin" / "lib"
    activation(sub, "alias-common.bash")
    activation(sub, "alias-git.bash")
    activation(sub, "configure-Python.bash")
    activation(sub, "declare-base.bash")
    activation(sub, "declare-common.bash")
    activation(sub, "declare-log4bash.bash")
    activation(sub, "declare-require.bash")
    activation(sub, "declare.bash")
    activation(sub, "pve-activate.bash")
    generate_set_path(sub)


def _generate_project(dir_):
    sub = dir_
    activation(sub, "alias.bash")
    activation(sub, "context.bash")
    generate_activate(sub)
    sub = dir_ / "cfg" / "sample"
    activation(sub, "alias.bash")
    activation(sub, "context.bash")


def generate(directory):
    _generate_briteonyx(directory / "BriteOnyx")
    _generate_project(directory)
    generate_all_briteonyx(directory)


"""DisabledContent
"""

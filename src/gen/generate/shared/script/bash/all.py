#!/usr/bin/env false
"""Generate all custom Bash scripts."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)

# Project modules   (relative references, NOT packaged, in project)


"""DisabledContent
from src_gen.script.bash.complete import generate_activation as activation
from .activate import generate as generate_activate
from .alias import generate as generate_alias
from .briteonyx.all import generate as generate_all_briteonyx
from .configure_python import generate as generate_configure_python
from .declare import generate as generate_declare
from .declare_base import generate as generate_declare_base
from .declare_common import generate as generate_declare_common
from .declare_log4bash import generate as generate_declare_log4bash
from .declare_require import generate as generate_declare_require
from .set_path import generate as generate_set_path

def _generate_briteonyx(dir_):
    sub = dir_ / "bin" / "lib"
    generate_alias(sub)
    generate_configure_python(sub)
    generate_declare(sub)
    generate_declare_base(sub)
    generate_declare_common(sub)
    generate_declare_log4bash(sub)
    generate_declare_require(sub)
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


"""

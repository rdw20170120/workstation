#!/usr/bin/env false
"""Generate all shared source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.complete import generate_activation as activation
# Project modules   (relative references, NOT packaged, in project)
from .script.bash.activate import generate as generate_activate
from .script.bash.alias import generate as generate_alias
from .script.bash.configure_python import generate as generate_configure_python
from .script.bash.declare import generate as generate_declare
from .script.bash.declare_base import generate as generate_declare_base
from .script.bash.declare_common import generate as generate_declare_common
from .script.bash.declare_log4bash import generate as generate_declare_log4bash
from .script.bash.declare_require import generate as generate_declare_require
from .script.bash.set_path import generate as generate_set_path


def _generate(dir_):
    sub = dir_
    activation(sub, "alias.bash")
    activation(sub, "context.bash")
    generate_activate(sub)

def _generate_bin(dir_):
    sub = dir_

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

def _generate_cfg(dir_):
    sub = dir_ / "sample"
    activation(sub, "alias.bash")
    activation(sub, "context.bash")

def _generate_doc(dir_):
    sub = dir_

def _generate_src(dir_):
    sub = dir_

def generate(directory):
    _generate(directory)
    _generate_bin(directory / "bin")
    _generate_briteonyx(directory / "BriteOnyx")
    _generate_cfg(directory / "cfg")
    _generate_doc(directory / "doc")
    _generate_src(directory / "src")


"""DisabledContent
"""

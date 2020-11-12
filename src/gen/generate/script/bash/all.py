#!/usr/bin/env false
"""Generate all BASH scripts."""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from src_gen.script.bash.source import generate as gen
from src_gen.script.bash.structure import *

# Co-located modules (relative references, NOT packaged, in project)


def _sourced():
    return [
        header_sourced(),
        todo("DESCRIPTION"),
        line(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def _generate_briteonyx(dir_):
    sub = Path("BriteOnyx", "bin", "lib")
    gen(_sourced(), dir_, sub, "alias-common.bash")
    gen(_sourced(), dir_, sub, "alias-git.bash")
    gen(_sourced(), dir_, sub, "configure-Python.bash")
    gen(_sourced(), dir_, sub, "declare-base.bash")
    gen(_sourced(), dir_, sub, "declare-common.bash")
    gen(_sourced(), dir_, sub, "declare-require.bash")
    gen(_sourced(), dir_, sub, "declare.bash")
    gen(_sourced(), dir_, sub, "pve-activate.bash")


def _generate_cfg(dir_):
    sub = Path("cfg", "sample")
    gen(_sourced(), dir_, sub, "alias.bash")
    gen(_sourced(), dir_, sub, "context.bash")


def _generate_project(dir_):
    sub = Path(".")
    gen(_sourced(), dir_, sub, "alias.bash")
    gen(_sourced(), dir_, sub, "context.bash")


def generate(directory):
    _generate_briteonyx(directory)
    _generate_cfg(directory)
    _generate_project(directory)


"""DisabledContent
"""

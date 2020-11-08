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


def generate(directory):
    sub = Path(".")
    gen(_sourced(), directory, sub, "alias.bash")
    gen(_sourced(), directory, sub, "context.bash")
    sub = Path("BriteOnyx", "bin", "lib")
    gen(_sourced(), directory, sub, "alias-common.bash")
    gen(_sourced(), directory, sub, "alias-git.bash")
    gen(_sourced(), directory, sub, "pve-activate.bash")
    sub = Path("cfg", "sample")
    gen(_sourced(), directory, sub, "alias.bash")
    gen(_sourced(), directory, sub, "context.bash")


"""DisabledContent
"""

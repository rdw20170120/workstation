#!/usr/bin/env false
"""Generate all shared BriteOnyx Bash scripts."""
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
    executed(sub, "app-run")
    executed(sub, "dep-install")
    executed(sub, "show_maybe_missed_source")
    executed(sub, "tool-report")


def _generate_briteonyx(dir_):
    sub = dir_ / "bin"
    executed(sub, "all-capture")
    executed(sub, "all-check")
    executed(sub, "dep-capture")
    executed(sub, "dep-check")
    executed(sub, "dep-reinstall")
    executed(sub, "dep-report")
    executed(sub, "dep-upgrade")
    executed(sub, "env-capture")
    executed(sub, "env-check")
    executed(sub, "env-report")
    executed(sub, "gen-run")
    executed(sub, "prj-clean")
    executed(sub, "prj-wipe")
    executed(sub, "pve-create")
    executed(sub, "pve-recreate")
    executed(sub, "pve-reinstall")
    executed(sub, "pve-rm")
    executed(sub, "py-2to3")
    executed(sub, "py-capture")
    executed(sub, "py-check")
    executed(sub, "py-compile")
    executed(sub, "py-reformat")
    executed(sub, "py-report")
    executed(sub, "sig-check")
    executed(sub, "sig-make")
    executed(sub, "test-run")
    executed(sub, "tool-capture")
    executed(sub, "tool-check")


def generate(directory):
    _generate_bin(directory / "bin")
    _generate_briteonyx(directory / "BriteOnyx")


"""DisabledContent
"""

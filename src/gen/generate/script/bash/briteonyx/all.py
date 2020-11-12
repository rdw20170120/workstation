#!/usr/bin/env false
"""Generate all BriteOnyx BASH scripts."""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from src_gen.script.bash.briteonyx.source import generate as gen
from src_gen.script.bash.briteonyx.structure import *

# Co-located modules (relative references, NOT packaged, in project)


def _executed():
    return [
        header_executed(),
        abort_if_not_activated(),
        line(),
        function(
            "main",
            [
                indent(),
                todo("DESCRIPTION"),
                line(),
                indent(),
                todo("CONTENT"),
                line(),
                indent(),
                return_(0),
                eol(),
            ],
        ),
        eol(),
        line(),
        line("main $@"),
        disabled_content_footer(),
    ]


def _generate_bin(dir_):
    sub = Path("bin")
    gen(_executed(), dir_, sub, "app-run")
    gen(_executed(), dir_, sub, "dep-install")
    gen(_executed(), dir_, sub, "source-may-be-left-out")
    gen(_executed(), dir_, sub, "tool-report")


def _generate_briteonyx(dir_):
    sub = Path("BriteOnyx", "bin")
    gen(_executed(), dir_, sub, "all-capture")
    gen(_executed(), dir_, sub, "all-check")
    gen(_executed(), dir_, sub, "dep-capture")
    gen(_executed(), dir_, sub, "dep-check")
    gen(_executed(), dir_, sub, "dep-reinstall")
    gen(_executed(), dir_, sub, "dep-report")
    gen(_executed(), dir_, sub, "dep-upgrade")
    gen(_executed(), dir_, sub, "env-capture")
    gen(_executed(), dir_, sub, "env-check")
    gen(_executed(), dir_, sub, "env-report")
    gen(_executed(), dir_, sub, "gen-run")
    gen(_executed(), dir_, sub, "prj-clean")
    gen(_executed(), dir_, sub, "prj-wipe")
    gen(_executed(), dir_, sub, "pve-create")
    gen(_executed(), dir_, sub, "pve-recreate")
    gen(_executed(), dir_, sub, "pve-reinstall")
    gen(_executed(), dir_, sub, "pve-rm")
    gen(_executed(), dir_, sub, "py-2to3")
    gen(_executed(), dir_, sub, "py-capture")
    gen(_executed(), dir_, sub, "py-check")
    gen(_executed(), dir_, sub, "py-compile")
    gen(_executed(), dir_, sub, "py-reformat")
    gen(_executed(), dir_, sub, "py-report")
    gen(_executed(), dir_, sub, "sig-check")
    gen(_executed(), dir_, sub, "sig-make")
    gen(_executed(), dir_, sub, "test-run")
    gen(_executed(), dir_, sub, "tool-capture")
    gen(_executed(), dir_, sub, "tool-check")


def _sourced():
    return [
        header_sourced(),
        todo("DESCRIPTION"),
        line(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def generate(directory):
    _generate_bin(directory)
    _generate_briteonyx(directory)


"""DisabledContent
"""

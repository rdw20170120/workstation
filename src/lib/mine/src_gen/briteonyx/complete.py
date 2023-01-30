#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.briteonyx.source import generate
from src_gen.briteonyx.structure import *

# Project modules   (relative references, NOT packaged, in project)


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
        line(),
        disabled_content_footer(),
    ]


def _sourced():
    return [
        header_sourced(),
        todo("DESCRIPTION"),
        line(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def generate_executed(directory, filename):
    generate(_executed(), directory, filename)


def generate_sourced(directory, filename):
    generate(_sourced(), directory, filename)


"""DisabledContent
"""

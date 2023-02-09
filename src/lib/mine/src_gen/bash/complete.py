#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.bash.structure import *

# Project modules   (relative references, NOT packaged, in project)


def executed():
    return [
        header_executed(),
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


def sourced():
    return [
        header_sourced(),
        todo("DESCRIPTION"),
        line(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


"""DisabledContent
"""

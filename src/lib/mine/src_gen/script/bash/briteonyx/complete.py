#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)
from .frame import *
from .material import *


def executed():
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

#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)
from .frame import *
from .material import *


def executed(config):
    return [
        header_executed(config),
        abort_if_not_activated(config),
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


def sourced(config):
    return [
        header_sourced(config),
        todo("DESCRIPTION"),
        line(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


"""DisabledContent
"""

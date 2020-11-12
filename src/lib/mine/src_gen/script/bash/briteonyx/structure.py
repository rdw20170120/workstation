#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from ..structure import *
from .source import my_visitor_map


def abort_if_not_activated():
    return [
        line(),
        string_is_null(vr("BO_Project")),
        and_(),
        eol(),
        indent(),
        log_fatal(
            "This project is NOT ACTIVATED, aborting",
        ),
        and_(),
        eol(),
        indent(),
        exit(99),
        eol(),
    ]


"""DisabledContent
"""

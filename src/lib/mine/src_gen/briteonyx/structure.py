#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.bash.structure import *
from src_gen.briteonyx.source import my_visitor_map

# Project modules   (relative references, NOT packaged, in project)


def abort_if_not_activated():
    return [
        string_is_null(dq(vr("BO_Project"))),
        and_(),
        eol(),
        indent(),
        echo_error("Aborting, this project is NOT ACTIVATED"),
        and_(),
        eol(),
        indent(),
        exit(99),
        eol(),
    ]


"""DisabledContent
"""

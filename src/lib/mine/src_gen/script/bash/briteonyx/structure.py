#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.activating.structure import *

# Project modules   (relative references, NOT packaged, in project)
from .script import my_visitor_map


###############################################################################


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


###############################################################################


def header_executed():
    return [
        shebang_bash(),
        comment("Intended to be executed in a Bash shell."),
        tracing_in_header(),
        no(set_("-e")),
        trap("warn_on_error", "EXIT"),
        eol(),
        rule(),
    ]


def header_sourced():
    return [
        shebang_sourced(),
        comment("Intended to be sourced in a Bash shell."),
        tracing_in_header(),
        no(set_("-e")),
        no(trap("...", "EXIT")),
        rule(),
    ]


"""DisabledContent
"""

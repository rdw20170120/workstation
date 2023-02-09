#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.structure import *
from src_gen.script.structure import _Command
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .script import my_visitor_map


###############################################################################


def log_debug(*element):
    return command("log_debug", dq(element))


def log_error(*element):
    return command("log_error", dq(element))


def log_good(*element):
    return command("log_good", dq(element))


def log_info(*element):
    return command("log_info", dq(element))


def log_warn(*element):
    return command("log_warn", dq(element))


def remembering(name):
    return [
        command("remembering", name),
    ]


###############################################################################


def header_activation():
    return [
        shebang_sourced(),
        comment("Intended to be sourced in a Bash shell during activation."),
        tracing_in_header(),
        no(set_("-e")),
        no(trap("...", "EXIT")),
        rule(),
    ]


def header_executed():
    raise NotImplementedError


def header_sourced():
    raise NotImplementedError


###############################################################################


def maybe_copy_file(source, target):
    return [
        command("maybe_copy_file", source, target),
    ]


###############################################################################


"""DisabledContent
"""

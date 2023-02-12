#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


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


def header_executed():
    raise NotImplementedError


def header_sourced():
    raise NotImplementedError


"""DisabledContent
"""

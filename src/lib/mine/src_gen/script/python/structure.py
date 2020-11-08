#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from ..structure import *
from .source import my_visitor_map


###############################################################################


def disabled_content_footer():
    return [
        line(),
        "'''",
        "DisabledContent",
        eol(),
        "'''",
        eol(),
        line(),
    ]


def imports():
    return [
        comment(
            "Internal packages  (absolute references, distributed with Python)"
        ),
        comment(
            "External packages  (absolute references, NOT distributed with Python)"
        ),
        comment(
            "Library modules    (absolute references, NOT packaged, in project)"
        ),
        comment(
            "Co-located modules (relative references, NOT packaged, in project)"
        ),
        line(),
        line(),
    ]


def library_module_header():
    return [
        shebang_false(),
        '"""TODO: Write',
        eol(),
        '"""',
        eol(),
        imports(),
    ]


def main_module_header():
    return [
        shebang_false(),
        '"""TODO: Write',
        eol(),
        '"""',
        eol(),
        imports(),
    ]


def package_module_header():
    return [
        shebang_false(),
    ]


def script_module_header():
    return [
        shebang_python3(),
        '"""TODO: Write',
        eol(),
        '"""',
        eol(),
        imports(),
    ]


###############################################################################


def shebang_python3():
    return shebang_thru_env("python3")


"""DisabledContent
"""

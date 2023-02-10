#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.python.structure import *

# Project modules   (relative references, NOT packaged, in project)


def generator():
    return [
        header_for_generator(),
        todo("CONTENT"),
        footer_for_disabled_content(),
    ]


def library():
    return [
        header_for_library(),
        todo("CONTENT"),
        footer_for_disabled_content(),
    ]


def main():
    return [
        header_for_main(),
        todo("CONTENT"),
        footer_for_disabled_content(),
    ]


def package():
    return [
        header_for_package(),
    ]


def script():
    return [
        header_for_script(),
        todo("CONTENT"),
        footer_for_disabled_content(),
    ]


def suite():
    return [
        header_for_suite(),
        todo("CONTENT"),
        footer_for_disabled_content(),
    ]


"""DisabledContent
"""

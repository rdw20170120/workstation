#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.python.source import generate
from src_gen.python.structure import *

# Project modules   (relative references, NOT packaged, in project)


def _generator():
    return [
        header_for_generator(),
        todo("CONTENT"),
        footer_for_disabled_content(),
    ]


def _library():
    return [
        header_for_library(),
        todo("CONTENT"),
        footer_for_disabled_content(),
    ]


def _main():
    return [
        header_for_main(),
        todo("CONTENT"),
        footer_for_disabled_content(),
    ]


def _package():
    return [
        header_for_package(),
    ]


def _script():
    return [
        header_for_script(),
        todo("CONTENT"),
        footer_for_disabled_content(),
    ]


def _test():
    return [
        header_for_tests(),
        todo("CONTENT"),
        footer_for_disabled_content(),
    ]


def generate_generator(directory, filename):
    generate(_generator(), directory, filename)


def generate_library(directory, filename):
    generate(_library(), directory, filename)


def generate_main(directory, filename):
    generate(_main(), directory, filename)


def generate_package(directory, filename):
    generate(_package(), directory, filename)


def generate_script(directory, filename):
    generate(_script(), directory, filename)


def generate_test(directory, filename):
    generate(_test(), directory, filename)


"""DisabledContent
"""

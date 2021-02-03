#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.python.source import generate
from src_gen.script.python.structure import *

# Project modules   (relative references, NOT packaged, in project)


def _generator():
    return [
        generator_header(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def _library():
    return [
        library_header(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def _main():
    return [
        main_header(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def _package():
    return [
        package_header(),
    ]


def _script():
    return [
        script_header(),
        todo("CONTENT"),
        disabled_content_footer(),
    ]


def _test():
    return [
        test_header(),
        todo("CONTENT"),
        disabled_content_footer(),
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

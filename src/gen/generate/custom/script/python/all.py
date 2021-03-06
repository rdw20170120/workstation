#!/usr/bin/env false
"""Generate all Python scripts."""
# TODO: Add method for test module
# TODO: Add method for module to generate one source file
# TODO: Add method for module to generate many source files
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.python.complete import generate_library as library
from src_gen.script.python.complete import generate_package as package
from src_gen.script.python.complete import generate_test as test
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)


def _generate_bin(dir_):
    sub = dir_


def _generate_src(dir_):
    sub = dir_
    _generate_src_app(sub / "app" / Config().application_name)
    _generate_src_gen(sub / "gen" / "generate")


def _generate_src_app(dir_):
    sub = dir_


def _generate_src_gen(dir_):
    sub = dir_


def _generate_src_app_task(dir_):
    sub = dir_
    package(sub, "__init__.py")
    library(sub, "bootstrap.py")
    library(sub, "mapping.py")
    library(sub, "scan_directory.py")
    test(sub, "test_mapping.py")
    test(sub, "test_task.py")


def _generate_src_gen(dir_):
    sub = dir_ / "custom" / "document" / "markdown"


def generate(directory):
    _generate_bin(directory / "bin")
    _generate_src(directory / "src")


"""DisabledContent
"""

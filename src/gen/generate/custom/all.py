#!/usr/bin/env false
"""Generate all custom source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.markdown.complete import generate_document as document
from src_gen.briteonyx.complete import (
    generate_executed as executed,
)
from src_gen.briteonyx.complete import generate_sourced as sourced
from src_gen.bash.complete import generate_activation as activation
from src_gen.python.complete import generate_generator as generator
from src_gen.python.complete import generate_library as library
from src_gen.python.complete import generate_main as main
from src_gen.python.complete import generate_package as package
from src_gen.python.complete import generate_script as script
from src_gen.python.complete import generate_test as test
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)


def _generate_bin(dir_):
    sub = dir_
    executed(sub, "sync_on_macOS")
    sub = dir_ / "lib"
    activation(sub, "configure-Anaconda.bash")
    activation(sub, "declare.bash")


def _generate_src(dir_):
    sub = dir_
    _generate_src_app(sub / "app")


def _generate_src_app(dir_):
    sub = dir_ / Config().application_name
    sub = dir_ / Config().application_name / "task"
    package(sub, "__init__.py")
    library(sub, "bootstrap.py")
    library(sub, "mapping.py")
    library(sub, "scan_directory.py")
    test(sub, "test_mapping.py")
    test(sub, "test_task.py")


def generate(directory):
    # NOTE: Typically,
    # there should NOT exist
    # any custom Bash scripts.
    # Any Bash scripts
    # should be shared,
    # or they should be
    # BriteOnyx scripts
    # instead.
    _generate_bin(directory / "bin")
    _generate_src(directory / "src")


"""DisabledContent
"""

#!/usr/bin/env false
"""Generate all custom source contained in this directory tree."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.markdown.complete import document
from src_gen.briteonyx.complete import executed
from src_gen.briteonyx.complete import sourced
from src_gen.bash.complete import activation
from src_gen.python.complete import generator
from src_gen.python.complete import library
from src_gen.python.complete import main
from src_gen.python.complete import package
from src_gen.python.complete import script
from src_gen.python.complete import suite
from utility.config import Config
from src_gen.briteonyx.source import generate as briteonyx
from src_gen.python.source import generate as python

# Project modules   (relative references, NOT packaged, in project)


def _generate_bin(dir_):
    sub = dir_
    briteonyx(executed(), sub, "sync_on_macOS")
    sub = dir_ / "lib"
    briteonyx(activation(), sub, "configure-Anaconda.bash")
    briteonyx(activation(), sub, "declare.bash")


def _generate_src(dir_):
    sub = dir_
    _generate_src_app(sub / "app")


def _generate_src_app(dir_):
    sub = dir_ / Config().application_name
    sub = dir_ / Config().application_name / "task"
    python(package(), sub, "__init__.py")
    python(library(), sub, "bootstrap.py")
    python(library(), sub, "mapping.py")
    python(library(), sub, "scan_directory.py")
    python(suite(), sub, "test_mapping.py")
    python(suite(), sub, "test_task.py")


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

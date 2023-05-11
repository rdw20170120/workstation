#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.material import *

# Project modules   (relative references, NOT packaged, in project)
from .frame import *


def import_(package, as_=None):
    return Import(package, as_)


def import_from(package, item, as_=None):
    return ImportFrom(package, item, as_)


def shebang_python3():
    return shebang_thru_env("python3")


"""DisabledContent
"""

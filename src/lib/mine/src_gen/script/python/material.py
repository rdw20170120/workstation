#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)


def import_(package, as_=None):
    return _Import(package, as_)


def import_from(package, item, as_=None):
    return _ImportFrom(package, item, as_)


def shebang_python3():
    return shebang_thru_env("python3")


"""DisabledContent
"""

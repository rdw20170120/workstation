#!/usr/bin/env false
"""Establish supporting infrastructure for pytest."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
from pytest import fixture

# Library modules   (absolute references, NOT packaged, in project)
from utility.config import Config

# Project modules   (relative references, NOT packaged, in project)


@fixture(scope="session")
def config():
    return Config()


"""DisabledContent
"""

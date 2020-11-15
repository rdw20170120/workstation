#!/usr/bin/env false
"""Test corresponding module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
from pytest import fixture
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)
from task.config import Config


@fixture
def config():
    return Config()

"""DisabledContent
"""


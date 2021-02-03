#!/usr/bin/env false
"""Establish supporting infrastructure for pytest."""
# Internal packages (absolute references, distributed with Python)
from os import environ

# External packages (absolute references, NOT distributed with Python)
from pytest import fixture

# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)
from utility.config import Config


@fixture(scope="session")
def config():
    return Config()


@fixture(scope="session")
def running_humanless():
    try:
        environ["BO_RunningHumanless"]
        return True
    except KeyError:
        return False


"""DisabledContent
"""

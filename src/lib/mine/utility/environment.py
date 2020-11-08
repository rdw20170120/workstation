#!/usr/bin/env false
"""TODO: Write

TODO: REVIEW: this module against its siblings.
"""
# Internal packages  (absolute references, distributed with Python)
from os import environ

# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)


def get(key):
    return environ[key]


def has(key):
    return key in environ


def put(key, value):
    environ[key] = value


"""DisabledContent
"""

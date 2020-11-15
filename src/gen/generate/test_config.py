#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


def test_application_name(config):
    v = config.application_name
    assert is_.instance(v, str)


def test_config(config):
    assert is_.not_none(config)


"""DisabledContent
"""

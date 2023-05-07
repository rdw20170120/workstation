#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .queue import TaskQueue


def test_queue():
    assert is_.not_none(TaskQueue())


"""DisabledContent
"""

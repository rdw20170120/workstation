#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.my_assert import assert_not_none
# Co-located modules (relative references, NOT packaged, in project)
from .queue import TaskQueue


def test_queue():
    assert assert_not_none(TaskQueue())

'''DisabledContent
'''


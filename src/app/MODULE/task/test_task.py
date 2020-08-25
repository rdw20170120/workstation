#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from task.task_manager import TaskManager
from utility.my_assert import assert_not_none
# Co-located modules (relative references, NOT packaged, in project)
from ..config import Config
from .bootstrap import Bootstrap
from .scan_directory import ScanDirectory


def test_bootstrap():
    assert assert_not_none(Bootstrap(TaskManager(Config())))

def test_scan_directory():
    assert assert_not_none(ScanDirectory(TaskManager(Config()), Path()))

'''DisabledContent
'''


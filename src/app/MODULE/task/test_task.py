#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path

# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from task.task_manager import TaskManager
from utility import my_assert as is_

# Co-located modules (relative references, NOT packaged, in project)
from ..config import Config
from .bootstrap import Bootstrap
from .mapping import Mapping
from .scan_directory import ScanDirectory


c = Config()
m = Mapping()
path = Path()
tm = TaskManager(c, m)


def test_bootstrap():
    assert is_.not_none(Bootstrap(tm))


def test_scan_directory():
    assert is_.not_none(ScanDirectory(tm, path))


"""DisabledContent
"""

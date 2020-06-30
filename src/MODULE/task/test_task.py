#!/usr/bin/env false
"""Test task functionality."""
from pathlib import Path

from task.task_manager import TaskManager

from .bootstrap      import Bootstrap
from .scan_directory import ScanDirectory


def test_bootstrap():
    assert Bootstrap(TaskManager(None)) is not None

def test_scan_directory():
    assert ScanDirectory(TaskManager(None), Path()) is not None

'''DisabledContent
'''


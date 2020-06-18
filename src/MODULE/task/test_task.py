#!/usr/bin/env false
"""
"""
from pathlib import Path

from .bootstrap                    import Bootstrap
from .delete_file                  import DeleteFile
from .queue                        import TaskQueue
from .scan_directory               import ScanDirectory
from .task                         import QueuingTask
from .task                         import Task


def test_bootstrap():
    assert Bootstrap(TaskQueue()) is not None

def test_delete_file():
    assert DeleteFile(Path()) is not None

def test_queuing_task():
    assert QueuingTask(TaskQueue()) is not None

def test_scan_directory():
    assert ScanDirectory(TaskQueue(), 'monitor') is not None

def test_task():
    assert Task() is not None

'''DisabledContent
'''


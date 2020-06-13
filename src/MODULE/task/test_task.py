#!/bin/false

from pathlib import Path

from .delete_file_task    import DeleteFileTask
from .first_task          import FirstTask
from .queue               import TaskQueue
from .scan_directory_task import ScanDirectoryTask
from .task                import QueuingTask
from .task                import Task

def test_delete_file_task():
    assert DeleteFileTask(Path()) is not None

def test_first_task():
    assert FirstTask(TaskQueue()) is not None

def test_queuing_task():
    assert QueuingTask(TaskQueue()) is not None

def test_scan_directory_task():
    assert ScanDirectoryTask(TaskQueue()) is not None

def test_task():
    assert Task() is not None


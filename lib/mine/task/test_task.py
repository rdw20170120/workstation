#!/usr/bin/env false
"""Test task functionality."""
from pathlib import Path

from .delete_file  import DeleteFile
from .task         import BaseTask
from .task         import FileSystemTask
from .task         import PlainTask
from .task_manager import TaskManager


def test_base_task():
    assert BaseTask(TaskManager(None)) is not None

def test_delete_file():
    assert DeleteFile(TaskManager(None), Path()) is not None

def test_file_system_task():
    assert FileSystemTask(TaskManager(None)) is not None

def test_plain_task():
    assert PlainTask(TaskManager(None)) is not None

'''DisabledContent
'''


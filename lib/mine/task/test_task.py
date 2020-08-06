#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .delete_file  import DeleteFile
from .task         import FileSystemTask
from .task         import PlainTask
from .task_manager import TaskManager


def test_delete_file():
    assert DeleteFile(TaskManager(None), Path()) is not None

def test_file_system_task():
    assert FileSystemTask(None, TaskManager(None)) is not None

def test_plain_task():
    assert PlainTask(None, TaskManager(None)) is not None

'''DisabledContent
'''


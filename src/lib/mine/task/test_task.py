#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_
from utility.tracked_path import TrackedPath

# Project modules   (relative references, NOT packaged, in project)
from .delete_file import DeleteFile
from .task import FileSystemTask
from .task import PlainTask
from .task_manager import TaskManager


logger = "logger"
source = TrackedPath("title", "/top")
tm = TaskManager(None, None)


def test_delete_file():
    assert is_.not_none(DeleteFile(tm, source))


def test_file_system_task():
    assert is_.not_none(FileSystemTask(logger, tm))


def test_plain_task():
    assert is_.not_none(PlainTask(logger, tm))


"""DisabledContent
"""

#!/usr/bin/env false
"""Delete file."""
# Internal packages (absolute references, distributed with Python)
from logging import getLogger
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from .task import FileSystemTask
from utility import my_assert as is_
from utility.filesystem import delete_file
from utility.tracked_path import TrackedPath

# Project modules   (relative references, NOT packaged, in project)


class DeleteFile(FileSystemTask):
    """Delete file."""

    def __init__(self, task_manager, file_):
        if not isinstance(file_, TrackedPath):
            file_ = file_.tracked_path
        assert is_.instance(file_, TrackedPath)
        self._file = file_
        super().__init__(getLogger(self.__class__.__name__), task_manager)

    def __str__(self):
        return "{} for {}".format(
            self.__class__.__name__,
            self._file.for_log(),
        )

    def _execute(self):
        if self._should_delete_file(self._file):
            delete_file(self._file)

    def _register_sources(self):
        self._register_source(self._file)


"""DisabledContent
"""

#!/bin/false

from pathlib import Path

from utility.filesystem import delete_file

from .task import Task


class DeleteFileTask(Task):
    """Delete the file."""
    def __init__(self, the_file):
        assert isinstance(the_file, Path)
        super().__init__()
        self._file = the_file

    def __str__(self):
        return "DeleteFileTask for file '{}'".format(self._file)

    def execute(self):
        super().execute()
        self._skip_for_dry_run()
        self._skip_if_file_is_missing(self._file)
        delete_file(self._file)


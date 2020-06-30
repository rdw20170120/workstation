#!/usr/bin/env false
"""Delete file."""
from pathlib import Path

from task.task          import FileSystemTask
from utility.filesystem import delete_file


class DeleteFile(FileSystemTask):
    """Delete file."""
    def __init__(self, task_manager, the_file):
        assert isinstance(the_file, Path)
        self._file = the_file
        super().__init__(task_manager)

    def __str__(self):
        return "DeleteFile for file '{}'".format(self._file)

    def _execute(self):
        super()._execute()
        if self._should_delete_file(self._file):
            delete_file(self._file)

    def _register_sources(self):
        self._the_file = self._register_source(self._the_file)

'''DisabledContent
'''


#!/usr/bin/env false
"""
"""
from pathlib import Path

from utility.filesystem import delete_file

from .task import Task


class DeleteFile(Task):
    """Delete the file."""
    def __init__(self, the_file):
        assert isinstance(the_file, Path)
        super().__init__()
        self._file = the_file

    def __str__(self):
        return "DeleteFile for file '{}'".format(self._file)

    def execute(self):
        super().execute()
        if self._should_delete_file(self._file): delete_file(self._file)

'''DisabledContent
'''


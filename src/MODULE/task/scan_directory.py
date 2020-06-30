#!/usr/bin/env false
"""Scan directory for files to process."""
from os      import walk
from pathlib import Path
from pathlib import PurePath as Filename

from logzero import logger as log

from task.task import FileSystemTask

from .mapping import Mapping


m = Mapping()


class ScanDirectory(FileSystemTask):
    """Scan directory for files to process."""
    def __init__(self, task_manager, directory):
        assert isinstance(directory, Path)
        self._directory = directory
        super().__init__(task_manager)

    def __str__(self):
        return "ScanDirectory '{}'".format(self._directory)

    def _consider(self, directory, filename):
        assert isinstance(directory, Path)
        assert isinstance(filename, Filename)

    def _execute(self):
        super()._execute()
        self._scan(self._directory)

    def _register_sources(self):
        self._directory = self._register_source(self._directory)

    def _scan(self, directory):
        assert isinstance(directory, Path)
        log.debug("Scanning directory '%s'", directory)
        for directory, directories, files in walk(directory):
            directory = Path(directory)
            for f in files:
                self._consider(directory, Filename(f))

'''DisabledContent
'''


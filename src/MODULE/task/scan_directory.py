#!/usr/bin/env false
"""Scan directory for files to process."""
# Internal packages  (absolute references, distributed with Python)
from os import walk
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from task.task import FileSystemTask
# Co-located modules (relative references, NOT packaged, in project)
from .mapping import Mapping


m = Mapping()


class ScanDirectory(FileSystemTask):
    """Scan directory for files to process."""
    def __init__(self, task_manager, directory):
        self._directory = directory
        super().__init__(task_manager)

    def __str__(self):
        return "ScanDirectory {}".format(self._directory)

    def _consider(self, directory, filename):
        pass

    def _execute(self):
        super()._execute()
        for directory, directories, files in walk(self._directory):
            for f in files:
                self._consider(directory, f)

    def _register_sources(self):
        self._directory = self._register_source(self._directory)

'''DisabledContent
'''


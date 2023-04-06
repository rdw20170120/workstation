#!/usr/bin/env false
"""Scan directory for files to process."""
# Internal packages  (absolute references, distributed with Python)
from logging import getLogger
from os import walk
from pathlib import Path

# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from task.task import FileSystemTask

# Project modules   (relative references, NOT packaged, in project)
from .mapping import Mapping


m = Mapping()


class ScanDirectory(FileSystemTask):
    """Scan directory for files to process."""

    def __init__(self, task_manager, directory):
        self._directory = directory
        super().__init__(getLogger(self.__class__.__name__), task_manager)

    def __str__(self):
        return "{} for {}".format(
            self.__class__.__name__,
            self._directory.for_log(),
        )

    def _consider(self, the_file):
        self._log.debug("Considering %s", the_file.for_log())

    def _execute(self):
        for directory, directories, files in walk(self._directory):
            d = Path(directory)
            for f in files:
                self._consider(self._directory.for_path(d / f))

    def _register_sources(self):
        self._directory = self._register_source(self._directory)


"""DisabledContent
"""

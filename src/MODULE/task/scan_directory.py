#!/bin/false

from os      import walk
from pathlib import Path
from pathlib import PurePath as Filename

from logzero import logger as log

from ..config import Config
from .mapping import Mapping
from .queue   import TaskQueue
from .task    import QueuingTask


c, m = Config(), Mapping()


class ScanDirectory(QueuingTask):
    """Scan directory for files to process."""
    def __init__(self, queue, directory):
        assert isinstance(queue, TaskQueue)
        super().__init__(queue)
        self._directory = directory

    def __str__(self):
        return "ScanDirectory '{}'".format(self._directory)

    def _consider(self, directory, filename):
        assert isinstance(directory, Path)
        assert isinstance(filename, Filename)

    def _scan(self, directory):
        assert isinstance(directory, Path)
        log.debug("Scanning directory '%s'", directory)
        for directory, directories, files in walk(directory):
            directory = Path(directory)
            for f in files:
                self._consider(directory, Filename(f))

    def execute(self):
        super().execute()
        self._skip_if_directory_is_missing(self._directory)
        self._scan(self._directory)


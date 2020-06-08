#!/bin/false

from os      import walk
from pathlib import Path
from pathlib import PurePath as Filename

from ..config                          import Config
from .delete_file_task                 import DeleteFileTask
from .mapping                          import Mapping
from .queue                            import TaskQueue
from .task                             import QueuingTask

c, m = Config(), Mapping()


class ScanDirectoryTask(QueuingTask):
    """Scan directory for files to process."""
    def __init__(self, queue, monitor):
        assert isinstance(queue, TaskQueue)
        assert isinstance(monitor, str)
        super().__init__(queue)
        self._monitor = monitor

    def __str__(self):
        return "ScanDirectoryTask for monitor '{}'".format(
            self._monitor
            )

    def execute(self):
        super().execute()

        self._skip_if_directory_is_missing(monitor_directory)

        for directory, directories, files in walk(monitor_directory):
            for f in files:
                filename = Filename(f)


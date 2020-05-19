#!/bin/false

from os      import walk
from pathlib import Path as Filename

from ..config                     import Config
from .decompress_file_task        import DecompressFileTask
from .mapping                     import Mapping
from .queue                       import TaskQueue
from .scan_monitor_directory_task import ScanMonitorDirectoryTask
from .task                        import QueuingTask

c, m = Config(), Mapping()


class ScanInboxDirectoryTask(QueuingTask):
    """Scan inbox directory for files to process."""
    def __init__(self, queue):
        assert isinstance(queue, TaskQueue)
        super().__init__(queue)

    def __str__(self):
        return "ScanInboxDirectoryTask"

    def _process(self, the_file):
        if m.file_is_monitor_archive(the_file):
            monitor = m.map_monitor_archive_filename_to_monitor(the_file)
            monitor_archive_file = m.map_monitor_to_monitor_archive_file(
                monitor
                )
            monitor_directory = m.map_monitor_to_monitor_directory(monitor)
            self._queue.put(DecompressFileTask(
                monitor_archive_file, monitor_directory
                ))
            self._queue.put(ScanMonitorDirectoryTask(
                self._queue, monitor
                ))

    def execute(self):
        super().execute()
        for directory, directories, files in walk(c.inbox_directory):
            for f in files:
                self._process(Filename(f))


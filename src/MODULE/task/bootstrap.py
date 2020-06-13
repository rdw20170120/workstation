#!/bin/false

from ..config        import Config
from .queue          import TaskQueue
from .scan_directory import ScanDirectory
from .task           import QueuingTask


class Bootstrap(QueuingTask):
    """First task to populate queue with starting tasks."""
    def __init__(self, queue):
        assert isinstance(queue, TaskQueue)
        super().__init__(queue)

    def __str__(self): return 'Bootstrap'

    def execute(self):
        super().execute()
        self._queue.put(ScanDirectory(self._queue, Config().temporary_directory))


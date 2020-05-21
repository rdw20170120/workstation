#!/bin/false

from .queue                     import TaskQueue
from .scan_inbox_directory_task import ScanInboxDirectoryTask
from .scan_inbox_objects_task   import ScanInboxObjectsTask
from .task                      import QueuingTask


class FirstTask(QueuingTask):
    """First task to populate queue with starting tasks."""
    def __init__(self, queue):
        assert isinstance(queue, TaskQueue)
        super().__init__(queue)

    def __str__(self): return 'FirstTask'

    def execute(self):
        super().execute()
        self._queue.put(ScanInboxObjectsTask(self._queue))
        self._queue.put(ScanInboxDirectoryTask(self._queue))


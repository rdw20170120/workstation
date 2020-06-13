#!/bin/false

from ..config import Config
from .mapping import Mapping
from .queue   import TaskQueue
from .task    import QueuingTask


c, m = Config(), Mapping()


class ScanDirectoryTask(QueuingTask):
    """Scan directory for files to process."""
    def __init__(self, queue):
        assert isinstance(queue, TaskQueue)
        super().__init__(queue)

    def __str__(self):
        return "ScanDirectoryTask".format()

    def execute(self):
        super().execute()


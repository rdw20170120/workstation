#!/usr/bin/env false
"""Bootstrap by creating first tasks."""
from task.task import PlainTask

from .scan_directory import ScanDirectory


class Bootstrap(PlainTask):
    """First task that adds starting tasks."""
    def __init__(self, task_manager):
        super().__init__(task_manager)

    def __str__(self): return 'Bootstrap'

    def execute(self):
        super().execute()
        ScanDirectory(self._tm, self.config.temporary_directory)

'''DisabledContent
'''


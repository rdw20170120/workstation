#!/usr/bin/env false
"""Bootstrap by creating first tasks."""
# Internal packages  (absolute references, distributed with Python)
from logging import getLogger
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from task.task import PlainTask
# Co-located modules (relative references, NOT packaged, in project)
from .scan_directory import ScanDirectory


class Bootstrap(PlainTask):
    """First task that adds starting tasks."""
    def __init__(self, task_manager):
        super().__init__(getLogger(self.__class__.__name__), task_manager)

    def __str__(self): return self.__class__.__name__

    def execute(self):
        super().execute()
        ScanDirectory(self._tm, self.config.temporary_directory)

'''DisabledContent
'''


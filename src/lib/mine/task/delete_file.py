#!/usr/bin/env false
"""Delete file."""
# Internal packages  (absolute references, distributed with Python)
from logging import getLogger
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from task.task import FileSystemTask
from utility.my_assert import assert_instance
# Co-located modules (relative references, NOT packaged, in project)


class DeleteFile(FileSystemTask):
    """Delete file."""
    def __init__(self, task_manager, source_file):
        self._source_file = source_file
        super().__init__(getLogger(self.__class__.__name__), task_manager)

    def __str__(self):
        return "{} for {}".format(
            self.__class__.__name__, self._source_file.for_log(),
            )

    def _execute(self):
        if self._should_delete_file(self._source_file):
            self._source_file.delete()

    def _register_sources(self):
        self._register_source(self._source_file)

'''DisabledContent
'''


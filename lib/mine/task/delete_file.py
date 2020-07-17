#!/usr/bin/env false
"""Delete file."""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from task.task          import FileSystemTask
from utility.filesystem import delete_file
# Co-located modules (relative references, NOT packaged, in project)


class DeleteFile(FileSystemTask):
    """Delete file."""
    def __init__(self, task_manager, the_file):
        assert isinstance(the_file, Path)
        self._file = the_file
        super().__init__(task_manager)

    def __str__(self):
        return "DeleteFile for file '{}'".format(self._file)

    def _execute(self):
        super()._execute()
        if self._should_delete_file(self._file):
            delete_file(self._file)

    def _register_sources(self):
        self._file = self._register_source(self._file)

'''DisabledContent
'''


#!/bin/false

from pathlib import Path

from .task                import Task
from ..utility.filesystem import concatenate_text_file
from ..utility.filesystem import file_size


class AssembleEncounterTask(Task):
    """Assemble encounters into a single file."""
    def __init__(self, source_file, target_file):
        assert isinstance(source_file, Path)
        assert isinstance(target_file, Path)
        super().__init__()
        self._source_file = source_file
        self._target_file = target_file

    def __str__(self):
        m = "AssembleEncounterTask from source file '{}' to target file '{}'"
        return m.format(
            self._source_file, self._target_file
            )

    def execute(self):
        super().execute()
        self._skip_if_file_is_missing(self._source_file)
        size = file_size(self._source_file)
        self._skip_for_dry_run()
        self._skip_for_lack_of_disk_space(size)
        try:
            concatenate_text_file(self._source_file, self._target_file)
        except BaseException:
            self._delete_output_file_upon_exception(self._target_file)
            raise


#!/bin/false

from pathlib import Path

from .task                import Task
from ..utility.filesystem import file_size


class SortTextFileTask(Task):
    """Sort source file to target file."""
    def __init__(self, source_file, target_file):
        assert isinstance(source_file, Path)
        assert isinstance(target_file, Path)
        super().__init__()
        self._source_file = source_file
        self._target_file = target_file

    def __str__(self):
        return "SortTextFileTask from source file '{}' to target file '{}'".format(
            self._source_file, self._target_file
            )

    def execute(self):
        super().execute()
        self._skip_if_file_already_exists(self._target_file)
        self._skip_for_dry_run()
        self._skip_if_file_is_missing(self._source_file)
        self._skip_for_lack_of_disk_space(file_size(self._source_file))
        try:
            with open(self._target_file, 'wt') as writer:
                with open(self._source_file, 'rt') as reader:
                    for line in sorted(reader):
                        writer.write(line)
        except BaseException:
            self._delete_output_target_file_upon_exception(self._target_file)
            raise


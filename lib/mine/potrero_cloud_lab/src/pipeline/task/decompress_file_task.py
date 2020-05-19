#!/bin/false

from pathlib import Path
from zipfile import ZipFile

from .task                import Task
from ..utility.filesystem import file_size


class DecompressFileTask(Task):
    """Decompress the file to the directory."""
    def __init__(self, the_file, the_directory):
        assert isinstance(the_file, Path)
        assert isinstance(the_file, Path)
        super().__init__()
        self._file = the_file
        self._directory = the_directory

    def __str__(self):
        return "DecompressFileTask from file '{}' to directory '{}'".format(
            self._file, self._directory
            )

    def execute(self):
        super().execute()
        self._skip_if_directory_already_exists(self._directory)
        self._skip_for_dry_run()
        self._skip_if_file_is_missing(self._file)
        self._skip_for_lack_of_disk_space(5 * file_size(self._file))
        try:
            with ZipFile(self._file) as f:
                f.extractall(self._directory)
        except BaseException:
            self._delete_output_directory_upon_exception(self._directory)
            raise

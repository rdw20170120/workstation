#!/bin/false

from pathlib import Path

from logzero import logger as log

from ..config import Config
from .task    import Task

c = Config()


class DownloadObjectTask(Task):
    """Download S3 object to the file."""
    def __init__(self, the_object, the_file):
        super().__init__()
        assert isinstance(the_object, dict)
        assert isinstance(the_file, Path)
        self._object = the_object
        self._file = the_file

    def __str__(self):
        return "DownloadObjectTask from object '{}' to file '{}'".format(
            self._object, self._file
            )

    def execute(self):
        super().execute()
        size = self._object['Size']
        self._skip_if_file_already_exists(self._file)
        self._skip_for_dry_run()
        self._skip_for_quick_run(size)
        self._skip_for_lack_of_disk_space(2 * size)
        if c.is_safe_to_download_phi:
            key = self._object['Key']
            try:
                self._get_s3().download_object(
                    c.bucket_name, key, str(self._file)
                    )
            except BaseException:
                self._delete_output_file_upon_exception(self._file)
                raise
        else:
            log.error(
                "Unsafe to download Protected Health Information (PHI), skipping"
                )


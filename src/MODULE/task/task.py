#!/bin/false

from shutil import disk_usage

from logzero import logger as log

from utility.filesystem import delete_directory_tree
from utility.filesystem import delete_file

from ..config import Config


c = Config()


class Task:
    """Base class for tasks."""
    def __init__(self):
        pass

    def _delete_directory_upon_exception(self, directory_path):
        log.warn(
            "Encountered exception, deleting output directory '%s'",
            directory_path
            )
        delete_directory_tree(directory_path, force=True)

    def _delete_file_upon_exception(self, file_path):
        if file_path.exists():
            log.warn(
                "Encountered exception, deleting output file '%s'",
                file_path
                )
            delete_file(file_path)
        else:
            log.warn(
                "Encountered exception, cannot delete missing output file '%s'",
                file_path
                )

    def _skip_for_dry_run(self):
        if c.is_dry_run:
            raise RuntimeError("Skipping for dry run")

    def _skip_for_lack_of_disk_space(self, needed_space_in_bytes):
        du = disk_usage(c.intermediate_directory)
        if du.free < needed_space_in_bytes:
            raise RuntimeError("Skipping for lack of disk space")

    def _skip_for_quick_run(self, source_size):
        if source_size > c.quick_run_limit:
            raise RuntimeError("Skipping for quick run")

    def _skip_if_directory_already_exists(self, the_directory):
        if the_directory.is_dir():
            raise RuntimeError(
                "Skipping since directory '{}' already exists".format(
                    the_directory
                    )
                )

    def _skip_if_directory_is_missing(self, the_directory):
        if not the_directory.exists():
            raise RuntimeError(
                "Skipping since directory '{}' is missing".format(
                    the_directory
                ))

    def _skip_if_file_already_exists(self, the_file):
        skip = the_file.is_file()
        if c.is_forced_run: skip = False
        if skip:
            raise RuntimeError(
                "Skipping since file '{}' already exists".format(the_file)
                )

    def _skip_if_file_is_missing(self, the_file):
        if not the_file.exists():
            raise RuntimeError(
                "Skipping since file '{}' is missing".format(the_file)
                )

    def execute(self):
        log.info("Executing: %s", self)
        self._skip_for_lack_of_disk_space(c.reserved_disk_space_in_bytes)


class QueuingTask(Task):
    """Subclass for tasks that queue more tasks."""
    def __init__(self, queue):
        super().__init__()
        self._queue = queue

    def execute(self):
        super().execute()


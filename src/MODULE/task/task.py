#!/usr/bin/env false
"""
"""
from pathlib import Path
from shutil  import disk_usage

from logzero import logger as log

from utility.filesystem import delete_directory_tree
from utility.filesystem import delete_file

from ..config import Config


c = Config()


class Task:
    """Base class for tasks."""
    def __init__(self, filesystem_location_to_watch=None):
        # TODO: Consider refactoring `filesystem_location_to_watch` to a better location
        if filesystem_location_to_watch is None:
            filesystem_location_to_watch = c.temporary_directory
        assert isinstance(filesystem_location_to_watch, Path)
        self._filesystem_location_to_watch = filesystem_location_to_watch

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

    def _should_delete_file(self, file_path):
        self._skip_for_dry_run()
        if not file_path.exists(): return False
        if not file_path.is_file(): return False
        return True

    def _should_write_file(self, file_path):
        self._skip_for_dry_run()
        if file_path.exists(): return False
        return True

    def _skip_for_dry_run(self):
        if c.is_dry_run:
            raise RuntimeError("Skipping for dry run")

    def _skip_for_lack_of_disk_space(self, needed_space_in_bytes):
        du = disk_usage(self._filesystem_location_to_watch)
        if du.free < needed_space_in_bytes:
            raise RuntimeError("Skipping for lack of disk space")

    def _skip_for_quick_run(self, disk_space_estimate):
        if disk_space_estimate > c.quick_run_limit:
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

'''DisabledContent
'''


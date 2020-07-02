#!/usr/bin/env false
"""Tasks managed by a TaskManager."""
from pathlib import Path
from shutil  import disk_usage

from logzero import logger as log

from utility.filesystem import delete_directory_tree
from utility.filesystem import delete_file

from .task_manager import TaskManager


class BaseTask(object):
    """Base class for tasks managed by a TaskManager."""
    def __init__(self, task_manager):
        super().__init__()
        assert isinstance(task_manager, TaskManager)
        self._tm = task_manager
        self._tm._add(self)

    def _not_implemented(self):
        raise NotImplementedError("This task is not yet implemented")

    @property
    def config(self):
        return self._tm._config

    def execute(self):
        log.info("Executing: %s", self)


class FileSystemTask(BaseTask):
    """Subclass for tasks that manipulate the filesystem."""
    def __init__(self, task_manager):
        super().__init__(task_manager)
        self._sources = []
        self._targets = []

    def _abort_for_dry_run(self):
        if self.config.is_dry_run:
            raise RuntimeError("Aborting for dry run")

    def _abort_for_lack_of_disk_space(self, needed_space_in_bytes):
        du = disk_usage(self.config.filesystem_to_watch)
        if du.free < needed_space_in_bytes:
            raise RuntimeError("Aborting for lack of disk space")

    def _abort_for_quick_run(self, disk_space_estimate):
        if disk_space_estimate > self.config.quick_run_limit:
            raise RuntimeError("Aborting for quick run")

    def _abort_if_any_are_missing(self, name, paths):
        if not len(paths):
            log.warn("No %s registered", name)
        for path in paths:
            if not path.exists():
                raise RuntimeError(
                    "Aborting since {} '{}' is missing".format(name, path)
                    )

    def _abort_if_source_is_missing(self):
        self._abort_if_any_are_missing('source', self._sources)

    def _abort_if_target_is_missing(self):
        self._abort_if_any_are_missing('target', self._targets)

    def _delete_targets_upon_exception(self):
        log.debug("Deleting targets upon exception")
        if self.config.should_leave_output_upon_task_failure: return
        for target in self._targets:
            if target.exists():
                if target.is_dir():
                    log.warn(
                        "Encountered exception"
                        + ", deleting target directory '%s'",
                        target
                        )
                    delete_directory_tree(target, force=True)
                elif target.is_file():
                    log.warn(
                        "Encountered exception"
                        + ", deleting target file '%s'",
                        target
                        )
                    delete_file(target)
                else:
                    log.error(
                        "Encountered exception"
                        + ", cannot delete unrecognized target '%s'",
                        target
                        )
            else:
                log.debug(
                    "Encountered exception"
                    + ", no need to delete absent target '%s'",
                    target
                    )

    def _execute(self):
        """Intended to be overridden in subclasses."""
        pass

    def _register_source(self, source):
        assert isinstance(source, Path)
        self._sources.append(source)
        return source

    def _register_sources(self):
        """Intended to be overridden in subclasses."""
        pass

    def _register_target(self, target):
        assert isinstance(target, Path)
        self._targets.append(target)
        return target

    def _should_delete_directory(self, directory_path):
        self._abort_for_dry_run()
        if not directory_path.exists(): return False
        if not directory_path.is_dir(): return False
        return True

    def _should_delete_file(self, file_path):
        self._abort_for_dry_run()
        if not file_path.exists(): return False
        if not file_path.is_file(): return False
        return True

    def _should_create_target(self, target):
        self._abort_for_dry_run()
        if target.exists():
            log.warn("Skipping creation of existing target '%s'", target)
            return False
        return True

    def _touch_targets(self):
        for target in self._targets:
            touch(target)

    def execute(self):
        """Should NOT be overridden in subclasses."""
        super().execute()
        self._abort_for_dry_run()
        self._abort_for_lack_of_disk_space(
            self.config.reserved_disk_space_in_bytes
            )
        self._register_sources()
        self._abort_if_source_is_missing()

        try:
            if self.config.should_fake_it:
                log.warn("Executing task with FAKE file processing")
                self._touch_targets()
            else:
                self._execute()
            self._abort_if_target_is_missing()
        except RuntimeError as e:
            self._delete_targets_upon_exception()
            raise
        except BaseException as e:
            self._delete_targets_upon_exception()
            raise


class PlainTask(BaseTask):
    """Subclass for plain tasks that only add more tasks."""
    def __init__(self, task_manager):
        super().__init__(task_manager)

    def execute(self):
        super().execute()

'''DisabledContent
'''


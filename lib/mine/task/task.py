#!/usr/bin/env false
"""Tasks managed by a TaskManager."""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
from shutil  import disk_usage
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.filesystem import delete_directory_tree
from utility.filesystem import delete_file
# Co-located modules (relative references, NOT packaged, in project)


class PlainTask(object):
    """Base class for tasks managed by a TaskManager."""
    def __init__(self, logger, task_manager):
        super().__init__()
        self._log = logger
        self._tm = task_manager
        self._tm._add(self)

    def _not_implemented(self):
        raise NotImplementedError("{} is not yet implemented".format(self))

    @property
    def config(self):
        return self._tm.config

    def execute(self):
        self._log.info("Executing: %s", self)


class FileSystemTask(PlainTask):
    """Subclass for tasks that manipulate the filesystem."""
    def __init__(self, logger, task_manager):
        super().__init__(logger, task_manager)
        self._sources = []
        self._targets = []

    def _abort_for_lack_of_disk_space(self, needed_space_in_bytes):
        du = disk_usage(self.config.filesystem_to_watch)
        if du.free < needed_space_in_bytes:
            raise RuntimeError(
                "{} is aborting for lack of disk space".format(self)
                )

    def _abort_for_quick_run(self, disk_space_estimate):
        if disk_space_estimate > self.config.quick_run_limit:
            raise RuntimeError("{} is aborting for quick run".format(self))

    def _abort_if_any_are_missing(self, name, paths):
        if not len(paths):
            self._log.debug("No %s registered in %s", name, self)
        for path in paths:
            if not path.exists():
                raise RuntimeError(
                    "{} is aborting since {} {} is missing".format(
                    self, name, path
                    ))

    def _abort_if_source_is_missing(self):
        self._abort_if_any_are_missing('source', self._sources)

    def _abort_if_target_is_missing(self):
        self._abort_if_any_are_missing('target', self._targets)

    def _delete_targets_upon_exception(self):
        if self.config.should_leave_output_upon_task_failure: return
        self._log.info("%s is deleting targets upon exception", self)
        for target in self._targets:
            if target.exists():
                if target.is_dir():
                    self._log.warn(
                        "%s encountered exception"
                        + ", deleting target %s",
                        self, target.for_log()
                        )
                    delete_directory_tree(target, force=True)
                elif target.is_file():
                    self._log.warn(
                        "%s encountered exception"
                        + ", deleting target %s",
                        self, target.for_log()
                        )
                    delete_file(target)
                else:
                    self._log.error(
                        "%s encountered exception"
                        + ", cannot delete unrecognized target %s",
                        self, target.for_log()
                        )
            else:
                self._log.debug(
                    "%s encountered exception"
                    + ", no need to delete absent target %s",
                    self, target.for_log()
                    )

    def _execute(self):
        raise NotImplementedError(
            "_execute() should be overridden in subclasses"
            )

    def _register_source(self, source, directory=None):
        if source is None: return None
        if directory is not None: source = directory / source
        self._log.debug("Registering source %s", source.for_log())
        self._sources.append(source)
        return source

    def _register_sources(self):
        raise NotImplementedError(
            "_register_sources() should be overridden in subclasses"
            )

    def _register_target(self, target, directory=None):
        if target is None: return None
        if directory is not None: target = directory / target
        self._log.debug("Registering target %s", target.for_log())
        self._targets.append(target)
        return target

    def _should_create_target(self, target, force=False):
        """ Return whether task should create target.

        If the target does not exist,
        then return True.
        If force is True,
        or we are configured for a forced run,
        then return True
        and delete the target first.
        If force is False,
        and we are NOT configured for a forced run,
        then return False.
        Note the special case:
        if force is None,
        then return True
        but do NOT delete the target first
        (which will allow concatenation to an existing file).
        """
        if self.config.is_dry_run: return False
        if force is None: return True
        if not force: force = self.config.is_forced_run
        if not target.exists(): return True
        result = False
        if force:
            result = True
            if target.is_dir():
                self._log.warn('Target creation forced, deleting %s',
                    target.for_log()
                    )
                delete_directory_tree(target, force=True)
            elif target.is_file():
                self._log.warn('Target creation forced, deleting %s',
                    target.for_log()
                    )
                delete_file(target)
            else:
                self._log.error(
                    "Cannot delete unrecognized target %s",
                    self, target.for_log()
                    )
        if not result:
            self._log.warn(
                "%s is skipping creation of existing target %s",
                self, target.for_log()
                )
        return result

    def _should_delete_directory(self, directory_path):
        if self.config.is_dry_run: return False
        if not directory_path.exists(): return False
        if not directory_path.is_dir():
            raise RuntimeError(
                "Aborting delete of unexpected non-directory {}".format(
                path
                ))
        return True

    def _should_delete_file(self, file_path):
        if self.config.is_dry_run: return False
        if not file_path.exists(): return False
        if not file_path.is_file():
            raise RuntimeError(
                "Aborting delete of unexpected non-file {}".format(
                path
                ))
        return True

    def _touch_targets(self):
        for target in self._targets:
            touch(target)

    def execute(self):
        """Should NOT be overridden in subclasses."""
        super().execute()
        self._abort_for_lack_of_disk_space(
            self.config.reserved_disk_space_in_bytes
            )
        self._register_sources()
        self._abort_if_source_is_missing()

        try:
            if self.config.should_fake_it:
                self._log.warn("Executing %s with FAKE file processing", self)
                self._touch_targets()
            else:
                self._execute()
            self._abort_if_target_is_missing()
        except BaseException as e:
            self._log.debug("%s execute() except 1",
                self.__class__.__name__
                )
            try:
                self._delete_targets_upon_exception()
            except BaseException as f:
                self._log.debug("%s execute() except 2",
                    self.__class__.__name__
                    )
                raise f from e
            raise e

'''DisabledContent
'''


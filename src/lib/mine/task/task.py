#!/usr/bin/env false
"""Tasks managed by a TaskManager."""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
from shutil import disk_usage
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from task.exception import Abort
from task.exception import Skip
from utility.filesystem import delete_directory_tree
from utility.filesystem import delete_file
from utility.filesystem import touch
from utility import my_assert as is_
from utility.my_logging import log_exception
# Co-located modules (relative references, NOT packaged, in project)


class PlainTask(object):
    """Base class for tasks managed by a TaskManager."""
    def __init__(self, logger, task_manager):
        assert is_.not_none(logger)
        assert is_.not_none(task_manager)
        self._log = logger
        self._tm = task_manager
        self._tm._add(self)
        super().__init__()

    def _cleanup_upon_exception(self):
        """MAY be overridden in subclasses, starting with call to super()."""
        pass

    def _disabled(self):
        raise Skip(
            "{} is disabled".format(self)
            )
    def _execute(self):
        """MUST be overridden in subclasses, WITHOUT a call to super()."""
        raise NotImplementedError(
            "_execute() MUST be overridden in subclasses"
            )

    def _fake_it(self):
        """MAY be overridden in subclasses, starting with call to super()."""
        self._log.warn("Executing %s with FAKE processing", self)

    def _not_implemented(self):
        raise NotImplementedError("{} is not yet implemented".format(self))

    def _post_execute(self):
        """MAY be overridden in subclasses, starting with call to super()."""
        self._log.debug("Done: %s", self)

    def _pre_execute(self):
        """MAY be overridden in subclasses, starting with call to super()."""
        self._log.debug("Executing: %s", self)

    @property
    def config(self):
        return self._tm.config

    def execute(self):
        """Should NOT be overridden in subclasses."""
        self._pre_execute()
        try:
            if self.config.should_fake_it: self._fake_it()
            else: self._execute()
            self._post_execute()
        except Abort as e:
            self._log.debug(
                "From %s execute() except Abort",
                self.__class__.__name__
                )
            self._log.warn(repr(e))
            raise
        except KeyboardInterrupt as e:
            self._log.debug(
                "From %s execute() except KeyboardInterrupt",
                self.__class__.__name__
                )
            self._log.fatal(repr(e))
            raise
        except NotImplementedError as e:
            self._log.debug(
                "From %s execute() except NotImplementedError",
                self.__class__.__name__
                )
            self._log.warn(repr(e))
            raise
        except Skip as e:
            self._log.debug(
                "From %s execute() except Skip",
                self.__class__.__name__
                )
            self._log.info(repr(e))
            raise
        except BaseException as e:
            self._log.debug(
                "From %s execute() except outer BaseException",
                self.__class__.__name__
                )
            log_exception(self._log, e)
            try:
                self._cleanup_upon_exception()
            except BaseException as f:
                self._log.debug(
                    "From %s execute() except inner BaseException",
                    self.__class__.__name__
                    )
                log_exception(self._log, f)
                raise
            raise


class FileSystemTask(PlainTask):
    """Subclass for tasks that manipulate the filesystem."""
    def __init__(self, logger, task_manager):
        super().__init__(logger, task_manager)
        self._sources = []
        self._targets = []

    def _abort_for_lack_of_disk_space(self, needed_space_in_bytes):
        du = disk_usage(self.config.filesystem_to_watch)
        if du.free < needed_space_in_bytes:
            raise Abort(
                "{} is aborting for lack of disk space".format(self)
                )

    def _abort_for_quick_run(self, disk_space_estimate):
        if disk_space_estimate > self.config.quick_run_limit:
            raise Skip("{} is skipping for quick run".format(self))

    def _abort_if_any_are_missing(self, name, paths):
        if not len(paths):
            self._log.debug("No %s registered in %s", name, self)
        for path in paths:
            assert is_.absolute_path(path)
            if not path.exists():
                raise FileNotFoundError(
                    "{} is aborting since {} {} is missing".format(
                    self, name, path.for_log()
                    ))

    def _abort_if_source_is_missing(self):
        self._abort_if_any_are_missing('source', self._sources)

    def _abort_if_target_is_missing(self):
        self._abort_if_any_are_missing('target', self._targets)

    def _cleanup_upon_exception(self):
        """MAY be overridden in subclasses, starting with call to super()."""
        super()._cleanup_upon_exception()
        if self.config.should_leave_output_upon_task_failure: return
        self._log.debug("%s is deleting targets upon exception", self)
        for target in self._targets:
            assert is_.absolute_path(target)
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

    def _fake_it(self):
        """MAY be overridden in subclasses, starting with call to super()."""
        super()._fake_it()
        self._touch_targets()

    def _post_execute(self):
        """MAY be overridden in subclasses, starting with call to super()."""
        super()._post_execute()
        self._abort_if_target_is_missing()

    def _pre_execute(self):
        """MAY be overridden in subclasses, starting with call to super()."""
        super()._pre_execute()
        self._abort_for_lack_of_disk_space(
            self.config.reserved_disk_space_in_bytes
            )
        self._register_sources()
        self._abort_if_source_is_missing()

    def _register_source(self, source):
        if source is None: return None
        assert is_.absolute_path(source)
        self._log.debug("Registering source %s", source.for_log())
        self._sources.append(source)
        return source

    def _register_sources(self):
        raise NotImplementedError(
            "_register_sources() should be overridden in subclasses"
            )

    def _register_target(self, target):
        if target is None: return None
        assert is_.absolute_path(target)
        self._log.debug("Registering target %s", target.for_log())
        self._targets.append(target)
        return target

    def _should_create_target(self, target, force=False):
        """ Return whether task should create target.

        Logic supports calls that preceed 
        concatenation to an existing file.
        TODO: Add `concatenating` parameter
        """
        if self.config.is_dry_run: return False
        if force is None: return True
        if not force: force = self.config.is_forced_run
        assert is_.absolute_path(target)
        if not target.exists(): return True
        result = False
        if force:
            result = True
            if target.is_dir():
                self._log.info('Target creation forced, deleting %s',
                    target.for_log()
                    )
                delete_directory_tree(target, force=True)
            elif target.is_file():
                self._log.info('Target creation forced, deleting %s',
                    target.for_log()
                    )
                delete_file(target)
            else:
                self._log.error(
                    "Cannot delete unrecognized target %s",
                    self, target.for_log()
                    )
        if not result:
            self._log.debug(
                "%s is skipping creation of existing target %s",
                self, target.for_log()
                )
        return result

    def _should_delete_directory(self, directory_path):
        assert is_.absolute_path(directory_path)
        if self.config.is_dry_run: return False
        if not directory_path.exists(): return False
        if not directory_path.is_dir():
            raise NotADirectoryError(
                "Aborting deletion of unexpected non-directory {}".format(
                directory_path.for_log()
                ))
        return True

    def _should_delete_file(self, file_path):
        assert is_.absolute_path(file_path)
        if self.config.is_dry_run: return False
        if not file_path.exists(): return False
        if not file_path.is_file():
            raise OSError(
                "Aborting deletion of unexpected non-file {}".format(
                file_path.for_log()
                ))
        return True

    def _touch_targets(self):
        for target in self._targets:
            assert is_.absolute_path(target)
            touch(target)
            assert is_.absolute_file(target)

'''DisabledContent
'''


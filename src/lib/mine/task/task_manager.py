#!/usr/bin/env false
"""Manage tasks."""
# Internal packages (absolute references, distributed with Python)
from logging import getLogger

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from .exception import Abort
from .exception import Skip
from .queue import TaskQueue
from utility.my_logging import log_exception

# Project modules   (relative references, NOT packaged, in project)


class TaskManager(object):
    def __init__(self, config, mapping):
        self._log = getLogger(self.__class__.__name__)
        self._config = config
        self._mapping = mapping
        self._q = TaskQueue()
        super().__init__()

    def _add(self, task):
        self._q.put(task)

    def _execute_task(self, the_task):
        try:
            the_task.execute()
        except Abort as e:
            self._log.debug("From %s _execute_task() except Abort", __name__)
            self._log.info(repr(e))
        except KeyboardInterrupt as e:
            self._log.debug(
                "From %s _execute_task() except KeyboardInterrupt", __name__
            )
            self._log.fatal(repr(e))
            raise
        except NotImplementedError as e:
            self._log.debug(
                "From %s _execute_task() except NotImplementedError", __name__
            )
            self._log.debug(repr(e))
        except Skip as e:
            self._log.debug("From %s _execute_task() except Skip", __name__)
            self._log.info(repr(e))
        except BaseException as e:
            self._log.debug("From %s _execute_task() except BaseException", __name__)
            if self._config.should_abort_upon_task_failure:
                log_exception(self._log, e)
                raise
            else:
                log_exception(self._log, e, with_traceback=True)

    @property
    def config(self):
        return self._config

    @property
    def mapping(self):
        return self._mapping

    def run(self):
        self._log.info("Running task manager...")
        while not self._q.empty():
            self._execute_task(self._q.get())
            self._log.debug("Queue contains %d tasks", self._q.length)


"""DisabledContent
"""

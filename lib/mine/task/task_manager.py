#!/usr/bin/env false
"""Manage tasks."""
# Internal packages  (absolute references, distributed with Python)
from logging import getLogger
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .queue import TaskQueue


class TaskManager(object):
    def __init__(self, config):
        self._config = config
        self._log = getLogger(self.__class__.__name__)
        self._q = TaskQueue()
        super().__init__()

    def _add(self, task):
        self._q.put(task)

    def _execute_task(self, the_task):
        try:
            the_task.execute()
        except NotImplementedError as e:
            self._log.debug("%s _execute_task() except 1", __name__)
            self._log.warn(str(e))
        except RuntimeError as e:
            self._log.debug("%s _execute_task() except 2", __name__)
            self._log.error(e)
        except BaseException as e:
            self._log.debug("%s _execute_task() except 3", __name__)
            if self._config.should_abort_upon_task_failure:
                raise e
            else:
                self._log.exception(e)

    @property
    def config(self):
        return self._config

    def run(self):
        self._log.info("Running task manager...")
        while not self._q.empty():
            self._execute_task(self._q.get())
            self._log.debug("Queue contains %d tasks", self._q.length)

'''DisabledContent
'''


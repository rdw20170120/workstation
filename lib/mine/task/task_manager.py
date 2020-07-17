#!/usr/bin/env false
"""Manage tasks."""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from logzero import logger as log
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .queue import TaskQueue


class TaskManager(object):
    def __init__(self, config):
        super().__init__()
        self._config = config
        self._q = TaskQueue()

    def _add(self, task):
        self._q.put(task)

    def _execute_task(self, the_task):
        try:
            the_task.execute()
        except NotImplementedError as e:
            log.warn(str(e))
        except RuntimeError as e:
            log.error(str(e))
        except Exception as e:
            if self._config.should_abort_upon_task_failure: raise
            else: log.exception(e)

    @property
    def config(self):
        return self._config

    def run(self):
        log.info("Running task manager...")
        while not self._q.empty():
            self._execute_task(self._q.get())
            log.debug("Queue contains about %d tasks", self._q.length)

'''DisabledContent
'''


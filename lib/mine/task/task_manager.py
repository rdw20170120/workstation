#!/usr/bin/env false
"""Manage tasks."""
from logzero import logger as log

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
            if self._config.should_abort_upon_task_failure: raise
            else: log.error(str(e))
        except Exception as e:
            if self._config.should_abort_upon_task_failure: raise
            else: log.exception(e)

    def run(self):
        log.info("Running task manager...")
        while not self._q.empty():
            self._execute_task(self._q.get())
            log.debug("Queue contains about %d tasks", self._q.length)

'''DisabledContent
'''


#!/bin/false

from logging import DEBUG

from logzero import logger as log

from ..config    import Config
from .first_task import FirstTask
from .queue      import TaskQueue


c = Config()


class TaskManager(object):
    def __init__(self):
        super().__init__()

    def _execute_task(self, the_task):
        try:
            the_task.execute()
        except NotImplementedError:
            log.error("This task is not yet implemented")
        except RuntimeError as e:
            log.warn(str(e))
        except Exception as e:
            if c.should_abort_on_task_failure:
                raise
            else: log.exception(e)

    def run(self):
        log.info("Running task manager...")
        q = TaskQueue()
        q.put(FirstTask(q))
        while not q.empty():
            self._execute_task(q.get())


''' Disabled content
'''


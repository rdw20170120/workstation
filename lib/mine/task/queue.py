#!/usr/bin/env false
"""Queue to manage tasks."""
# Internal packages  (absolute references, distributed with Python)
from queue import Queue
# External packages  (absolute references, NOT distributed with Python)
from logzero import logger as log
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)


class TaskQueue:
    """Queue to manage tasks.

    Wrap a private implementation to isolate the application from the
    architectural choice.
    """
    def __init__(self):
        self._implementation = Queue() 

    def empty(self):
        return self._implementation.empty()

    def get(self):
        result = self._implementation.get()
        log.debug("Getting from the queue: %s", result)
        return result

    @property
    def length(self):
        return self._implementation.qsize()

    def put(self, task):
        log.debug("Putting on the queue: %s", task)
        self._implementation.put_nowait(task)

'''DisabledContent
'''


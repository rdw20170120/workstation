#!/bin/false

from queue import Queue

from logzero import logger as log


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


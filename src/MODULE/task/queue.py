#!/bin/false

from queue import Queue


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
        return self._implementation.get(block=False)

    def put(self, task):
        self._implementation.put_nowait(task)


#!/bin/false

from pathlib import Path

from .queue import TaskQueue
from .task   import QueuingTask


class DeleteOutboxFileTask(QueuingTask):
    """Delete outbox file mapped to outbox key."""
    def __init__(self, queue, outbox_key):
        assert isinstance(queue, TaskQueue)
        assert isinstance(outbox_key, Path)
        super().__init__(queue)
        self._outbox_key = outbox_key

    def __str__(self):
        return "DeleteOutboxFileTask mapped to outbox key '{}'".format(
            self._outbox_key
            )

    def execute(self):
        super().execute()
        # TODO: Implement
        raise NotImplementedError


#!/bin/false

from .queue import TaskQueue
from .task  import QueuingTask


class DeleteIntermediateObjectsTask(QueuingTask):
    """Delete intermediate objects associated with monitor."""
    def __init__(self, queue, monitor):
        assert isinstance(queue, TaskQueue)
        assert isinstance(monitor, str)
        super().__init__(queue)
        self._monitor = monitor

    def __str__(self):
        return "DeleteIntermediateObjectsTask associated with monitor '{}'".format(
            self._monitor
            )

    def execute(self):
        super().execute()
        raise NotImplementedError


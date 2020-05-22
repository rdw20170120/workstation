#!/bin/false

from .queue import TaskQueue
from .task   import QueuingTask


class DeleteIntermediateFilesTask(QueuingTask):
    """Delete intermediate files associated with monitor."""
    def __init__(self, queue, monitor):
        assert isinstance(queue, TaskQueue)
        assert isinstance(monitor, str)
        super().__init__(queue)
        self._monitor = monitor

    def __str__(self):
        return "DeleteIntermediateFilesTask associated with monitor '{}'".format(
            self._monitor
            )

    def execute(self):
        super().execute()
        # TODO: Implement
        raise NotImplementedError


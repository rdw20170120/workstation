#!/bin/false

from logzero import logger as log

from ..config                  import Config
from .queue                   import TaskQueue
from .scan_outbox_objects_task import ScanOutboxObjectsTask
from .task                     import QueuingTask


class ScanInboxObjectsTask(QueuingTask):
    """Scan S3 inbox for objects to process.

    We must create a task for each object we find in the inbox, so that we can
    follow up with scans for corresponding objects in the outbox.  We cannot
    know whether to process an inbox object until we know whether we have
    already created all of its outbox objects.
    """
    def __init__(self, queue):
        assert isinstance(queue, TaskQueue)
        super().__init__(queue)

    def __str__(self): return 'ScanInboxObjectsTask'

    def execute(self):
        super().execute()
        c = Config()
        prefix = c.inbox_prefix
        for obj in self._get_s3().list_bucket_objects(
            c.bucket_name, str(c.inbox_prefix)
            ):
            if obj['Key'] == prefix:
                log.debug(
                    "Skipping inbox prefix while looking for actual objects"
                    )
            else:
                self._queue.put(ScanOutboxObjectsTask(self._queue, obj))


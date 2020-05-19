#!/bin/false

from pathlib import PurePosixPath as S3Key

from ..config                          import Config
from .queue                            import TaskQueue
from .delete_file_task                 import DeleteFileTask
from .delete_intermediate_files_task   import DeleteIntermediateFilesTask
from .delete_intermediate_objects_task import DeleteIntermediateObjectsTask
from .delete_outbox_file_task          import DeleteOutboxFileTask
from .download_object_task             import DownloadObjectTask
from .mapping                          import Mapping
from .task                             import QueuingTask

c, m = Config(), Mapping()


class ScanOutboxObjectsTask(QueuingTask):
    """Scan S3 outbox for objects corresponding to the S3 inbox object.
    
    If any of the outbox objects are missing for an inbox object, then we must
    still process the inbox object to create them.  If all the outbox objects
    are present, then we have the option to clean up in local storage and S3.
    """
    def __init__(self, queue, monitor_archive_object):
        assert isinstance(queue, TaskQueue)
        assert isinstance(monitor_archive_object, dict)
        super().__init__(queue)
        self._monitor_archive_object = monitor_archive_object

    def __str__(self):
        return "ScanOutboxObjectsTask for inbox object: {}".format(
            self._monitor_archive_object
            )

    def execute(self):
        super().execute()
        monitor_archive_key = S3Key(self._monitor_archive_object['Key'])
        monitor = m.map_monitor_archive_key_to_monitor(monitor_archive_key)
        monitor_archive_file = m.map_monitor_to_monitor_archive_file(
            monitor
            )
        must_process_object = False
        outbox_keys = m.map_monitor_to_outbox_keys(monitor)
        for k in outbox_keys:
            if k is not None:
                objects = self._get_s3().list_bucket_objects(c.bucket_name, str(k))
                if len(objects) == 0: must_process_object = True
        if must_process_object:
            self._queue.put(DownloadObjectTask(
                self._monitor_archive_object, monitor_archive_file
                ))
        else:
            # NOTE: Do these in reverse order of creation, so they will not be
            # recreated if deletions are interrupted
            self._queue.put(DeleteIntermediateFilesTask(self._queue, monitor))
            self._queue.put(DeleteIntermediateObjectsTask(self._queue, monitor))
            self._queue.put(DeleteFileTask(monitor_archive_file))
            for k in outbox_keys:
                self._queue.put(DeleteOutboxFileTask(k))


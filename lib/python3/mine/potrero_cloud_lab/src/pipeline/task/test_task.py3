#!/bin/false

from pathlib import Path

from .combine_encounters_task          import CombineEncountersTask
from .decompress_file_task             import DecompressFileTask
from .delete_file_task                 import DeleteFileTask
from .delete_intermediate_files_task   import DeleteIntermediateFilesTask
from .delete_intermediate_objects_task import DeleteIntermediateObjectsTask
from .delete_outbox_file_task          import DeleteOutboxFileTask
from .download_object_task             import DownloadObjectTask
from .extract_accuryn_data_task        import ExtractAccurynDataTask
from .extract_encounter_task           import ExtractEncounterTask
from .first_task                       import FirstTask
from .organize_data_by_encounters_task import OrganizeDataByEncountersTask
from .organize_encounter_data_task     import OrganizeEncounterDataTask
from .queue                            import TaskQueue
from .scan_inbox_objects_task          import ScanInboxObjectsTask
from .scan_monitor_directory_task      import ScanMonitorDirectoryTask
from .scan_outbox_objects_task         import ScanOutboxObjectsTask
from .sort_text_file_task              import SortTextFileTask
from .task                             import QueuingTask
from .task                             import Task

def test_combine_encounters_task():
    assert CombineEncountersTask(Path(), Path()) is not None

def test_decompress_file_task():
    assert DecompressFileTask(Path(), Path()) is not None

def test_delete_file_task():
    assert DeleteFileTask(Path()) is not None

def test_delete_intermediate_files_task():
    assert DeleteIntermediateFilesTask(TaskQueue(), 'monitor') is not None

def test_delete_intermediate_objects_task():
    assert DeleteIntermediateObjectsTask(TaskQueue(), 'monitor') is not None

def test_delete_outbox_file_task():
    assert DeleteOutboxFileTask(TaskQueue(), Path()) is not None

def test_download_object_task():
    assert DownloadObjectTask({}, Path()) is not None

def test_extract_accuryn_data_task():
    assert ExtractAccurynDataTask(Path(), Path()) is not None

def test_extract_encounter_task():
    assert ExtractEncounterTask('monitor', Path(), Path()) is not None

def test_first_task():
    assert FirstTask(TaskQueue()) is not None

def test_organize_data_by_encounters_task():
    assert OrganizeDataByEncountersTask(TaskQueue(), Path()) is not None

def test_organize_encounter_data_task():
    assert OrganizeEncounterDataTask({}) is not None

def test_queuing_task():
    assert QueuingTask(TaskQueue()) is not None

def test_scan_inbox_objects_task():
    assert ScanInboxObjectsTask(TaskQueue()) is not None

def test_scan_monitor_directory_task():
    assert ScanMonitorDirectoryTask(TaskQueue(), 'monitor') is not None

def test_scan_outbox_objects_task():
    assert ScanOutboxObjectsTask(TaskQueue(), {}) is not None

def test_sort_text_file_task():
    assert SortTextFileTask(Path(), Path()) is not None

def test_task():
    assert Task() is not None


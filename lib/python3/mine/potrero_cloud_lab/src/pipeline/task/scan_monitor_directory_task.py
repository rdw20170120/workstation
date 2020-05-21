#!/bin/false

from os      import walk
from pathlib import Path
from pathlib import PurePath as Filename

from ..config                          import Config
from .assemble_encounter_task          import AssembleEncounterTask
from .combine_encounters_task          import CombineEncountersTask
from .delete_file_task                 import DeleteFileTask
from .extract_accuryn_data_task        import ExtractAccurynDataTask
from .extract_encounter_task           import ExtractEncounterTask
from .mapping                          import Mapping
from .organize_data_by_encounters_task import OrganizeDataByEncountersTask
from .queue                            import TaskQueue
from .sort_text_file_task              import SortTextFileTask
from .task                             import QueuingTask

c, m = Config(), Mapping()


class ScanMonitorDirectoryTask(QueuingTask):
    """Scan monitor directory for files to process."""
    def __init__(self, queue, monitor):
        assert isinstance(queue, TaskQueue)
        assert isinstance(monitor, str)
        super().__init__(queue)
        self._monitor = monitor

    def __str__(self):
        return "ScanMonitorDirectoryTask for monitor '{}'".format(
            self._monitor
            )

    def execute(self):
        super().execute()
        stage_3 = m.map_monitor_to_raw_encounter_file(self._monitor)
        stage_4 = m.map_monitor_to_sorted_encounter_file(self._monitor)
        stage_5 = m.map_monitor_to_combined_encounter_file(self._monitor)
        self._queue.put(DeleteFileTask(stage_3))
        self._queue.put(DeleteFileTask(stage_4))
        self._queue.put(DeleteFileTask(stage_5))

        monitor_directory = m.map_monitor_to_monitor_directory(self._monitor)
        self._skip_if_directory_is_missing(monitor_directory)
        for directory, directories, files in walk(monitor_directory):
            for f in files:
                filename = Filename(f)
                if m.file_is_stage_0(filename):
                    stage_0 = Path(directory, f)
                    stage_1 = m.map_stage_0_file_to_stage_1_file(
                        self._monitor, stage_0
                        )
                    stage_2 = m.map_stage_0_file_to_stage_2_file(
                        self._monitor, stage_0
                        )
                    self._queue.put(ExtractAccurynDataTask(stage_0, stage_1))
                    self._queue.put(ExtractEncounterTask(
                        self._monitor, stage_1, stage_2
                        ))
                    self._queue.put(AssembleEncounterTask(stage_2, stage_3))

        self._queue.put(SortTextFileTask(stage_3, stage_4))
        self._queue.put(CombineEncountersTask(stage_4, stage_5))
        self._queue.put(OrganizeDataByEncountersTask(self._queue, stage_5))


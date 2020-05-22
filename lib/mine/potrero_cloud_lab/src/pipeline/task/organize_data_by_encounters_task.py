#!/bin/false

from pathlib import Path

from ..utility.text                import dict_from_string
from .organize_encounter_data_task import OrganizeEncounterDataTask
from .queue                        import TaskQueue
from .task                         import QueuingTask


class OrganizeDataByEncountersTask(QueuingTask):
    """Organize data by encounters."""
    def __init__(self, queue, encounters_file):
        assert isinstance(encounters_file, Path)
        assert isinstance(queue, TaskQueue)
        super().__init__(queue)
        self._encounters_file = encounters_file

    def __str__(self):
        m = "OrganizeDataByEncountersTask from file '{}'"
        return m.format(self._encounters_file)

    def execute(self):
        super().execute()
        self._skip_if_file_is_missing(self._encounters_file)
        with open(self._encounters_file, 'rt') as reader:
            for e in reader:
                encounter = dict_from_string(e)
                self._queue.put(OrganizeEncounterDataTask(encounter))


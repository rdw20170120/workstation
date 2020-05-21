#!/bin/false

from pathlib import Path

from avro.datafile import DataFileReader
from avro.io       import DatumReader
from logzero       import logger as log

from ..config             import Config
from ..data.encounter     import SingleFileEncounter
from ..utility.filesystem import file_size
from ..utility.filesystem import touch
from .task                import Task
from .mapping             import Mapping

c, m = Config(), Mapping()


class ExtractEncounterTask(Task):
    """Extract encounters from source file into target file."""
    def __init__(self, monitor, source_file, target_file):
        assert isinstance(monitor, str)
        assert isinstance(source_file, Path)
        assert isinstance(target_file, Path)
        super().__init__()
        self._monitor = monitor
        self._source_file = source_file
        self._target_file = target_file

    def __str__(self):
        m = "ExtractEncounterTask from source file '{}' into target file '{}'"
        return m.format(self._source_file, self._target_file)

    def _consider(self, accuryn_record):
        """Consider whether Accuryn record begins or continues an encounter."""
        # TODO: Adjust logging so this next line can be left uncommented
        # log.debug("Considering Accuryn record: %s", accuryn_record)
        if self._encounter:
            if not self._encounter.continues(accuryn_record):
                self._write()
                self._make_new(accuryn_record)
        else:
            self._make_new(accuryn_record)

    def _extract_encounter(self):
        monitor_directory = m.map_monitor_to_monitor_directory(
            self._monitor
            )
        self._extracted_file = self._source_file.relative_to(
            monitor_directory
            )
        self._encounter = None
        with self._target_file.open('wt') as self._writer:
            with DataFileReader(
                self._source_file.open('rb'), DatumReader()
                ) as self._reader:
                for r in self._reader:
                    self._consider(r)
            self._write()

    def _make_new(self, accuryn_record):
        self._encounter = SingleFileEncounter(
            self._monitor, self._extracted_file, accuryn_record
            )

    def _write(self):
        if self._encounter:
            self._writer.write(str(self._encounter.record()) + '\n')

    def _fake_execute(self):
        log.warn("Executing task with FAKE data processing")
        touch(self._target_file)

    def _real_execute(self):
        self._skip_if_file_is_missing(self._source_file)
        size = file_size(self._source_file)
        self._skip_if_file_already_exists(self._target_file)
        self._skip_for_dry_run()
        self._skip_for_quick_run(size)
        # This target file is tiny compared to most, so ignore disk usage
        self._skip_for_lack_of_disk_space(0)
        try:
            self._extract_encounter()
        except BaseException:
            self._delete_output_file_upon_exception(self._target_file)
            raise

    def execute(self):
        super().execute()
        if c.should_fake_it: self._fake_execute()
        else:                self._real_execute()


#!/bin/false

from pathlib import Path

from logzero import logger as log

from ..config             import Config
from ..data.encounter     import CombinedEncounter
from ..utility.filesystem import file_size
from ..utility.filesystem import touch
from ..utility.text       import dict_from_string
from .task                import Task

c = Config()


class CombineEncountersTask(Task):
    """Combine encounters from source file into target file."""
    def __init__(self, source_file, target_file):
        assert isinstance(source_file, Path)
        assert isinstance(target_file, Path)
        super().__init__()
        self._source_file = source_file
        self._target_file = target_file
        self._combined = None
        self._identifier = 0

    def __str__(self):
        m = "CombineEncountersTask from source file '{}' into target file '{}'"
        return m.format(self._source_file, self._target_file)

    def _combine_encounters(self):
        with self._target_file.open('wt') as self._writer:
            with self._source_file.open('rt') as self._reader:
                for e in self._reader:
                    encounter = dict_from_string(e)
                    self._consider(encounter)
            self._write()

    def _consider(self, encounter):
        """Consider whether encounter begins or continues."""
        # TODO: Adjust logging so this next line can be left uncommented
        # log.debug("Considering encounter: %s", encounter)
        if self._combined:
            if not self._combined.continues(encounter):
                self._write()
                self._make_new(encounter)
        else:
            self._make_new(encounter)

    def _fake_execute(self):
        log.warn("Executing task with FAKE data processing")
        touch(self._target_file)

    def _make_new(self, encounter):
        self._identifier += 1
        self._combined = CombinedEncounter(self._identifier, encounter)

    def _real_execute(self):
        self._skip_if_file_already_exists(self._target_file)
        self._skip_for_dry_run()
        self._skip_if_file_is_missing(self._source_file)
        size = file_size(self._source_file)
        self._skip_for_quick_run(size)
        # This target file is tiny compared to most, so ignore disk usage
        # self._skip_for_lack_of_disk_space(size)
        try:
            self._combine_encounters()
        except BaseException:
            self._delete_output_file_upon_exception(self._target_file)
            raise

    def _write(self):
        if self._combined:
            self._writer.write(str(self._combined.record()) + '\n')

    def execute(self):
        super().execute()
        if c.should_fake_it: self._fake_execute()
        else:                self._real_execute()


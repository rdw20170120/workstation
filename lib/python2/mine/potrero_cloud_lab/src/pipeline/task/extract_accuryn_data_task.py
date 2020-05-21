#!/bin/false

from pathlib import Path

from avro.datafile import DataFileWriter
from avro.io       import DatumWriter
from avro.schema   import Parse
from logzero       import logger as log

from ..config             import Config
from ..data.accuryn_data  import AccurynData
from ..utility.filesystem import file_size
from ..utility.filesystem import touch
from .task                import Task

c = Config()


class ExtractAccurynDataTask(Task):
    """Extract raw Accuryn data from the source file to the target file."""
    def __init__(self, source_file, target_file):
        assert isinstance(source_file, Path)
        assert isinstance(target_file, Path)
        super().__init__()
        self._source_file = source_file
        self._target_file = target_file

    def __str__(self):
        m = "ExtractAccurynDataTask from source file '{}' to target file '{}'"
        return m.format(self._source_file, self._target_file)

    def _extract_accuryn_data(self, source_file, target_file):
        assert isinstance(source_file, Path)
        assert isinstance(target_file, Path)
        schema = Parse(c.avro_extracted_schema_file.read_text(
            encoding='utf_8'
            ))
        with DataFileWriter(
            target_file.open('wb'),
            DatumWriter(),
            schema
            ) as w:
            for r in AccurynData(source_file):
                w.append(r)

    def _fake_execute(self):
        log.warn("Executing task with FAKE data processing")
        touch(self._target_file)

    def _real_execute(self):
        self._skip_if_file_is_missing(self._source_file)
        size = file_size(self._source_file)
        self._skip_if_file_already_exists(self._target_file)
        self._skip_for_dry_run()
        self._skip_for_quick_run(size)
        self._skip_for_lack_of_disk_space(2 * size)
        try:
            self._extract_accuryn_data(self._source_file, self._target_file)
        except BaseException:
            self._delete_output_file_upon_exception(self._target_file)
            raise

    def execute(self):
        super().execute()
        if c.should_fake_it: self._fake_execute()
        else:                self._real_execute()


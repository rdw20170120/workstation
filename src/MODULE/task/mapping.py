#!/bin/false

from pathlib import Path
from pathlib import PurePath as Filename
from pathlib import PurePath
from pathlib import PurePosixPath as Subpath

from logzero import logger as log

from utility.filesystem import name_has_extension
from utility.filesystem import split_file_name
from utility.text       import string_without_suffix

from ..config import Config

c = Config()


class Mapping:
    """Mappings among filesystem pathnames."""
    pass


'''
    def _encounter_file(self, monitor):
        assert isinstance(monitor, str)
        return self._intermediate_file(
            monitor, None, Filename('encounter' + c.list_file_extension)
            )

    def _encounter_subset_file(self, monitor, encounter_id, subset):
        assert isinstance(encounter_id, int)
        assert isinstance(monitor, str)
        assert isinstance(subset, str)
        s = "no_phi-encounter_{:03d}-{}{}"
        result = self._monitor_directory(monitor) / s.format(
            encounter_id, subset, c.stage_7_file_suffix
            )
        assert isinstance(result, Path)
        return result

    def _extract_monitor(self, filename):
        assert isinstance(filename, Filename)
        monitor, extension = self._split_monitor_archive_filename(filename)
        assert extension == c.monitor_archive_file_extension
        assert isinstance(monitor, str)
        return monitor

    def _intermediate_file(self, monitor, subpath, filename):
        assert isinstance(monitor, str)
        assert isinstance(filename, Filename)
        if subpath is None:
            return c.intermediate_directory / monitor / filename
        else:
            assert isinstance(subpath, Subpath)
            return c.intermediate_directory / monitor / subpath / filename

    def _monitor_archive_file(self, monitor):
        assert isinstance(monitor, str)
        return c.inbox_directory / self._monitor_filename(monitor)

    def _monitor_directory(self, monitor):
        assert isinstance(monitor, str)
        return c.intermediate_directory / monitor

    def _monitor_filename(self, monitor, extension=None):
        assert isinstance(monitor, str)
        if extension is None: extension = c.monitor_archive_file_extension
        assert extension
        return Filename(monitor + extension)

    def _monitor_prefix(self, monitor):
        assert isinstance(monitor, str)
        return c.intermediate_prefix / monitor

    def _outbox_key(self, monitor, extension):
        assert isinstance(monitor, str)
        assert extension
        name = self._monitor_filename(monitor, extension)
        assert isinstance(name, Filename)
        return c.outbox_prefix / name

    def _split_intermediate_file(self, monitor, intermediate_file):
        assert isinstance(monitor, str)
        assert isinstance(intermediate_file, Path)
        subpath = intermediate_file.parent
        subpath = subpath.relative_to(c.intermediate_directory)
        subpath = subpath.relative_to(monitor)
        assert isinstance(subpath, Subpath)
        name = Filename(intermediate_file.name)
        return subpath, name

    def _split_monitor_archive_file(self, the_file):
        assert isinstance(the_file, PurePath)
        directory, name = the_file.parent, Filename(the_file.name)
        assert directory == c.inbox_directory
        return name

    def _split_monitor_archive_filename(self, filename):
        assert isinstance(filename, Filename)
        monitor, extension = split_file_name(filename)
        assert isinstance(monitor, str)
        assert isinstance(extension, str)
        return monitor, extension

    def _split_monitor_archive_key(self, the_key):
        assert isinstance(the_key, S3Key)
        prefix, name = the_key.parent, Filename(the_key.name)
        assert prefix == c.inbox_prefix
        return prefix, name

    def encounter_1_Hz_file(self, monitor, encounter_id):
        return self._encounter_subset_file(monitor, encounter_id, '1_Hz')

    def encounter_100_Hz_file(self, monitor, encounter_id):
        return self._encounter_subset_file(monitor, encounter_id, '100_Hz')

    def encounter_sparse_file(self, monitor, encounter_id):
        return self._encounter_subset_file(monitor, encounter_id, 'sparse')

    def file_is_monitor_archive(self, filename):
        assert isinstance(filename, Filename)
        return str(filename).endswith(c.monitor_archive_file_extension)

    def file_is_stage_0(self, filename):
        assert isinstance(filename, Filename)
        return str(filename).endswith(c.stage_0_file_suffix)

    def file_is_stage_1(self, filename):
        assert isinstance(filename, Filename)
        return str(filename).endswith(c.stage_1_file_suffix)

    def file_is_stage_2(self, filename):
        assert isinstance(filename, Filename)
        return str(filename).endswith(c.stage_2_file_suffix)

    def map_monitor_archive_filename_to_monitor(self, monitor_archive_filename):
        assert isinstance(monitor_archive_filename, Filename)
        monitor = self._extract_monitor(monitor_archive_filename)
        assert isinstance(monitor, str)
        return monitor

    def map_monitor_archive_key_to_monitor(self, monitor_archive_key):
        assert isinstance(monitor_archive_key, S3Key)
        prefix, name = self._split_monitor_archive_key(monitor_archive_key)
        assert prefix == c.inbox_prefix
        assert isinstance(name, Filename)
        monitor = self._extract_monitor(name)
        assert isinstance(monitor, str)
        return monitor

    def map_monitor_to_anonymized_encounter_file(self, monitor):
        assert isinstance(monitor, str)
        return self._intermediate_file(
            monitor, None, Filename('encounter' + c.stage_6_file_suffix)
            )

    def map_monitor_to_combined_encounter_file(self, monitor):
        assert isinstance(monitor, str)
        return self._intermediate_file(
            monitor, None, Filename('encounter' + c.stage_5_file_suffix)
            )

    def map_monitor_to_monitor_archive_file(self, monitor):
        return self._monitor_archive_file(monitor)

    def map_monitor_to_monitor_directory(self, monitor):
        return self._monitor_directory(monitor)

    def map_monitor_to_outbox_keys(self, monitor):
        assert isinstance(monitor, str)
        result = []
        result.append(self._outbox_key(
            monitor, c.column_oriented_data_file_extension
            ))
        result.append(self._outbox_key(
            monitor, c.row_oriented_data_file_extension
            ))
        return result

    def map_monitor_to_raw_encounter_file(self, monitor):
        assert isinstance(monitor, str)
        return self._intermediate_file(
            monitor, None, Filename('encounter' + c.stage_3_file_suffix)
            )

    def map_monitor_to_sorted_encounter_file(self, monitor):
        assert isinstance(monitor, str)
        return self._intermediate_file(
            monitor, None, Filename('encounter' + c.stage_4_file_suffix)
            )

    def map_stage_0_file_to_stage_1_file(self, monitor, the_file):
        assert isinstance(monitor, str)
        assert isinstance(the_file, Path)
        subpath, name = self._split_intermediate_file(monitor, the_file)
        assert isinstance(subpath, Subpath)
        assert isinstance(name, Filename)
        assert self.file_is_stage_0(name)
        n = string_without_suffix(str(name), c.stage_0_file_suffix)
        assert n
        name = Filename(n + c.stage_1_file_suffix)
        assert self.file_is_stage_1(name)
        return self._intermediate_file(monitor, subpath, name)

    def map_stage_0_file_to_stage_2_file(self, monitor, the_file):
        assert isinstance(monitor, str)
        assert isinstance(the_file, Path)
        subpath, name = self._split_intermediate_file(monitor, the_file)
        assert isinstance(subpath, Subpath)
        assert isinstance(name, Filename)
        assert self.file_is_stage_0(name)
        n = string_without_suffix(str(name), c.stage_0_file_suffix)
        assert n
        name = Filename(n + c.stage_2_file_suffix)
        assert self.file_is_stage_2(name)
        return self._intermediate_file(monitor, subpath, name)

'''


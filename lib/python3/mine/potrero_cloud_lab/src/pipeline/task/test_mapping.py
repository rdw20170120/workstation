#!/bin/false

from pathlib import Path
from pathlib import PurePath as Filename
from pathlib import PurePosixPath as S3Key
from pathlib import PurePosixPath as Subpath

from ..config             import Config
from .mapping             import Mapping
from ..utility.filesystem import name_has_extension

c, m = Config(), Mapping()

monitor = 'MONITOR'
filename = Filename(monitor + c.monitor_archive_file_extension)
subpath = Subpath('sub/path')

# Test private interface

def test_extract_monitor():
    assert m._extract_monitor(filename) == monitor

def test_intermediate_file_having_subpath():
    a = Filename('SOMETHING.ext')
    z = c.intermediate_directory / monitor / subpath / a
    assert m._intermediate_file(monitor, subpath, a) == z

def test_intermediate_file_missing_subpath():
    a = Filename('SOMETHING.ext')
    z = c.intermediate_directory / monitor / a
    assert m._intermediate_file(monitor, None, a) == z

def test_monitor_archive_file():
    p = c.inbox_directory / filename
    assert m._monitor_archive_file(monitor) == p

def test_monitor_directory():
    d = c.intermediate_directory / monitor
    assert m._monitor_directory(monitor) == d

def test_monitor_filename():
    assert m._monitor_filename(monitor) == filename
    assert m._monitor_filename(
        monitor, c.monitor_archive_file_extension
        ) == filename

def test_monitor_prefix():
    p = c.intermediate_prefix / monitor
    assert m._monitor_prefix(monitor) == p

def test_outbox_key():
    k = c.outbox_prefix / filename
    assert m._outbox_key(monitor, c.monitor_archive_file_extension) == k

def test_split_intermediate_file_having_subpath():
    z = Filename('SOMETHING.ext')
    y = c.intermediate_directory / monitor / subpath / z
    x, w = m._split_intermediate_file(monitor, y)
    assert x == subpath
    assert w == z

def test_split_intermediate_file_missing_subpath():
    z = Filename('SOMETHING.ext')
    y = c.intermediate_directory / monitor / z
    x, w = m._split_intermediate_file(monitor, y)
    assert x == Subpath('.')
    assert w == z

def test_split_monitor_archive_file():
    f = c.inbox_directory / filename
    n = m._split_monitor_archive_file(f)
    assert n == filename

def test_split_monitor_archive_filename():
    n, e = m._split_monitor_archive_filename(filename)
    assert n == monitor
    assert e == c.monitor_archive_file_extension

def test_split_monitor_archive_key():
    k = c.inbox_prefix / filename
    p, f = m._split_monitor_archive_key(k)
    assert p == c.inbox_prefix
    assert f == filename

# Test public interface

def test_encounter_1_Hz_file():
    f = (
        c.intermediate_directory /
        monitor /
        ('no_phi-encounter_099-1_Hz' + c.stage_6_file_suffix)
        )
    assert m.encounter_1_Hz_file(monitor, 99) == f

def test_encounter_100_Hz_file():
    f = (
        c.intermediate_directory /
        monitor /
        ('no_phi-encounter_099-100_Hz' + c.stage_6_file_suffix)
        )
    assert m.encounter_100_Hz_file(monitor, 99) == f

def test_encounter_sparse_file():
    f = (
        c.intermediate_directory /
        monitor /
        ('no_phi-encounter_099-sparse' + c.stage_6_file_suffix)
        )
    assert m.encounter_sparse_file(monitor, 99) == f

def test_file_is_monitor_archive():
    f = Filename('SOMETHING' + c.monitor_archive_file_extension)
    assert m.file_is_monitor_archive(f)
    f = Filename('SOMETHING' + c.stage_0_file_suffix)
    assert not m.file_is_monitor_archive(f)
    f = Filename('SOMETHING' + c.stage_1_file_suffix)
    assert not m.file_is_monitor_archive(f)
    f = Filename('SOMETHING' + c.stage_2_file_suffix)
    assert not m.file_is_monitor_archive(f)
    f = Filename('SOMETHING' + c.stage_3_file_suffix)
    assert not m.file_is_monitor_archive(f)
    f = Filename('SOMETHING' + c.stage_4_file_suffix)
    assert not m.file_is_monitor_archive(f)
    f = Filename('SOMETHING' + c.stage_5_file_suffix)
    assert not m.file_is_monitor_archive(f)
    f = Filename('SOMETHING' + c.stage_6_file_suffix)
    assert not m.file_is_monitor_archive(f)

def test_file_is_stage_0():
    f = Filename('SOMETHING' + c.monitor_archive_file_extension)
    assert not m.file_is_stage_0(f)
    f = Filename('SOMETHING' + c.stage_0_file_suffix)
    assert m.file_is_stage_0(f)
    f = Filename('SOMETHING' + c.stage_1_file_suffix)
    assert not m.file_is_stage_0(f)
    f = Filename('SOMETHING' + c.stage_2_file_suffix)
    assert not m.file_is_stage_0(f)
    f = Filename('SOMETHING' + c.stage_3_file_suffix)
    assert not m.file_is_stage_0(f)
    f = Filename('SOMETHING' + c.stage_4_file_suffix)
    assert not m.file_is_stage_0(f)
    f = Filename('SOMETHING' + c.stage_5_file_suffix)
    assert not m.file_is_stage_0(f)
    f = Filename('SOMETHING' + c.stage_6_file_suffix)
    assert not m.file_is_stage_0(f)

def test_file_is_stage_1():
    f = Filename('SOMETHING' + c.monitor_archive_file_extension)
    assert not m.file_is_stage_1(f)
    f = Filename('SOMETHING' + c.stage_0_file_suffix)
    assert not m.file_is_stage_1(f)
    f = Filename('SOMETHING' + c.stage_1_file_suffix)
    assert m.file_is_stage_1(f)
    f = Filename('SOMETHING' + c.stage_2_file_suffix)
    assert not m.file_is_stage_1(f)
    f = Filename('SOMETHING' + c.stage_3_file_suffix)
    assert not m.file_is_stage_1(f)
    f = Filename('SOMETHING' + c.stage_4_file_suffix)
    assert not m.file_is_stage_1(f)
    f = Filename('SOMETHING' + c.stage_5_file_suffix)
    assert not m.file_is_stage_1(f)
    f = Filename('SOMETHING' + c.stage_6_file_suffix)
    assert not m.file_is_stage_1(f)

def test_file_is_stage_2():
    f = Filename('SOMETHING' + c.monitor_archive_file_extension)
    assert not m.file_is_stage_2(f)
    f = Filename('SOMETHING' + c.stage_0_file_suffix)
    assert not m.file_is_stage_2(f)
    f = Filename('SOMETHING' + c.stage_1_file_suffix)
    assert not m.file_is_stage_2(f)
    f = Filename('SOMETHING' + c.stage_2_file_suffix)
    assert m.file_is_stage_2(f)
    f = Filename('SOMETHING' + c.stage_3_file_suffix)
    assert not m.file_is_stage_2(f)
    f = Filename('SOMETHING' + c.stage_4_file_suffix)
    assert not m.file_is_stage_2(f)
    f = Filename('SOMETHING' + c.stage_5_file_suffix)
    assert not m.file_is_stage_2(f)
    f = Filename('SOMETHING' + c.stage_6_file_suffix)
    assert not m.file_is_stage_2(f)

def test_map_monitor_archive_filename_to_monitor():
    assert m.map_monitor_archive_filename_to_monitor(filename) == monitor

def test_map_monitor_archive_key_to_monitor():
    k = c.inbox_prefix / filename
    assert m.map_monitor_archive_key_to_monitor(k) == monitor

def test_map_monitor_to_combined_encounter_file():
    n = 'encounter' + c.stage_5_file_suffix
    f = c.intermediate_directory / monitor / n
    assert m.map_monitor_to_combined_encounter_file(monitor) == f

def test_map_monitor_to_monitor_archive_file():
    f = c.inbox_directory / filename
    assert m.map_monitor_to_monitor_archive_file(monitor) == f

def test_map_monitor_to_monitor_directory():
    d = c.intermediate_directory / monitor
    assert m.map_monitor_to_monitor_directory(monitor) == d

def test_map_monitor_to_outbox_keys():
    outbox_keys = m.map_monitor_to_outbox_keys(monitor)
    assert len(outbox_keys) == 2
    assert outbox_keys[0] == (
        c.outbox_prefix / (monitor + c.column_oriented_data_file_extension)
        )
    assert outbox_keys[1] == (
        c.outbox_prefix / (monitor + c.row_oriented_data_file_extension)
        )

def test_map_monitor_to_raw_encounter_file():
    n = 'encounter' + c.stage_3_file_suffix
    f = c.intermediate_directory / monitor / n
    assert m.map_monitor_to_raw_encounter_file(monitor) == f

def test_map_monitor_to_sorted_encounter_file():
    n = 'encounter' + c.stage_4_file_suffix
    f = c.intermediate_directory / monitor / n
    assert m.map_monitor_to_sorted_encounter_file(monitor) == f

def test_map_stage_0_file_to_stage_1_file():
    ardf = (
        c.intermediate_directory / monitor / subpath
        / ('SOMETHING' + c.stage_0_file_suffix)
        )
    edf = (
        c.intermediate_directory / monitor / subpath
        / ('SOMETHING' + c.stage_1_file_suffix)
        )
    assert m.map_stage_0_file_to_stage_1_file(monitor, ardf) == edf

def test_map_stage_0_file_to_stage_2_file():
    ardf = (
        c.intermediate_directory / monitor / subpath
        / ('SOMETHING' + c.stage_0_file_suffix)
        )
    edf = (
        c.intermediate_directory / monitor / subpath
        / ('SOMETHING' + c.stage_2_file_suffix)
        )
    assert m.map_stage_0_file_to_stage_2_file(monitor, ardf) == edf


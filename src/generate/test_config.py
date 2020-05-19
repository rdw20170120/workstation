#!/bin/false

from datetime import timedelta

from .config import Config

c = Config()

def test_allowed_gap():
    v = c.allowed_gap
    assert isinstance(v, timedelta)
    assert v.days == 0
    assert v.seconds > 60

def test_avro_1_Hz_schema_file():
    v = c.avro_1_Hz_schema_file
    assert v is not None
    assert v.is_absolute()
    assert v.is_file()

def test_avro_100_Hz_schema_file():
    v = c.avro_100_Hz_schema_file
    assert v is not None
    assert v.is_absolute()
    assert v.is_file()

def test_avro_extracted_schema_file():
    v = c.avro_extracted_schema_file
    assert v is not None
    assert v.is_absolute()
    assert v.is_file()

def test_avro_sparse_schema_file():
    v = c.avro_sparse_schema_file
    assert v is not None
    assert v.is_absolute()
    assert v.is_file()

def test_bucket_name():
    v = c.bucket_name
    assert v is not None
    assert len(v) > 0

def test_column_oriented_data_file_extension():
    v = c.column_oriented_data_file_extension
    assert v is not None
    assert len(v) > 0

def test_fake_file_extension():
    v = c.fake_file_extension
    assert v is not None
    assert len(v) > 0

def test_inbox_directory():
    v = c.inbox_directory
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()

def test_inbox_prefix():
    v = c.inbox_prefix
    assert v is not None

def test_intermediate_directory():
    v = c.intermediate_directory
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()

def test_intermediate_prefix():
    v = c.intermediate_prefix
    assert v is not None

def test_is_dry_run():
    v = c.is_dry_run
    assert v is not None
    assert (v is True) or (v is False)

def test_is_forced_run():
    v = c.is_forced_run
    assert v is not None
    assert (v is True) or (v is False)

def test_is_safe_to_download_phi():
    v = c.is_safe_to_download_phi
    assert v is not None
    assert (v is True) or (v is False)

def test_list_file_extension():
    v = c.list_file_extension
    assert v is not None
    assert len(v) > 0

def test_log_directory():
    v = c.log_directory
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()

def test_log_file():
    v = c.log_file
    assert v is not None
    assert v.is_absolute()

def test_monitor_archive_file_extension():
    v = c.monitor_archive_file_extension
    assert v is not None
    assert len(v) > 0

def test_outbox_directory():
    v = c.outbox_directory
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()

def test_outbox_prefix():
    v = c.outbox_prefix
    assert v is not None

def test_pid_file():
    v = c.pid_file
    assert v is not None
    assert v.is_absolute()

def test_profile_name():
    v = c.profile_name
    assert v is not None
    assert len(v) > 0

def test_project_directory():
    v = c.project_directory
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()

def test_quick_run_limit():
    v = c.quick_run_limit
    assert isinstance(v, int)
    assert v >= 0

def test_region_name():
    v = c.region_name
    assert v is not None
    assert len(v) > 0

def test_reserved_space_in_bytes():
    v = c.reserved_space_in_bytes
    assert isinstance(v, float) or isinstance(v, int)
    assert v >= 0

def test_row_oriented_data_file_extension():
    v = c.row_oriented_data_file_extension
    assert v is not None
    assert len(v) > 0

def test_should_abort_on_task_failure():
    v = c.should_abort_on_task_failure
    assert v is not None
    assert (v is True) or (v is False)

def test_should_fake_it():
    v = c.should_fake_it
    assert v is not None
    assert (v is True) or (v is False)

def test_stage_0_file_suffix():
    v = c.stage_0_file_suffix
    assert v is not None
    assert len(v) > 0

def test_stage_1_file_suffix():
    v = c.stage_1_file_suffix
    assert v is not None
    assert len(v) > 0

def test_stage_2_file_suffix():
    v = c.stage_2_file_suffix
    assert v is not None
    assert len(v) > 0

def test_stage_3_file_suffix():
    v = c.stage_3_file_suffix
    assert v is not None
    assert len(v) > 0

def test_stage_4_file_suffix():
    v = c.stage_4_file_suffix
    assert v is not None
    assert len(v) > 0

def test_stage_5_file_suffix():
    v = c.stage_5_file_suffix
    assert v is not None
    assert len(v) > 0

def test_stage_6_file_suffix():
    v = c.stage_6_file_suffix
    assert v is not None
    assert len(v) > 0

def test_temporary_directory():
    v = c.temporary_directory
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()


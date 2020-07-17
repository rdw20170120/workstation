#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .config import Config


c = Config()

def test_fake_file_extension():
    v = c.fake_file_extension
    assert v is not None
    assert len(v) > 0

def test_filesystem_to_watch():
    v = c.filesystem_to_watch
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()

def test_is_dry_run():
    v = c.is_dry_run
    assert v is not None
    assert (v is True) or (v is False)

def test_is_forced_run():
    v = c.is_forced_run
    assert v is not None
    assert (v is True) or (v is False)

def test_log_directory():
    v = c.log_directory
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()

def test_log_file():
    v = c.log_file
    assert v is not None
    assert v.is_absolute()

def test_pid_file():
    v = c.pid_file
    assert v is not None
    assert v.is_absolute()

def test_project_directory():
    v = c.project_directory
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()

def test_quick_run_limit():
    v = c.quick_run_limit
    assert isinstance(v, int)
    assert v >= 0

def test_reserved_disk_space_in_bytes():
    v = c.reserved_disk_space_in_bytes
    assert isinstance(v, float) or isinstance(v, int)
    assert v >= 0

def test_should_abort_upon_task_failure():
    v = c.should_abort_upon_task_failure
    assert v is not None
    assert (v is True) or (v is False)

def test_should_fake_it():
    v = c.should_fake_it
    assert v is not None
    assert (v is True) or (v is False)

def test_should_leave_output_upon_task_failure():
    v = c.should_leave_output_upon_task_failure
    assert v is not None
    assert (v is True) or (v is False)

def test_temporary_directory():
    v = c.temporary_directory
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()

'''DisabledContent
'''


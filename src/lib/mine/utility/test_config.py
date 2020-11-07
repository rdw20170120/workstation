#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.config import Config
from utility import my_assert as is_
# Co-located modules (relative references, NOT packaged, in project)


c = Config()

def test_application_name():
    v = c.application_name
    assert is_.equal(v, 'PleaseOverrideMe')

def test_fake_suffix():
    v = c.fake_suffix
    assert is_.greater(len(v), 0)

def test_filesystem_to_watch():
    v = c.filesystem_to_watch
    assert is_.absolute_directory(v)

def test_is_dry_run():
    v = c.is_dry_run
    assert is_.instance(v, bool)

def test_is_forced_run():
    v = c.is_forced_run
    assert is_.instance(v, bool)

def test_log_directory():
    v = c.log_directory
    assert is_.absolute_path(v)
    if v.exists(): assert is_.absolute_directory(v)

def test_log_file():
    v = c.log_file
    assert is_.absolute_path(v)

def test_log_name():
    v = c.log_name
    assert is_.nonempty_string(v)

def test_log_suffix():
    v = c.log_suffix
    assert is_.nonempty_string(v)

def test_pid_file():
    v = c.pid_file
    assert is_.absolute_path(v)

def test_pid_suffix():
    v = c.pid_suffix
    assert is_.nonempty_string(v)

def test_project_directory():
    v = c.project_directory
    assert is_.absolute_directory(v)

def test_quick_run_limit():
    v = c.quick_run_limit
    assert is_.at_least(v, 0)

def test_reserved_disk_space_in_bytes():
    v = c.reserved_disk_space_in_bytes
    assert is_.at_least(v, 0)

def test_should_abort_upon_task_failure():
    v = c.should_abort_upon_task_failure
    assert is_.instance(v, bool)

def test_should_fake_it():
    v = c.should_fake_it
    assert is_.instance(v, bool)

def test_should_leave_output_upon_task_failure():
    v = c.should_leave_output_upon_task_failure
    assert is_.instance(v, bool)

def test_temporary_directory():
    v = c.temporary_directory
    assert is_.absolute_directory(v)

'''DisabledContent
'''


#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.config import Config
from utility.my_assert import assert_absolute_directory
from utility.my_assert import assert_absolute_path
from utility.my_assert import assert_equal
from utility.my_assert import assert_equal_or_greater
from utility.my_assert import assert_greater
from utility.my_assert import assert_instance
# Co-located modules (relative references, NOT packaged, in project)


c = Config()

def test_application_name():
    v = c.application_name
    assert assert_equal(v, 'PleaseOverrideMe')

def test_fake_file_suffix():
    v = c.fake_file_suffix
    assert assert_greater(len(v), 0)

def test_filesystem_to_watch():
    v = c.filesystem_to_watch
    assert assert_absolute_directory(v)

def test_is_dry_run():
    v = c.is_dry_run
    assert assert_instance(v, bool)

def test_is_forced_run():
    v = c.is_forced_run
    assert assert_instance(v, bool)

def test_log_directory():
    v = c.log_directory
    assert assert_absolute_path(v)
    if v.exists(): assert assert_absolute_directory(v)

def test_log_file():
    v = c.log_file
    assert assert_absolute_path(v)

def test_pid_file():
    v = c.pid_file
    assert assert_absolute_path(v)

def test_project_directory():
    v = c.project_directory
    assert assert_absolute_directory(v)

def test_quick_run_limit():
    v = c.quick_run_limit
    assert assert_equal_or_greater(v, 0)

def test_reserved_disk_space_in_bytes():
    v = c.reserved_disk_space_in_bytes
    assert assert_equal_or_greater(v, 0)

def test_should_abort_upon_task_failure():
    v = c.should_abort_upon_task_failure
    assert assert_instance(v, bool)

def test_should_fake_it():
    v = c.should_fake_it
    assert assert_instance(v, bool)

def test_should_leave_output_upon_task_failure():
    v = c.should_leave_output_upon_task_failure
    assert assert_instance(v, bool)

def test_temporary_directory():
    v = c.temporary_directory
    assert assert_absolute_directory(v)

'''DisabledContent
'''


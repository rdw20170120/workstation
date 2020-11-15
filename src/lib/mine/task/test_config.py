#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_
from utility.test_config import *
# Project modules   (relative references, NOT packaged, in project)

def test_fake_suffix(config):
    v = config.fake_suffix
    assert is_.greater(len(v), 0)


def test_filesystem_to_watch(config):
    v = config.filesystem_to_watch
    assert is_.absolute_directory(v)


def test_is_dry_run(config):
    v = config.is_dry_run
    assert is_.instance(v, bool)


def test_is_forced_run(config):
    v = config.is_forced_run
    assert is_.instance(v, bool)


def test_quick_run_limit(config):
    v = config.quick_run_limit
    assert is_.at_least(v, 0)


def test_reserved_disk_space_in_bytes(config):
    v = config.reserved_disk_space_in_bytes
    assert is_.at_least(v, 0)


def test_should_abort_upon_task_failure(config):
    v = config.should_abort_upon_task_failure
    assert is_.instance(v, bool)


def test_should_fake_it(config):
    v = config.should_fake_it
    assert is_.instance(v, bool)


def test_should_leave_output_upon_task_failure(config):
    v = config.should_leave_output_upon_task_failure
    assert is_.instance(v, bool)


"""DisabledContent
"""

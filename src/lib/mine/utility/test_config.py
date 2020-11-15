#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_
# Project modules   (relative references, NOT packaged, in project)

def test_application_name(config):
    v = config.application_name
    assert is_.nonempty_string(v)


def test_log_directory(config):
    v = config.log_directory
    assert is_.absolute_path(v)
    if v.exists():
        assert is_.absolute_directory(v)


def test_log_file(config):
    v = config.log_file
    assert is_.absolute_path(v)


def test_log_name(config):
    v = config.log_name
    assert is_.nonempty_string(v)


def test_log_suffix(config):
    v = config.log_suffix
    assert is_.nonempty_string(v)


def test_pid_file(config):
    v = config.pid_file
    assert is_.absolute_path(v)


def test_pid_suffix(config):
    v = config.pid_suffix
    assert is_.nonempty_string(v)


def test_project_directory(config):
    v = config.project_directory
    assert is_.absolute_directory(v)


def test_temporary_directory(config):
    v = config.temporary_directory
    assert is_.absolute_directory(v)


"""DisabledContent
"""

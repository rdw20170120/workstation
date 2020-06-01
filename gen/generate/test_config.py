#!/bin/false

from .config import Config

c = Config()

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

def test_should_fake_it():
    v = c.should_fake_it
    assert v is not None
    assert (v is True) or (v is False)

def test_temporary_directory():
    v = c.temporary_directory
    assert v is not None
    assert v.is_absolute()
    assert v.is_dir()


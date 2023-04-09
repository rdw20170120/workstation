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
    assert is_.instance(v, str)


def test_config(config):
    assert is_.not_none(config)


def test_log_name(config):
    assert is_.equal(config.log_name, "gen")


def test_trace_maximal(config):
    assert is_.equal(config.trace_maximal, "DEEP")


def test_var_capture_directory(config):
    assert is_.equal(config.var_capture_directory, "BO_DirCapture")


def test_var_logging_directory(config):
    assert is_.equal(config.var_logging_directory, "BO_DirLog")


def test_var_operating_system(config):
    assert is_.equal(config.var_operating_system, "BO_OS")


def test_var_output_directory(config):
    assert is_.equal(config.var_output_directory, "BO_DirOut")


def test_var_project_path(config):
    assert is_.equal(config.var_project_path, "BO_PathProject")


def test_var_system_path(config):
    assert is_.equal(config.var_system_path, "BO_PathSystem")


def test_var_tool_path(config):
    assert is_.equal(config.var_tool_path, "BO_PathTool")


def test_var_user_path(config):
    assert is_.equal(config.var_user_path, "BO_PathUser")


"""DisabledContent
"""

#!/usr/bin/env false
"""Manage configuration."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import environment
from utility.tracked_path import TrackedPath

# Project modules   (relative references, NOT packaged, in project)


class Config(object):
    @property
    def application_name(self):
        return environment.get(self.var_application_name)

    @property
    def log_directory(self):
        return TrackedPath("logging", environment.get(self.var_logging_directory))

    @property
    def log_file(self):
        return self.log_directory / (self.log_name + self.log_suffix)

    @property
    def log_name(self):
        return "app"

    @property
    def log_suffix(self):
        return ".log"

    @property
    def pid_file(self):
        return self.project_directory / (self.application_name + self.pid_suffix)

    @property
    def pid_suffix(self):
        return ".pid"

    @property
    def project_directory(self):
        return TrackedPath("project", environment.get(self.var_project_directory))

    @property
    def running_humanless(self):
        try:
            environment.get(self.var_running_humanless)
            return True
        except KeyError:
            return False

    @property
    def temporary_directory(self):
        return TrackedPath("temporary", environment.get(self.var_temporary_directory))

    @property
    def trace_minimal(self):
        return "TRACE"

    @property
    def var_application_name(self):
        return "%sNameApp" % self.variable_prefix

    @property
    def var_logging_directory(self):
        return "%sDirLog" % self.variable_prefix

    @property
    def var_project_directory(self):
        return "%sProject" % self.variable_prefix

    @property
    def var_running_humanless(self):
        return "%sRunningHumanless" % self.variable_prefix

    @property
    def var_temporary_directory(self):
        return "%sDirTemp" % self.variable_prefix

    @property
    def var_trace(self):
        return "%sTrace" % self.variable_prefix

    @property
    def variable_prefix(self):
        return "BO_"


"""DisabledContent
"""

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
        return environment.get("BO_NameApp")

    @property
    def log_directory(self):
        return self.project_directory / "log"

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
        return self.project_directory / (
            self.application_name + self.pid_suffix
        )

    @property
    def pid_suffix(self):
        return ".pid"

    @property
    def project_directory(self):
        return TrackedPath("project", environment.get("BO_Project"))

    @property
    def temporary_directory(self):
        return TrackedPath("temporary", environment.get("TMPDIR"))


"""DisabledContent
"""

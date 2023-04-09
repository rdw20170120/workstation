#!/usr/bin/env false
"""Configure application."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility.config import Config as BaseConfig

# Project modules   (relative references, NOT packaged, in project)


class Config(BaseConfig):
    @property
    def log_name(self):
        return "gen"

    @property
    def trace_maximal(self):
        return "DEEP"

    @property
    def var_capture_directory(self):
        return "%sDirCapture" % self.variable_prefix

    @property
    def var_logging_directory(self):
        return "%sDirLog" % self.variable_prefix

    @property
    def var_operating_system(self):
        return "%sOS" % self.variable_prefix

    @property
    def var_output_directory(self):
        return "%sDirOut" % self.variable_prefix

    @property
    def var_project_path(self):
        return "%sPathProject" % self.variable_prefix

    @property
    def var_system_path(self):
        return "%sPathSystem" % self.variable_prefix

    @property
    def var_tool_path(self):
        return "%sPathTool" % self.variable_prefix

    @property
    def var_user_path(self):
        return "%sPathUser" % self.variable_prefix


"""DisabledContent
"""

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

"""DisabledContent
"""

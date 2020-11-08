#!/usr/bin/env false
"""Configure application."""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.config import Config as BaseConfig
# Co-located modules (relative references, NOT packaged, in project)


class Config(BaseConfig):
    @property
    def should_abort_upon_task_failure(self):
        # TODO: Enhance to override via environment variable and CLI argument
        # TODO: Overriding BaseConfig, should remove for production
        return False
 
    @property
    def should_leave_output_upon_task_failure(self):
        # TODO: Enhance to override via environment variable and CLI argument
        # TODO: Overriding BaseConfig, should remove for production
        return False
 
    @property
    def application_name(self):
        return 'MODULE'

'''DisabledContent
'''


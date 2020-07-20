#!/usr/bin/env false
"""Manage configuration."""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
from sys     import maxsize
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.config import Config as BaseConfig
# Co-located modules (relative references, NOT packaged, in project)


class Config(BaseConfig):
    @property
    def application_name(self):
        return 'generate'


'''DisabledContent
'''


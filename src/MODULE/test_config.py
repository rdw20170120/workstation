#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .config import Config


def test_application_name():
    v = Config().application_name
    assert isinstance(v, str)
    assert v != 'PleaseOverrideMe'

def test_config():
    assert Config() is not None

'''DisabledContent
'''


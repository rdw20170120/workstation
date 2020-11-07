#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility import my_assert as is_
# Co-located modules (relative references, NOT packaged, in project)
from .config import Config


c = Config()

def test_application_name():
    v = c.application_name
    assert is_.instance(v, str)
    assert is_.not_equal(v, 'PleaseOverrideMe')

def test_config():
    assert is_.not_none(c)

'''DisabledContent
'''


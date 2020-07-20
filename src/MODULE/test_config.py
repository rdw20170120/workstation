#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .config import Config


c = Config()

def test_application_name():
    v = c.application_name
    assert isinstance(v, str)
    assert v != 'PleaseOverrideMe'

'''DisabledContent
'''


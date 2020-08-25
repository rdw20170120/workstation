#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.my_assert import assert_instance
from utility.my_assert import assert_not_equal
from utility.my_assert import assert_not_none
# Co-located modules (relative references, NOT packaged, in project)
from .config import Config


def test_application_name():
    v = Config().application_name
    assert assert_instance(v, str)
    assert assert_not_equal(v, 'PleaseOverrideMe')

def test_config():
    assert assert_not_none(Config())

'''DisabledContent
'''


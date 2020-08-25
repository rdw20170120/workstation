#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from . import s3


def test_01():
    with raises(ValueError, match='profile_name'):
        s3.S3(None)

def test_02():
    with raises(ValueError, match='profile_name'):
        s3.S3('')

'''DisabledContent
'''


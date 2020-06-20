#!/usr/bin/env false
"""
"""
from pytest import raises

from . import s3

def test_01():
    with raises(ValueError, match='profile_name'):
        s3.S3(None)

def test_02():
    with raises(ValueError, match='profile_name'):
        s3.S3('')

'''DisabledContent
'''


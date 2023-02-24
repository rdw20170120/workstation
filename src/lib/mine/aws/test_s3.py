#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules    (absolute references, NOT packaged, in project)
from aws import s3

# Co-located modules (relative references, NOT packaged, in project)


def test_00():
    with raises(ValueError, match="profile_name"):
        s3.S3(None)


def test_01():
    with raises(ValueError, match="profile_name"):
        s3.S3("")


"""DisabledContent
"""

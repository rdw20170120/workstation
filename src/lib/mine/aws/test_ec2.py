#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises
# Library modules    (absolute references, NOT packaged, in project)
from aws import ec2
# Co-located modules (relative references, NOT packaged, in project)


def test_01():
    with raises(ValueError, match='profile_name'):
        ec2.EC2(None)

def test_02():
    with raises(ValueError, match='profile_name'):
        ec2.EC2('')

'''DisabledContent
'''


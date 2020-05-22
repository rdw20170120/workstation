#!/bin/false

from pytest import raises

from . import ec2

def test_01():
    with raises(ValueError, match='profile_name'):
        ec2.EC2(None)

def test_02():
    with raises(ValueError, match='profile_name'):
        ec2.EC2('')


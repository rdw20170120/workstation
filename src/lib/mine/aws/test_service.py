#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules    (absolute references, NOT packaged, in project)
from aws import service

# Co-located modules (relative references, NOT packaged, in project)


def test_init_rejects_service_name_of_none():
    with raises(ValueError, match="service_name"):
        service.AwsService(None, None)


def test_init_rejects_service_name_of_empty():
    with raises(ValueError, match="service_name"):
        service.AwsService("", None)


def test_init_rejects_profile_name_of_none():
    with raises(ValueError, match="profile_name"):
        service.AwsService("RESOURCE", None)


def test_init_rejects_profile_name_of_empty():
    with raises(ValueError, match="profile_name"):
        service.AwsService("RESOURCE", "")


"""DisabledContent
"""

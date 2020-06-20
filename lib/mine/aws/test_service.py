#!/usr/bin/env false
"""
"""
from pytest import raises

from . import service

def test_init_rejects_service_name_of_none():
    with raises(ValueError, match='service_name'):
        service.AwsService(None, None)

def test_init_rejects_service_name_of_empty():
    with raises(ValueError, match='service_name'):
        service.AwsService('', None)

def test_init_rejects_profile_name_of_none():
    with raises(ValueError, match='profile_name'):
        service.AwsService('RESOURCE', None)

def test_init_rejects_profile_name_of_empty():
    with raises(ValueError, match='profile_name'):
        service.AwsService('RESOURCE', '')

'''DisabledContent
'''


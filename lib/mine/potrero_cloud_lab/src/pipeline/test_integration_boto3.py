#!/bin/false

from botocore.exceptions import UnknownServiceError
from pytest              import raises

from .aws.ec2     import EC2
from .aws.s3      import S3
from .aws.service import AwsService
from .config      import Config

c = Config()

def test_service_session_rejects_service_unknown():
    with raises(UnknownServiceError):
        AwsService('RESOURCE', c.profile_name)

def test_service_session_accepts_service_ec2():
    assert AwsService('ec2', c.profile_name) is not None

def test_service_session_accepts_service_s3():
    assert AwsService('s3', c.profile_name) is not None

def test_ec2_session():
    assert EC2(c.profile_name) is not None

def test_s3_session():
    assert S3(c.profile_name) is not None


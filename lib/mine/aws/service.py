#!/usr/bin/env false
"""
"""
from boto3   import Session
from logzero import logger as log


class AwsService:
    def __init__(self, service_name, profile_name, region_name=None):
        if not service_name:
            raise ValueError("'service_name' has invalid value '{}'".format(service_name))
        self._service_name = service_name

        if not profile_name:
            raise ValueError("'profile_name' has invalid value '{}'".format(profile_name))
        self._profile_name = profile_name

        if region_name is None:
            self._region_name = AwsService.default_region()
        else:
            self._region_name = region_name

        log.debug(
            "Creating AWS session for profile '%s' and region '%s'",
            self._profile_name, self._region_name
            )
        self._session = Session(
            profile_name=profile_name, region_name=region_name
            )
        self._client = self._session.client(self._service_name)

    @property
    def client(self):
        return self._client

    @staticmethod
    def default_region():
        return 'us-east-1'

    @property
    def profile_name(self):
        return self._profile_name

    @staticmethod
    def region_is_enabled(region):
        return (region['OptInStatus'] != 'not-opted-in')

    @property
    def region_name(self):
        return self._region_name

    @property
    def service_name(self):
        return self._service_name

    @property
    def session(self):
        return self._session

'''DisabledContent
'''


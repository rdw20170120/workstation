#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from   botocore.exceptions import ClientError
from   logzero             import logger as log
import boto3
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .service import AwsService


class EC2(AwsService):
    def __init__(self, profile_name, region_name=None):
        super().__init__('ec2', profile_name, region_name)

    def _describe_availability_zones(self):
        result = []
        try:
            result = self.client.describe_availability_zones()['AvailabilityZones']
        except ClientError as e:
            if 'AccessDenied' in str(e):
                log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name, self.region_name, self.service_name,
                    'describe_availability_zones', e
                    )
            else: raise
        return result

    def _describe_regions(self, all=True):
        result = []
        try:
            result = self.client.describe_regions(AllRegions=all)['Regions']
        except ClientError as e:
            if 'AccessDenied' in str(e):
                log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name, self.region_name, self.service_name,
                    'describe_regions', e
                    )
            else: raise
        return result

    def get_all_regions(self):
        log.debug("Attempting to get all regions")
        result = self._describe_regions()
        log.debug("All regions: %r", result)
        return result

    def get_availability_zones(self):
        log.debug(
            "Attempting to get availability zones for region '%s'",
            self.region_name
            )
        result = self._describe_availability_zones()
        log.debug("Region '%s' has availability zones: %r", self.region_name, result)
        return result

'''DisabledContent
'''


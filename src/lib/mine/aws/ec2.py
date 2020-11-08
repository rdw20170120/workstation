#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from logging import getLogger

# External packages  (absolute references, NOT distributed with Python)
from botocore.exceptions import ClientError
import boto3

# Library modules    (absolute references, NOT packaged, in project)
from aws.service import AwsService

# Co-located modules (relative references, NOT packaged, in project)


class EC2(AwsService):
    def __init__(self, profile_name, region_name=None):
        self._log = getLogger(self.__class__.__name__)
        super().__init__("ec2", profile_name, region_name)

    def _describe_availability_zones(self):
        result = []
        try:
            result = self.client.describe_availability_zones()[
                "AvailabilityZones"
            ]
        except ClientError as e:
            if "AccessDenied" in str(e):
                self._log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name,
                    self.region_name,
                    self.service_name,
                    "describe_availability_zones",
                    e,
                )
            raise
        return result

    def _describe_regions(self, all=True):
        result = []
        try:
            result = self.client.describe_regions(AllRegions=all)["Regions"]
        except ClientError as e:
            if "AccessDenied" in str(e):
                self._log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name,
                    self.region_name,
                    self.service_name,
                    "describe_regions",
                    e,
                )
            raise
        return result

    def get_all_regions(self):
        self._log.debug("Attempting to get all regions")
        result = self._describe_regions()
        self._log.debug("All regions: %r", result)
        return result

    def get_availability_zones(self):
        self._log.debug(
            "Attempting to get availability zones for region '%s'",
            self.region_name,
        )
        result = self._describe_availability_zones()
        self._log.debug(
            "Region '%s' has availability zones: %r", self.region_name, result
        )
        return result


"""DisabledContent
"""

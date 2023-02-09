#!/usr/bin/env false
"""TODO: Write

TODO: Switch from os.path to pathlib.Path
"""
# Internal packages  (absolute references, distributed with Python)
from logging import getLogger
from os import path

# External packages  (absolute references, NOT distributed with Python)
from botocore.exceptions import ClientError
import boto3

# Library modules    (absolute references, NOT packaged, in project)
from aws.service import AwsService
from utility import my_assert as is_
from utility.text import string_without_prefix

# Co-located modules (relative references, NOT packaged, in project)


class S3(AwsService):
    def __init__(self, profile_name, region_name=None):
        self._log = getLogger(self.__class__.__name__)
        super().__init__("s3", profile_name, region_name)

    def _download_object(self, bucket_name, key, file_path):
        try:
            self.client.download_file(bucket_name, key, file_path)
        except ClientError as e:
            if "AccessDenied" in str(e):
                self._log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name,
                    self.region_name,
                    self.service_name,
                    "download_file",
                    e,
                )
            raise

    def _list_bucket_common_prefixes(self, bucket_name):
        result = None
        try:
            paginator = self.client.get_paginator("list_objects_v2")
            pager = paginator.paginate(Bucket=bucket_name, Delimiter="/")
            result = pager.search("CommonPrefixes")
        except ClientError as e:
            if "AccessDenied" in str(e):
                self._log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name,
                    self.region_name,
                    self.service_name,
                    "list_objects_v2",
                    e,
                )
            raise
        return result

    def _list_bucket_objects(self, bucket_name, prefix):
        result = None
        try:
            paginator = self.client.get_paginator("list_objects_v2")
            pager = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
            result = pager.search("Contents")
        except ClientError as e:
            if "AccessDenied" in str(e):
                self._log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name,
                    self.region_name,
                    self.service_name,
                    "list_objects_v2",
                    e,
                )
            raise
        return result

    def _upload_object(self, bucket_name, key, file_path):
        try:
            self.client.upload_file(file_path, bucket_name, key)
        except ClientError as e:
            if "AccessDenied" in str(e):
                self._log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name,
                    self.region_name,
                    self.service_name,
                    "upload_file",
                    e,
                )
            raise

    def download_object(self, bucket_name, key, file_path):
        assert is_.instance(bucket_name, str)
        assert is_.instance(key, str)
        assert is_.instance(file_path, str)
        self._log.debug(
            "Downloading key '%s' in bucket '%s' to file '%s'",
            key,
            bucket_name,
            file_path,
        )
        self._download_object(bucket_name, key, file_path)

    def get_bucket_prefixes(self, bucket_name):
        assert is_.instance(bucket_name, str)
        result = []
        self._log.debug("Getting common prefixes for bucket '%s'", bucket_name)
        for prefix in self._list_bucket_common_prefixes(bucket_name):
            if prefix is not None:
                result.append(prefix.get("Prefix"))
            else:
                self._log.debug("Found None")
        self._log.debug("Bucket '%s' has common prefixes: %r", bucket_name, result)
        return result

    def list_bucket_objects(self, bucket_name, prefix):
        assert is_.instance(bucket_name, str)
        assert is_.instance(prefix, str)
        result = []
        self._log.debug(
            "Listing objects in bucket '%s' with prefix '%s'",
            bucket_name,
            prefix,
        )
        for obj in self._list_bucket_objects(bucket_name, prefix):
            if obj is None:
                self._log.debug("Found None")
            else:
                self._log.debug("Bucket '%s' has object: %r", bucket_name, obj)
                result.append(obj)
        return result

    def upload_object(self, bucket_name, key, file_path):
        assert is_.instance(bucket_name, str)
        assert is_.instance(key, str)
        assert is_.instance(file_path, str)
        self._log.debug(
            "Uploading file '%s' to key '%s' in bucket '%s'",
            file_path,
            key,
            bucket_name,
        )
        self._upload_object(bucket_name, key, file_path)


"""DisabledContent
"""

#!/bin/false

from os import path

import boto3

from botocore.exceptions import ClientError
from logzero             import logger as log

from utility.text import string_without_prefix

from .service import AwsService


class S3(AwsService):
    def __init__(self, profile_name, region_name=None):
        super().__init__('s3', profile_name, region_name)

    def _download_object(self, bucket_name, key, file_path):
        try:
            self.client.download_file(bucket_name, key, file_path)
        except ClientError as e:
            if 'AccessDenied' in str(e):
                log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name, self.region_name, self.service_name,
                    'download_file', e
                    )
            else: raise

    def _list_bucket_common_prefixes(self, bucket_name):
        result = None
        try:
            paginator = self.client.get_paginator('list_objects_v2')
            pager = paginator.paginate(Bucket=bucket_name, Delimiter='/')
            result = pager.search('CommonPrefixes')
        except ClientError as e:
            if 'AccessDenied' in str(e):
                log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name, self.region_name, self.service_name,
                    'list_objects_v2', e
                    )
            else: raise
        return result

    def _list_bucket_objects(self, bucket_name, prefix):
        result = None
        try:
            paginator = self.client.get_paginator('list_objects_v2')
            pager = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
            result = pager.search('Contents')
        except ClientError as e:
            if 'AccessDenied' in str(e):
                log.warn(
                    "Profile '%s', region '%s', service '%s' failed to '%s': %s",
                    self.profile_name, self.region_name, self.service_name,
                    'list_objects_v2', e
                    )
            else: raise
        return result

    def download_object(self, bucket_name, key, file_path):
        assert isinstance(bucket_name, str)
        assert isinstance(key, str)
        assert isinstance(file_path, str)
        log.debug(
            "Attempting to download object from bucket '%s' with key '%s' to file '%s'",
            bucket_name, key, file_path
            )
        self._download_object(bucket_name, key, file_path)

    def get_bucket_prefixes(self, bucket_name):
        assert isinstance(bucket_name, str)
        result = []
        log.debug(
            "Attempting to get common prefixes for bucket '%s'",
            bucket_name
            )
        for prefix in self._list_bucket_common_prefixes(bucket_name):
            if prefix is not None: result.append(prefix.get('Prefix'))
            else: log.debug("Found None")
        log.debug("Bucket '%s' has common prefixes: %r", bucket_name, result)
        return result

    def list_bucket_objects(self, bucket_name, prefix):
        assert isinstance(bucket_name, str)
        assert isinstance(prefix, str)
        result = []
        log.debug(
            "Attempting to list objects in bucket '%s' with prefix '%s'",
            bucket_name, prefix
            )
        for obj in self._list_bucket_objects(bucket_name, prefix):
            if obj is None: log.debug("Found None")
            else:
                log.debug("Bucket '%s' has object: %r", bucket_name, obj)
                key = obj['Key']
                p, filename = path.split(obj['Key'])
                assert p == prefix
                if len(filename) > 0: result.append(obj)
        return result


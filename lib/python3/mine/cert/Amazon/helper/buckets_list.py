#!/usr/bin/env python

import boto3
import sys

from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError
from botocore.exceptions import ProfileNotFound


def list_buckets(s3_client):
    try:
        print "Listing buckets"
        response = s3_client.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        print("Bucket List: %s" % buckets)
    except ClientError as e:
        print "FATAL: ClientError: {0}".format(e)
    except NoCredentialsError as e:
        print "FATAL: NoCredentialsError: {0}".format(e)


def list_common_prefixes(s3_client, bucket):
    try:
        print "Listing common prefixes for bucket '{0}'".format(bucket)
        paginator = s3_client.get_paginator('list_objects')
        result = paginator.paginate(Bucket=bucket, Delimiter='/')
        for prefix in result.search('CommonPrefixes'):
            print(prefix.get('Prefix'))
    except ClientError as e:
        print "FATAL: ClientError: {0}".format(e)
    except NoCredentialsError as e:
        print "FATAL: NoCredentialsError: {0}".format(e)


def main():
    try:
        session = boto3.Session()
        s3 = session.client('s3')
        list_buckets(s3)
        list_common_prefixes(s3, 'couchbase-cert-preprod')
    except ProfileNotFound as e:
        print "FATAL: ProfileNotFound: {0}, verify environment variable AWS_PROFILE".format(e)


if __name__ == '__main__':
    sys.exit(main())


""" Disabled content
"""


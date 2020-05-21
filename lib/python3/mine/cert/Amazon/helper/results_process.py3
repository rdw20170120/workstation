#!/usr/bin/env python

import boto3
import logging
import os
import sys

from botocore.exceptions import ProfileNotFound


LOG = logging.getLogger('results_process')


def configure_logging():
    # TODO: Ensure time is emitted in UTC
    logging.basicConfig(
        datefmt='%Y%m%dT%H%M%S',
        format='%(asctime)s.%(msecs)dZ %(process)5d %(levelname)5s %(name)s %(message)s',
        level=logging.DEBUG
        )
    logging.addLevelName(logging.CRITICAL, 'FATAL')
    logging.addLevelName(logging.NOTSET, 'NONE')
    logging.addLevelName(logging.WARNING, 'WARN')


def results_process(s3, bucket_name):
    LOG.info("Processing exam results in bucket '%s'", bucket_name)
    bucket = s3.Bucket(bucket_name)
    for o in bucket.objects.all():
        LOG.debug("Found S3 object: '%s'", o.key)


def session_report(session):
    LOG.info('Available profiles: %s', session.available_profiles)
    LOG.info('Available regions: %s', session.get_available_regions('s3'))
    LOG.info('Available resources: %s', session.get_available_resources())
    LOG.info('Available services: %s', session.get_available_services())
    LOG.info('Profile name: %s', session.profile_name)
    LOG.info('Region name: %s', session.region_name)


def main():
    try:
        configure_logging()
        logging.getLogger('botocore').setLevel(logging.INFO)

        LOG.debug("main() try = began")
        bucket_name = os.environ['CB_S3_Bucket_Result']
        session = boto3.session.Session()
        session_report(session)
        s3 = session.resource('s3')
        results_process(s3, bucket_name)
    except KeyError as e:
        LOG.error("main() except = failure")
        LOG.exception(e)
        sys.exit(1)
    except ProfileNotFound as e:
        LOG.error("main() except = failure")
        LOG.exception(e)
        sys.exit(2)
    except BaseException as e:
        LOG.error("main() except = failure")
        LOG.exception(e)
        sys.exit(3)
    else:
        LOG.debug("main() else = success")
        sys.exit(0)
    finally:
        LOG.debug("main() finally = ended")


if __name__ == '__main__':
    main()


""" Disabled content
"""


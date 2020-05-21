"""
    This module contains phase processing specific to rev115.
"""

import logging
import os

from utility import valid_md5, extract_file, delete_directory
from status import Status


LOG = logging.getLogger('processor_rev115')
CB_SESSION_FILENAME = '/CB_session.rand'


def common(info, extract=True):
    """Method that performs processing common to most phases."""
    file_path = info.file_path

    if not os.path.exists(file_path):
        LOG.error("Unable to process missing file: %s", file_path)
        return Status.MISSING_FILE

    if info.file_size == 0:
        LOG.error("Unable to process empty file: %s", file_path)
        return Status.EMPTY_FILE

    if not valid_md5(file_path):
        LOG.error("MD5 validation failed for file: %s", file_path)
        return Status.MD5_INVALID

    status = Status.IN_PROGRESS

    # extract tar ball if requested
    if extract:
        LOG.debug("Extracting file: " + file_path)
        target = extract_file(file_path)
        if target is None:
            return Status.EXTRACT_FAIL
        try:
            with open(target + CB_SESSION_FILENAME, 'r') as session_file:
                info.session_id = session_file.read().rstrip()
                info.target_dir = target
        except IOError:
            status = Status.CONTENT_FAIL

    return status


def process_initialize(info):
    """Supports processing of the INITIALIZE phase."""
    status = common(info)
    if status is not Status.IN_PROGRESS:
        return status

    # Phase specific processing goes here

    delete_directory(info.target_dir)

    return Status.SUCCESS


def process_began(info):
    """Supports processing of the BEGAN phase"""
    status = common(info)
    if status is not Status.IN_PROGRESS:
        return status

    # Phase specific processing goes here

    delete_directory(info.target_dir)

    return Status.SUCCESS

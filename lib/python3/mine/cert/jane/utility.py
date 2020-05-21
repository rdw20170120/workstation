"""
    Utility functions used in phase processing.
"""

from datetime import datetime
import hashlib
import logging
import os
import re
import shutil
import tarfile
import tempfile
from phase import Phase


FILE_PATTERN = ".*cert-(rev\\d{3})-(.{4})-(CX\\d{3})-(\\d{8}T\\d{6}Z)-(\\w+).tb2$"


def get_phase_info(file_path):
    """Returns file info extracted from the filename"""
    parts = get_filename_parts(file_path)
    if parts is not None:
        phase_name = parts.phase_name
        if phase_name not in Phase.names():
            raise ValueError("Invalid phase: " + phase_name)

        return type('PhaseInfo', (object,),
                    {'file_path':  file_path,
                     'file_size':  os.path.getsize(file_path),
                     'received':   None,
                     'revision':   parts.revision,
                     'session_id': None,
                     'exam_id':    parts.exam_id,
                     'timestamp':  parts.timestamp,
                     'phase':      Phase[parts.phase_name],
                     'status':     None,
                     'target_dir': None})()


def get_filename_parts(file_path):
    """Simple function to extract info from parts of the filename."""
    match = re.compile(FILE_PATTERN).match(file_path)
    if match is not None:
        parts = match.groups()
        return type('FileInfo', (object,),
                    {'revision':   parts[0],
                     'exam_id':    parts[2],
                     'timestamp':  convert_timestamp(parts[3]),
                     'phase_name': parts[4]})()


def get_regex():
    """Simple function to return standard regex for matching filenames."""

    return FILE_PATTERN


def valid_md5(file_path):
    """Simple function to validate file using MD5"""
    try:
        with open(file_path, 'rb') as tar_file:
            digest1 = hashlib.md5(tar_file.read()).hexdigest()
        with open(file_path + '.md5', 'rb') as md5_file:
            digest2 = md5_file.read().rstrip()[-32:]
        return digest1 == digest2
    except Exception:
        return False


def configure_logging():
    """Configure logging for this module"""
    logging.basicConfig(
        datefmt='%Y%m%dT%H%M%S',
        format='%(asctime)s.%(msecs)dZ PID=%(process)-5d %(levelname)-5s %(message)s',
        level=logging.INFO)
    logging.addLevelName(logging.CRITICAL, 'FATAL')
    logging.addLevelName(logging.NOTSET, 'NONE')
    logging.addLevelName(logging.WARNING, 'WARN')


def extract_file(file_path):
    """Extract specified tarball into temporary directory."""
    target = tempfile.mkdtemp()
    with tarfile.open(file_path, "r:*") as source:
        source.extractall(target)
    return target


def delete_directory(dir_path):
    """Delete specified directory and swallow any exceptions."""
    if dir_path is None:
        return False

    try:
        shutil.rmtree(dir_path)
        return True
    except OSError:
        return False


def get_base_filename(file_path):
    """Returns base filename"""
    return os.path.basename(file_path)


def convert_timestamp(timestamp):
    """Converts a string to a datetime object"""
    return datetime.strptime(timestamp, "%Y%m%dT%H%M%SZ")

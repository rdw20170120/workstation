"""
    Simple enum that represents the status of exam processing.
"""

from enum import Enum


# pylint: disable=too-few-public-methods
class Status(Enum):
    """Simple enum that represents all of the valid exam statuses."""

    IN_PROGRESS = 1
    PHASE_IGNORED = 2
    MD5_INVALID = 3
    MISSING_FILE = 4
    EMPTY_FILE = 5
    EXTRACT_FAIL = 6
    CONTENT_FAIL = 7
    DUPLICATE_SESSION = 8
    CODE_FAIL = 9
    SUCCESS = 10

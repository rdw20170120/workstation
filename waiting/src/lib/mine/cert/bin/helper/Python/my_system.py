import os
import re

from datetime import datetime
from my_assert import has_type
from my_assert import has_type_message
from my_time import timestamp_as_datetime_utc
from types import BooleanType
from types import FloatType
from types import ListType
from types import StringType


def create_directory(pathname):
    assert has_type(pathname, StringType), has_type_message(
        pathname, StringType
    )
    os.makedirs(pathname)


def directory_exists(pathname):
    assert has_type(pathname, StringType), has_type_message(
        pathname, StringType
    )
    result = os.path.isdir(pathname)
    assert has_type(result, BooleanType), has_type_message(result, BooleanType)
    return result


def file_exists(filename):
    assert has_type(filename, StringType), has_type_message(
        filename, StringType
    )
    result = os.path.isfile(filename)
    assert has_type(result, BooleanType), has_type_message(result, BooleanType)
    return result


def file_is_empty(filename):
    assert has_type(filename, StringType), has_type_message(
        filename, StringType
    )
    result = (
        (os.path.getsize(filename) > 0) if file_exists(filename) else False
    )
    assert has_type(result, BooleanType), has_type_message(result, BooleanType)
    return result


def get_current_directory():
    return os.getcwd()


def get_empty_files(directory, pattern):
    assert has_type(directory, StringType), has_type_message(
        directory, StringType
    )
    assert has_type(pattern, StringType), has_type_message(pattern, StringType)
    compiled = re.compile(pattern)
    result = []
    result = [
        f
        for f in os.listdir(directory)
        if compiled.match(f) and file_is_empty(f)
    ]
    assert has_type(result, ListType), has_type_message(result, ListType)
    return result


def get_file_contents(pathname):
    assert has_type(pathname, StringType), has_type_message(
        pathname, StringType
    )
    with open(pathname, "r") as f:
        result = f.read()
    assert has_type(result, StringType), has_type_message(result, StringType)
    return result


def get_files(directory, pattern):
    assert has_type(directory, StringType), has_type_message(
        directory, StringType
    )
    assert has_type(pattern, StringType), has_type_message(pattern, StringType)
    result = []
    assert has_type(result, ListType), has_type_message(result, ListType)
    return result


def get_file_modified_time(pathname):
    """Return Unix epoch for when pathname was last modified"""
    assert has_type(pathname, StringType), has_type_message(
        pathname, StringType
    )
    result = os.path.getmtime(pathname)
    assert has_type(result, FloatType), has_type_message(result, FloatType)
    result = timestamp_as_datetime_utc(result)
    assert has_type(result, datetime), has_type_message(result, datetime)
    return result


def get_uptime_from_proc():
    with open("/proc/uptime", "r") as f:
        line = f.readline()
        result = float(line.split()[0])
    assert has_type(result, FloatType), has_type_message(result, FloatType)
    return result


def maybe_create_directory(pathname):
    assert has_type(pathname, StringType), has_type_message(
        pathname, StringType
    )
    if not directory_exists(pathname):
        create_directory(pathname)


def path_exists(pathname):
    assert has_type(pathname, StringType), has_type_message(
        pathname, StringType
    )
    result = os.path.exists(pathname)
    assert has_type(result, BooleanType), has_type_message(result, BooleanType)
    return result


def set_file_contents(pathname, contents):
    assert has_type(pathname, StringType), has_type_message(
        pathname, StringType
    )
    assert has_type(contents, StringType), has_type_message(
        contents, StringType
    )
    with open(pathname, "w") as f:
        f.write(contents)


""" Disabled content
"""

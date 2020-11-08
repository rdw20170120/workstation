from datetime import datetime
import os
import re
import shutil

# from types import BooleanType
# from types import FloatType
# from types import ListType
# from types import StringType

from .my_assert import has_type
from .my_assert import has_type_message
from .my_time import timestamp_as_datetime_utc


def clone_files(source_directory, target_directory):
    assert directory_exists(source_directory), directory_exists_message(
        source_directory
    )
    assert directory_exists(target_directory), directory_exists_message(
        target_directory
    )
    assert FALSE, "TODO: Implement"


def create_directory(path_name):
    # assert has_type(path_name, StringType), has_type_message(path_name, StringType)
    os.makedirs(path_name)


def delete_directory(path_name):
    # assert has_type(path_name, StringType), has_type_message(path_name, StringType)
    shutil.rmtree(path_name)


def directory_exists(path_name):
    # assert has_type(path_name, StringType), has_type_message(path_name, StringType)
    result = os.path.isdir(path_name)
    # assert has_type(result, BooleanType), has_type_message(result, BooleanType)
    return result


def directory_exists_message(directory):
    return "Expected directory '{0}' to exist, but it does NOT".format(
        directory
    )


def file_exists(file_name):
    # assert has_type(file_name, StringType), has_type_message(file_name, StringType)
    result = os.path.isfile(file_name)
    # assert has_type(result, BooleanType), has_type_message(result, BooleanType)
    return result


def file_is_empty(file_name):
    # assert has_type(file_name, StringType), has_type_message(file_name, StringType)
    result = (
        (os.path.getsize(file_name) > 0) if file_exists(file_name) else False
    )
    # assert has_type(result, BooleanType), has_type_message(result, BooleanType)
    return result


def get_current_directory():
    return os.getcwd()


def get_empty_files(directory, pattern):
    # assert has_type(directory, StringType), has_type_message(directory, StringType)
    # assert has_type(pattern, StringType), has_type_message(pattern, StringType)
    compiled = re.compile(pattern)
    result = []
    result = [
        f
        for f in os.listdir(directory)
        if compiled.match(f) and file_is_empty(f)
    ]
    # assert has_type(result, ListType), has_type_message(result, ListType)
    return result


def get_file_contents(path_name):
    # assert has_type(path_name, StringType), has_type_message(path_name, StringType)
    with open(path_name, "r") as f:
        result = f.read()
    # assert has_type(result, StringType), has_type_message(result, StringType)
    return result


def get_files(directory, pattern):
    # assert has_type(directory, StringType), has_type_message(directory, StringType)
    # assert has_type(pattern, StringType), has_type_message(pattern, StringType)
    result = []
    # assert has_type(result, ListType), has_type_message(result, ListType)
    return result


def get_file_modified_time(path_name):
    """Return Unix epoch for when path_name was last modified"""
    # assert has_type(path_name, StringType), has_type_message(path_name, StringType)
    result = os.path.getmtime(path_name)
    # assert has_type(result, FloatType), has_type_message(result, FloatType)
    result = timestamp_as_datetime_utc(result)
    # assert has_type(result, datetime), has_type_message(result, datetime)
    return result


def get_uptime_from_proc():
    with open("/proc/uptime", "r") as f:
        line = f.readline()
        result = float(line.split()[0])
    # assert has_type(result, FloatType), has_type_message(result, FloatType)
    return result


def maybe_create_directory(path_name):
    if not directory_exists(path_name):
        create_directory(path_name)


def maybe_delete_directory(path_name):
    if directory_exists(path_name):
        delete_directory(path_name)


def path_exists(path_name):
    # assert has_type(path_name, StringType), has_type_message(path_name, StringType)
    result = os.path.exists(path_name)
    # assert has_type(result, BooleanType), has_type_message(result, BooleanType)
    return result


def recreate_directory(path_name):
    maybe_delete_directory(path_name)
    create_directory(path_name)


def set_file_contents(path_name, contents):
    # assert has_type(path_name, StringType), has_type_message(path_name, StringType)
    # assert has_type(contents, StringType), has_type_message(contents, StringType)
    with open(path_name, "w") as f:
        f.write(contents)


""" Disabled content
"""

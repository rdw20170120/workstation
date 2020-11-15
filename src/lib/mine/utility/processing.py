#!/usr/bin/env false
"""TODO: Write

TODO: REVIEW: this module against its siblings.
"""
# Internal packages (absolute references, distributed with Python)
from os import getpid as os_get_pid

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility.filesystem import delete_file
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


def create_pid_file(pid_file):
    pid = get_pid()
    if pid_file.is_file():
        stored = read_pid_file(pid_file)
        if stored != pid:
            m = "PID file '{}' contains '{}' instead of current process id '{}', "
            m += "perhaps application is already running"
            raise RuntimeError(m.format(pid_file, stored, pid))
    write_pid_file(pid_file, pid)
    stored = read_pid_file(pid_file)
    assert is_.equal(stored, pid)


def delete_pid_file(pid_file):
    if pid_file.is_file():
        pid = get_pid()
        stored = read_pid_file(pid_file)
        if stored == pid:
            delete_file(pid_file)
        else:
            m = "PID file '{}' contains '{}' instead of current process id '{}', "
            m += "apparently PID file is corrupt"
            raise RuntimeError(m.format(pid_file, stored, pid))
    else:
        raise RuntimeError("Missing PID file '{}'".format(pid_file))


def get_pid():
    return os_get_pid()


def read_pid_file(pid_file):
    result = 0
    try:
        content = pid_file.read_text()
        result = int(content)
    except ValueError as e:
        raise RuntimeError(
            "PID file '{}' does not contain a valid process id: {}".format(
                pid_file, content
            )
        ) from e
    return result


def write_pid_file(pid_file, pid):
    pid_file.write_text(str(pid))


"""DisabledContent
"""

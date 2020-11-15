import psutil

from datetime import datetime
from types import FloatType
from my_assert import has_type
from my_assert import has_type_message
from my_time import now
from subprocess import PIPE
from my_time import timestamp_as_datetime_utc


def get_connected_sessions():
    return psutil.users()


def get_uptime():
    """Return system uptime in seconds."""
    bootTimestamp = psutil.boot_time()
    bootDateTime = timestamp_as_datetime_utc(bootTimestamp)
    result = now() - bootDateTime
    result = result.total_seconds()
    assert has_type(result, FloatType), has_type_message(result, FloatType)
    return result


def process_is_running(pid):
    return (
        psutil.Process(pid).is_running() if psutil.pid_exists(pid) else False
    )


def report_process(pid=None):
    p = psutil.Process(pid)
    print(("Reporting process pid {0}:".format(pid)))
    with p.oneshot():
        print(("cmdline: {0}".format(p.cmdline())))
        print(
            (
                "create_time: {0}".format(
                    timestamp_as_datetime_utc(p.create_time())
                )
            )
        )
        print(("cwd: {0}".format(p.cwd())))
        print(("exe: {0}".format(p.exe())))
        print(("hash: {0}".format(hash(p))))
        print(("is_running: {0}".format(p.is_running())))
        print(("num_threads: {0}".format(p.num_threads())))
        print(("pid: {0}".format(p.pid)))
        print(("ppid: {0}".format(p.ppid())))
        print(("status: {0}".format(p.status())))
        print(("terminal: {0}".format(p.terminal())))
        print(("username: {0}".format(p.username())))
        print(("cpu_percent: {0}".format(p.cpu_percent())))
        print(("cpu_times: {0}".format(p.cpu_times())))
        print(("gids: {0}".format(p.gids())))
        print(("uids: {0}".format(p.uids())))


""" Disabled content
    if psutil.pid_exists(pid):
        return psutil.Process(pid).is_running()
    else:
        return False
"""

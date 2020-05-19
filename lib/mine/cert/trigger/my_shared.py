import os

from datetime import datetime
from my_system import file_exists
from my_system import get_file_contents
from my_system import get_file_modified_time
from logging import getLogger
from my_assert import has_type
from my_assert import has_type_message
from my_time import now
from my_system import path_exists
from subprocess import PIPE
from psutil import Popen
from my_psutil import process_is_running
from my_system import set_file_contents
from types import StringType


LOG = getLogger('my_shared')

PROCESS_STATUS_DEAD = 'DEAD'
PROCESS_STATUS_FAILURE = 'FAILURE'
PROCESS_STATUS_RUNNING = 'RUNNING'
PROCESS_STATUS_SUCCESS = 'SUCCESS'
PROCESS_STATUS_UNSTARTED = 'UNSTARTED'


def _requireFileNotExists(pathname):
    assert has_type(pathname, StringType), has_type_message(pathname, StringType)
    if path_exists(pathname):  raise RuntimeError(
        "File '{0}' should NOT exist at this time".format(pathname)
    )

def get_base_directory(exam_id):
    assert has_type(exam_id, StringType), has_type_message(exam_id, StringType)
    return os.path.join('/tmp', '.CB', exam_id)

def get_command_filename(name, exam_id):
    assert has_type(name, StringType), has_type_message(name, StringType)
    assert has_type(exam_id, StringType), has_type_message(exam_id, StringType)
    return os.path.join(get_process_directory(exam_id), "{0}.cmd".format(name))

def get_download_directory():
    return os.path.join(os.environ['HOME'], '.CB', 'download')

def get_exit_filename(name, exam_id):
    assert has_type(name, StringType), has_type_message(name, StringType)
    assert has_type(exam_id, StringType), has_type_message(exam_id, StringType)
    return os.path.join(get_process_directory(exam_id), "{0}.exit".format(name))

def get_pid_filename(name, exam_id):
    assert has_type(name, StringType), has_type_message(name, StringType)
    assert has_type(exam_id, StringType), has_type_message(exam_id, StringType)
    return os.path.join(get_process_directory(exam_id), "{0}.pid".format(name))

def get_process_directory(exam_id):
    assert has_type(exam_id, StringType), has_type_message(exam_id, StringType)
    return os.path.join(get_base_directory(exam_id))

def get_process_status(file_exit, file_pid):
    assert has_type(file_exit, StringType), has_type_message(file_exit, StringType)
    assert has_type(file_pid, StringType), has_type_message(file_pid, StringType)
    result, as_of = None, now()
    exists_exit = file_exists(file_exit)
    LOG.debug("File exists '%s' = %s", file_exit, exists_exit)
    exists_pid = file_exists(file_pid)
    LOG.debug("File exists '%s' = %s", file_pid, exists_pid)
    if exists_exit:
        as_of = get_file_modified_time(file_exit)
        status = int(get_file_contents(file_exit))
        if status == 0:
            result = PROCESS_STATUS_SUCCESS
        else:
            result = PROCESS_STATUS_FAILURE
    else:
        if exists_pid:
            as_of = get_file_modified_time(file_pid)
            pid = int(get_file_contents(file_pid))
            if process_is_running(pid):
                result = PROCESS_STATUS_RUNNING
            else:
                result = PROCESS_STATUS_DEAD
        else:
            result = PROCESS_STATUS_UNSTARTED
    assert has_type(as_of, datetime), has_type_message(as_of, datetime)
    assert has_type(result, StringType), has_type_message(result, StringType)
    LOG.debug("Process status %s", result)
    return result, as_of

def get_script_filename(name, exam_id):
    assert has_type(name, StringType), has_type_message(name, StringType)
    assert has_type(exam_id, StringType), has_type_message(exam_id, StringType)
    return os.path.join(get_download_directory(), "{0}.bash".format(name))

def get_stderr_filename(name, exam_id):
    assert has_type(name, StringType), has_type_message(name, StringType)
    assert has_type(exam_id, StringType), has_type_message(exam_id, StringType)
    return os.path.join(get_process_directory(exam_id), "{0}.err".format(name))

def get_stdout_filename(name, exam_id):
    assert has_type(name, StringType), has_type_message(name, StringType)
    assert has_type(exam_id, StringType), has_type_message(exam_id, StringType)
    return os.path.join(get_process_directory(exam_id), "{0}.out".format(name))

def run_command(command, file_exit, file_pid, file_err, file_out, file_cmd):
    assert has_type(command, StringType), has_type_message(command, StringType)
    assert has_type(file_exit, StringType), has_type_message(file_exit, StringType)
    assert has_type(file_pid, StringType), has_type_message(file_pid, StringType)
    assert has_type(file_err, StringType), has_type_message(file_err, StringType)
    assert has_type(file_out, StringType), has_type_message(file_out, StringType)
    assert has_type(file_cmd, StringType), has_type_message(file_cmd, StringType)
    LOG.debug("file_cmd  = '%s'", file_cmd)
    LOG.debug("file_err  = '%s'", file_err)
    LOG.debug("file_exit = '%s'", file_exit)
    LOG.debug("file_out  = '%s'", file_out)
    LOG.debug("file_pid  = '%s'", file_pid)
    try:
        _requireFileNotExists(file_cmd)
        _requireFileNotExists(file_err)
        _requireFileNotExists(file_exit)
        _requireFileNotExists(file_out)
        _requireFileNotExists(file_pid)
        LOG.info("Starting subprocess with command: %s", command)
        with Popen(
            command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True
            ) as p:
            LOG.debug("pid= '%d'", p.pid)
            set_file_contents(file_cmd, command)
            set_file_contents(file_pid, str(p.pid))
            p.wait()
            set_file_contents(file_err, p.stderr.read())
            set_file_contents(file_out, p.stdout.read())
            set_file_contents(file_exit, str(p.returncode))
            if p.returncode == 0:
                LOG.info("Subprocess exited with success: %d", p.returncode)
            else:
                LOG.warning("Subprocess exited with failure: %d", p.returncode)
    except RuntimeError as e:
        raise RuntimeError("Aborting execution of command:\n{0}".format(command), e)


""" Disabled content
def run_url(url, file_script, file_exit, file_pid, file_err, file_out, file_cmd):
    LOG.debug("file_script  = '%s'", file_script)
    command = "curl -fLsS --output {0} {1}".format(file_script, url)
    command += " ; {0}".format(file_script)
    run_command(command, file_exit, file_pid, file_err, file_out, file_cmd)

def run_url_maybe(
    name, exam_id, threshold_minutes, uptime_in_minutes, url, file_script, file_exit, file_pid
):
    if uptime_in_minutes >= threshold_minutes:
        LOG.info(
            "It is time to run '%s' process, since uptime is %d minutes >= %d",
            name, uptime_in_minutes, threshold_minutes
            )
        sessions = get_connected_sessions()
        if sessions:
            if environment == ENV_PROD:
                raise EnvironmentError(
                    1,
                    "Aborting since there are connected user sessions:\n{0}".format(sessions)
                    )
            else:
                LOG.warning("There are connected user sessions:\n%s", sessions)
        LOG.info("Start the '%s' process", name)
        file_cmd = get_command_filename(name, exam_id)
        file_err = get_stderr_filename(name, exam_id)
        file_out = get_stdout_filename(name, exam_id)
        run_url(url, file_script, file_exit, file_pid, file_err, file_out, file_cmd)
    else:
        LOG.debug(
            "Not yet time to run '%s' process, since uptime is only %d minutes < %d",
            name, uptime_in_minutes, threshold_minutes
            )
"""


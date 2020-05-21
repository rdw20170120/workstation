"""
    This module contains the main entry point for phase processing.
"""

import importlib
import logging
import time
from repository import DuplicateError
from status import Status
from utility import get_phase_info, delete_directory


LOG = logging.getLogger('processor')
DEFAULT_REVISION = 'rev115'


def process(repo, file_path):
    """Method creates an instance of revision specific subclass and
    dispatches to the appropriate method to process the phase."""
    LOG.info("Processing started for file: " + file_path)

    info = get_phase_info(file_path)
    revision = info.revision
    phase_name = info.phase.name

    module_name = 'processor_' + revision
    mod = load_module(module_name)
    if mod is None:
        module_name = 'processor_' + DEFAULT_REVISION
        mod = load_module(module_name)
        if mod is None:
            raise ValueError('Unable to load module {} for {}'.format(module_name,
                                                                      file_path))
    LOG.debug('Using module %s to process file: %s', module_name, file_path)

    info.received = int(time.time())

    info.status = Status.PHASE_IGNORED if info.phase.ignored else Status.IN_PROGRESS

    try:
        repo.create(info)
    except DuplicateError:
        LOG.error('Ignored duplicate file: %s', file_path)
        return

    if info.phase.ignored():
        return

    phase_func = get_function(mod, 'process_' + phase_name)

    if phase_func is None:
        LOG.warning('Unsupported phase for file: %s', file_path)
        # default to common processing
        status = invoke_common(mod, info)
        info.status = Status.SUCCESS if status is Status.IN_PROGRESS else status
    else:
        # invoke phase specific processing
        info.status = phase_func(info)

    info.processed = int(time.time())

    try:
        repo.update(info)
    except DuplicateError:
        LOG.error('Duplicate session ID for file: %s', file_path)
        info.status = Status.DUPLICATE_SESSION
        repo.update(info, exclude_session=True)

    LOG.info("Processing completed for file: " + info.file_path)


def load_module(module_name):
    """Simple function to load a revision specific processor module."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def get_function(mod, func_name):
    """Simple function that returns the named function for the specified module"""
    try:
        return mod.__getattribute__(func_name)
    except AttributeError:
        return None


def invoke_common(mod, info):
    """Simple function that returns the common function for the specified module"""
    common_func = get_function(mod, 'common')
    if common_func is None:
        return Status.CODE_FAIL

    status = common_func(info)
    delete_directory(info.target_dir)

    return status

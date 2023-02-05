#!/usr/bin/env false
"""Application for TODO.

Intended to be executed as a Python module:  python3 -m ${BO_NameApp}
"""
# Internal packages (absolute references, distributed with Python)
from argparse import ArgumentParser
from logging import DEBUG, INFO, WARN, ERROR, FATAL
from logging import getLogger
import sys

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from task.task_manager import TaskManager
from utility import my_logging
from utility.singleton_application import SingletonApplication
from utility.text import generate

# Project modules   (relative references, NOT packaged, in project)
from .config import Config
from .task.bootstrap import Bootstrap
from .task.mapping import Mapping


c = Config()


def _apply_verbosity(verbosity=0):
    background = [
        getLogger("utility"),
    ]
    if verbosity <= 3:
        my_logging.set_log_level(background, FATAL)
    elif verbosity == 4:
        my_logging.set_log_level(background, FATAL)
    elif verbosity == 5:
        my_logging.set_log_level(background, ERROR)
    elif verbosity == 6:
        my_logging.set_log_level(background, WARN)
    elif verbosity == 7:
        my_logging.set_log_level(background, INFO)
    else:
        my_logging.set_log_level(background, DEBUG)


def _application_configuration():
    content = [
        "Application configuration:\n",
        {"application_name": c.application_name},
        "\n",
        {"fake_suffix": c.fake_suffix},
        "\n",
        {"filesystem_to_watch": c.filesystem_to_watch},
        "\n",
        {"is_dry_run": c.is_dry_run},
        "\n",
        {"is_forced_run": c.is_forced_run},
        "\n",
        {"log_directory": c.log_directory},
        "\n",
        {"log_file": c.log_file},
        "\n",
        {"log_name": c.log_name},
        "\n",
        {"log_suffix": c.log_suffix},
        "\n",
        {"pid_file": c.pid_file},
        "\n",
        {"pid_suffix": c.pid_suffix},
        "\n",
        {"project_directory": c.project_directory},
        "\n",
        {"quick_run_limit": c.quick_run_limit},
        "\n",
        {"reserved_disk_space_in_bytes": c.reserved_disk_space_in_bytes},
        "\n",
        {"should_abort_upon_task_failure": c.should_abort_upon_task_failure},
        "\n",
        {"should_fake_it": c.should_fake_it},
        "\n",
        {
            "should_leave_output_upon_task_failure": c.should_leave_output_upon_task_failure
        },
        "\n",
        {"temporary_directory": c.temporary_directory},
        "\n",
    ]
    return content


def _character_encoding_configuration():
    content = [
        "Character encoding configuration:\n",
        {"sys.getdefaultencoding()": sys.getdefaultencoding()},
        "\n",
        {"sys.getfilesystemencoding()": sys.getfilesystemencoding()},
        "\n",
        {"sys.stderr.encoding": sys.stderr.encoding},
        "\n",
        {"sys.stdin.encoding": sys.stdin.encoding},
        "\n",
        {"sys.stdout.encoding": sys.stdout.encoding},
        "\n",
    ]
    return content


def _configuration():
    content = [
        "Reporting configuration...\n",
        _character_encoding_configuration(),
        my_logging.configuration(),
        _application_configuration(),
    ]
    return content


def _parse_args():
    # TODO: Add dry run
    # TODO: Add fake run?
    # TODO: Add forced run
    # TODO: Add quick run
    # TODO: Configure for environments (dev, stg, prd, etc.)
    parser = ArgumentParser(
        description="Do something useful",
        prog="python3 -m " + c.application_name,
    )
    parser.add_argument(
        "--configuration",
        help="report configuration and exit",
        action="store_true",
    )
    parser.add_argument(
        "-v",
        dest="verbosity",
        help="increase logging verbosity (repeatable)",
        action="count",
        default=0,
    )
    return parser.parse_args()


def run():
    my_logging.configure(c)
    args = _parse_args()
    my_logging.apply_verbosity(args.verbosity)
    _apply_verbosity(args.verbosity)
    if args.configuration:
        print(generate(_configuration()))
    else:
        MyApp(c.pid_file).run()


class MyApp(SingletonApplication):
    def __init__(self, pid_file):
        super().__init__(getLogger(self.__class__.__name__), pid_file)

    def _run(self):
        self._log.info("Running application...")
        tm = TaskManager(c, Mapping())
        Bootstrap(tm)
        tm.run()


"""DisabledContent
"""

#!/usr/bin/env false
"""Generate source for this project.

Intended to be executed as a Python module:  python3 -m generate
"""
# Internal packages (absolute references, distributed with Python)
from argparse import ArgumentParser
from logging import DEBUG, INFO, WARN, ERROR, FATAL
from logging import getLogger
from pathlib import Path
import sys

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_logging
from utility.filesystem import recreate_directory
from utility.singleton_application import SingletonApplication

# Project modules   (relative references, NOT packaged, in project)
from .config import Config
from .custom.all import generate as generate_all_custom
from .shared.all import generate as generate_all_shared


c = Config()


class MyApp(SingletonApplication):
    def __init__(self, pid_file, target_directory):
        self._target_directory = target_directory
        super().__init__(getLogger(self.__class__.__name__), pid_file)

    def _run(self):
        self._log.info(
            "Generating content into directory '%s'", self._target_directory
        )
        recreate_directory(self._target_directory)
        generate_all_custom(self._target_directory)
        generate_all_shared(self._target_directory)


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


def _parse_args():
    # TODO: Add dry run
    # TODO: Add fake run?
    # TODO: Add forced run
    # TODO: Add quick run
    # TODO: Configure for environments (dev, stg, prd, etc.)
    parser = ArgumentParser(
        description="Generate source for various project files",
        prog="python3 -m " + c.application_name,
    )
    parser.add_argument(
        "target_directory", help="into which to generate output"
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


def _report_configuration():
    print("Reporting configuration...")
    _report_character_encoding_configuration()
    my_logging.report_configuration()
    # TODO: Report application configuration


def _report_character_encoding_configuration():
    # TODO: Add to application configuration
    print("Character encoding configuration:")
    print(("sys.getdefaultencoding()='%s'", sys.getdefaultencoding()))
    print(("sys.getfilesystemencoding()='%s'", sys.getfilesystemencoding()))
    print(("sys.stderr.encoding='%s'", sys.stderr.encoding))
    print(("sys.stdin.encoding='%s'", sys.stdin.encoding))
    print(("sys.stdout.encoding='%s'", sys.stdout.encoding))


def run():
    my_logging.configure(c)
    args = _parse_args()
    my_logging.apply_verbosity(args.verbosity)
    _apply_verbosity(args.verbosity)
    if args.configuration:
        _report_configuration()
    else:
        MyApp(c.pid_file, Path(args.target_directory)).run()


"""DisabledContent
"""

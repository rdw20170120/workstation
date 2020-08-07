#!/usr/bin/env false
"""Application for TODO.

Intended to be executed as a Python module:  python3 -m MODULE
"""
# Internal packages  (absolute references, distributed with Python)
from   argparse import ArgumentParser
from   logging  import getLogger
from   logging  import DEBUG, INFO, WARN, ERROR, FATAL
import sys
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from task.task_manager             import TaskManager
from utility                       import my_logging
from utility.singleton_application import SingletonApplication
# Co-located modules (relative references, NOT packaged, in project)
from .config         import Config
from .task.bootstrap import Bootstrap


c = Config()


class MyApp(SingletonApplication):
    def __init__(self, pid_file):
        super().__init__(getLogger(self.__class__.__name__), pid_file)

    def _run(self):
        self._log.info("Running application...")
        tm = TaskManager(c)
        Bootstrap(tm)
        tm.run()


def _apply_verbosity(verbosity=0):
    # Reference loggers for supporting code
    utility_logger = getLogger('utility')

    # Adjust logging from supporting code
    if verbosity <= 3:
        utility_logger.setLevel(FATAL)
    elif verbosity == 4:
        utility_logger.setLevel(FATAL)
    elif verbosity == 4:
        utility_logger.setLevel(FATAL)
    elif verbosity == 5:
        utility_logger.setLevel(ERROR)
    elif verbosity == 6:
        utility_logger.setLevel(WARN)
    elif verbosity == 7:
        utility_logger.setLevel(INFO)
    else:
        utility_logger.setLevel(DEBUG)

def _parse_args():
    # TODO: Add dry run
    # TODO: Add fake run?
    # TODO: Add forced run
    # TODO: Add quick run
    # TODO: Configure for environments (dev, stg, prd, etc.)
    parser = ArgumentParser(
        description="Do something useful",
        prog="python3 -m " + c.application_name
        )
    parser.add_argument(
        "--configuration",
        help="report configuration and exit",
        action="store_true"
        )
    parser.add_argument(
        "-v", dest="verbosity",
        help="increase logging verbosity (repeatable)",
        action="count", default=0,
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
    print("sys.getdefaultencoding()='%s'", sys.getdefaultencoding())
    print("sys.getfilesystemencoding()='%s'", sys.getfilesystemencoding())
    print("sys.stderr.encoding='%s'", sys.stderr.encoding)
    print("sys.stdin.encoding='%s'", sys.stdin.encoding)
    print("sys.stdout.encoding='%s'", sys.stdout.encoding)

def run():
    my_logging.configure(c)
    args = _parse_args()
    my_logging.apply_verbosity(args.verbosity)
    _apply_verbosity(args.verbosity)
    if args.configuration:
        _report_configuration()
    else:
        MyApp(c.pid_file).run()

'''DisabledContent
'''


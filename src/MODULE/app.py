#!/usr/bin/env false
"""Application for TODO.

Intended to be executed as a Python module:  python3 -m MODULE
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from   argparse import ArgumentParser
from   logging  import getLogger
import sys
# Library modules    (absolute references, NOT packaged, in project)
from task.task_manager             import TaskManager
from utility                       import my_logging
from utility.singleton_application import SingletonApplication
# Co-located modules (relative references, NOT packaged, in project)
from .config         import Config
from .task.bootstrap import Bootstrap


c = Config()
log = getLogger(__name__)


class MyApp(SingletonApplication):
    def __init__(self, pid_file):
        super().__init__(pid_file)

    def _run(self):
        super()._run()
        log.info("Running application...")
        tm = TaskManager(c)
        Bootstrap(tm)
        tm.run()


def _parse_args():
    parser = ArgumentParser(
        description="Process Potrero Accuryn monitor data through pipeline",
        prog="python3 -m " + c.application_name
        )
    parser.add_argument(
        "--configuration",
        help="report configuration and exit",
        action="store_true"
        )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0,
        help="increase logging verbosity (repeatable)"
        )
    return parser.parse_args()

def _report_configuration():
    print("Reporting configuration...")
    _report_character_encoding_configuration()
    my_logging.report_configuration()

def _report_character_encoding_configuration():
    print("Character encoding configuration:")
    print("sys.getdefaultencoding()='%s'", sys.getdefaultencoding())
    print("sys.getfilesystemencoding()='%s'", sys.getfilesystemencoding())
    print("sys.stderr.encoding='%s'", sys.stderr.encoding)
    print("sys.stdin.encoding='%s'", sys.stdin.encoding)
    print("sys.stdout.encoding='%s'", sys.stdout.encoding)

def run():
    my_logging.configure(c)
    args = _parse_args()
    if args.configuration:
        _report_configuration()
    else:
        my_logging.apply_verbose(args.verbose)
        MyApp(c.pid_file).run()

'''DisabledContent
'''


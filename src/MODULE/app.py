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
        self._log.info("Starting data processing pipeline...")
        tm = TaskManager(c)
        Bootstrap(tm)
        tm.run()


def _apply_verbosity(verbosity=0):
    # Reference loggers for supporting code
    avro_logger = getLogger('avro')
    aws_logger = getLogger('aws')
    botocore_logger = getLogger('botocore')
    s3transfer_logger = getLogger('s3transfer')
    urllib3_logger = getLogger('urllib3')
    utility_logger = getLogger('utility')

    # Adjust logging from supporting code
    if verbosity <= 3:
        avro_logger.setLevel(FATAL)
        aws_logger.setLevel(FATAL)
        botocore_logger.setLevel(FATAL)
        s3transfer_logger.setLevel(FATAL)
        urllib3_logger.setLevel(FATAL)
        utility_logger.setLevel(FATAL)
    elif verbosity == 4:
        avro_logger.setLevel(FATAL)
        aws_logger.setLevel(ERROR)
        botocore_logger.setLevel(FATAL)
        s3transfer_logger.setLevel(FATAL)
        urllib3_logger.setLevel(FATAL)
        utility_logger.setLevel(FATAL)
    elif verbosity == 4:
        avro_logger.setLevel(FATAL)
        aws_logger.setLevel(WARN)
        botocore_logger.setLevel(FATAL)
        s3transfer_logger.setLevel(FATAL)
        urllib3_logger.setLevel(FATAL)
        utility_logger.setLevel(FATAL)
    elif verbosity == 5:
        avro_logger.setLevel(ERROR)
        aws_logger.setLevel(INFO)
        botocore_logger.setLevel(ERROR)
        s3transfer_logger.setLevel(ERROR)
        urllib3_logger.setLevel(ERROR)
        utility_logger.setLevel(ERROR)
    elif verbosity == 6:
        avro_logger.setLevel(WARN)
        aws_logger.setLevel(DEBUG)
        botocore_logger.setLevel(WARN)
        s3transfer_logger.setLevel(WARN)
        urllib3_logger.setLevel(WARN)
        utility_logger.setLevel(WARN)
    elif verbosity == 7:
        avro_logger.setLevel(INFO)
        aws_logger.setLevel(DEBUG)
        botocore_logger.setLevel(INFO)
        s3transfer_logger.setLevel(INFO)
        urllib3_logger.setLevel(INFO)
        utility_logger.setLevel(INFO)
    else:
        avro_logger.setLevel(DEBUG)
        aws_logger.setLevel(DEBUG)
        botocore_logger.setLevel(DEBUG)
        s3transfer_logger.setLevel(DEBUG)
        urllib3_logger.setLevel(DEBUG)
        utility_logger.setLevel(DEBUG)


def _parse_args():
    # TODO: Add dry run
    # TODO: Add fake run?
    # TODO: Add forced run
    # TODO: Add quick run
    # TODO: Configure for environments (dev, stg, prd, etc.)
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


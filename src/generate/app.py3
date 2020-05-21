#!/bin/false
# Intended to be executed as a Python module: python3 -m MODULE

from argparse import ArgumentParser
from logging  import DEBUG

from logzero import logger as log
from logzero import loglevel

from build.helper.Python.my_system                     import recreate_directory
from .config                                           import Config
from potrero_cloud_lab.src.pipeline.utility.processing import create_pid_file
from potrero_cloud_lab.src.pipeline.utility.processing import delete_pid_file
from potrero_cloud_lab.src.pipeline.utility.processing import get_pid

loglevel(level=DEBUG)
c = Config()

class ContentGeneratorApp:
    def __init__(self):
        pass

    def _generate(self, target_directory):
        log.info("Generating scripts into directory '%s'", target_directory)
        recreate_directory(target_directory)

    def _parse_args(self):
        parser = ArgumentParser()
        parser.add_argument(
            'target_directory', help='into which to generate output'
            )
        return parser.parse_args()

    def _shutdown(self):
        delete_pid_file(c.pid_file)

    def _startup(self):
        create_pid_file(c.pid_file)

    def run(self):
        try:
            self._startup()
            args = self._parse_args()
            self._generate(args.target_directory)
        finally:
            self._shutdown()

def run():
    try:
        log.info("Began ContentGeneratorApp process with pid '%d'", get_pid())
        ContentGeneratorApp().run()
    except RuntimeError as e:
        log.error(str(e))
        log.fatal("Aborted ContentGeneratorApp process")
    except Exception as e:
        log.exception(e)
        log.fatal("Aborted ContentGeneratorApp process")
    finally:
        log.info("Ended ContentGeneratorApp process with pid '%d'", get_pid())


"""Disabled content
"""

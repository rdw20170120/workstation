#!/bin/false
# Intended to be executed as a Python module:  python3 -m MODULE

from logging import DEBUG
from pathlib import Path

from logzero import logfile
from logzero import logger as log
from logzero import loglevel

from utility.singleton_application import SingletonApplication

from .config import Config

c = Config()
c.log_directory.mkdir(exist_ok=True)
logfile(c.log_file, maxBytes=1e6, backupCount=9)
loglevel(level=DEBUG)


class MyApp(SingletonApplication):
    def __init__(self, pid_file):
        super().__init__(pid_file)

    def _run(self):
        super()._run()
        log.info("Running application...")


def run():
    MyApp(Config().pid_file).run()


''' Disabled content
'''


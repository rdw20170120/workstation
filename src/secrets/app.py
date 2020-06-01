#!/bin/false
# Intended to be executed as a Python module:  python3 -m MODULE

from logging  import DEBUG
from pathlib  import Path

from logzero import logger as log
from logzero import loglevel

from .config                        import Config
from .utility.singleton_application import SingletonApplication


loglevel(level=DEBUG)


class SampleApp(SingletonApplication):
    def __init__(self, pid_file):
        super().__init__(pid_file)

    def _run(self):
        super()._run()
        log.info("Managing secrets...")


def run():
    SampleApp(Config().pid_file).run()


''' Disabled content
'''


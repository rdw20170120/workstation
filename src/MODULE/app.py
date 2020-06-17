#!/usr/bin/env false
"""Application for TODO.

Intended to be executed as a Python module:  python3 -m MODULE
"""
from logzero import logger as log

from utility.singleton_application import SingletonApplication

from .config             import Config
from .task.task_manager  import TaskManager
from .utility.my_logging import configure as configure_logging


class MyApp(SingletonApplication):
    def __init__(self, pid_file):
        super().__init__(pid_file)

    def _run(self):
        super()._run()
        log.info("Running application...")
        TaskManager().run()


def run():
    c = Config()
    configure_logging(c)
    MyApp(c.pid_file).run()

'''DisabledContent
'''


#!/usr/bin/env false
"""Application for TODO.

Intended to be executed as a Python module:  python3 -m MODULE
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from logzero import logger as log
# Library modules    (absolute references, NOT packaged, in project)
from task.task_manager             import TaskManager
from utility.my_logging            import configure as configure_logging
from utility.singleton_application import SingletonApplication
# Co-located modules (relative references, NOT packaged, in project)
from .config         import Config
from .task.bootstrap import Bootstrap


c = Config()


class MyApp(SingletonApplication):
    def __init__(self, pid_file):
        super().__init__(pid_file)

    def _run(self):
        super()._run()
        log.info("Running application...")
        tm = TaskManager(c)
        Bootstrap(tm)
        tm.run()


def run():
    configure_logging(c)
    MyApp(c.pid_file).run()

'''DisabledContent
'''


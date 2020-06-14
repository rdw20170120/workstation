#!/usr/bin/env false
"""

Intended to be executed as a Python module:  python3 -m MODULE
"""

import logging

from logzero        import logfile
from logzero        import logger as log
from logzero        import loglevel
from logzero.colors import Fore as Foreground

from utility.singleton_application import SingletonApplication

from .config            import Config
from .task.task_manager import TaskManager


c = Config()


class MyApp(SingletonApplication):
    def __init__(self, pid_file):
        super().__init__(pid_file)

    def _run(self):
        super()._run()
        log.info("Running application...")
        TaskManager().run()


def _configure_logging():
    # TODO: Adjust logging between dev & prd
    logfile(
        c.log_file, backupCount=9, maxBytes=1e6, 
        disableStderrLogger=False,
        loglevel=logging.DEBUG
    )

def run():
    c.log_directory.mkdir(exist_ok=True)
    _configure_logging()
    MyApp(Config().pid_file).run()

'''DisabledContent
for logzero.LogFormatter._colors
    DEFAULT_COLORS = {
        logging.DEBUG: Foreground.CYAN,
        logging.INFO: Foreground.GREEN,
        logging.WARNING: Foreground.YELLOW,
        logging.ERROR: Foreground.RED
    }

logzero.colors.Fore:
BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
WHITE = 37
RESET = 39
LIGHTBLACK_EX = 90
LIGHTRED_EX = 91
LIGHTGREEN_EX = 92
LIGHTYELLOW_EX = 93
LIGHTBLUE_EX = 94
LIGHTMAGENTA_EX = 95
LIGHTCYAN_EX = 96
LIGHTWHITE_EX = 97
'''


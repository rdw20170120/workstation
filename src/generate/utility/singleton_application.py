#!/bin/false

from pathlib import Path

from logzero import logger as log

from .my_processing import create_pid_file
from .my_processing import delete_pid_file
from .my_processing import get_pid


class SingletonApplication(object):
    def __init__(self, pid_file):
        super().__init__()
        assert isinstance(pid_file, Path)
        self._pid_file = pid_file

    def _run(self):
        """This method should be overridden in a subclass."""
        pass

    def _shutdown(self):
        delete_pid_file(self._pid_file)

    def _startup(self):
        create_pid_file(self._pid_file)

    def run(self):
        try:
            log.info("Began process with pid '%d'", get_pid())
            self._startup()
            self._run()
        except RuntimeError as e:
            log.error(str(e))
            log.fatal("Aborted process")
        except Exception as e:
            log.exception(e)
            log.fatal("Aborted process")
        finally:
            log.info("Ended process with pid '%d'", get_pid())
            self._shutdown()


''' Disabled content
'''

#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
from logzero import logger as log
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .processing import create_pid_file
from .processing import delete_pid_file
from .processing import get_pid


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

'''DisabledContent
'''


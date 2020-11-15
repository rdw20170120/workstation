#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility.my_logging import log_exception
from utility.processing import create_pid_file
from utility.processing import delete_pid_file
from utility.processing import get_pid

# Project modules   (relative references, NOT packaged, in project)


class SingletonApplication(object):
    def __init__(self, logger, pid_file):
        self._log = logger
        self._pid_file = pid_file
        super().__init__()

    def _run(self):
        raise NotImplementedError("_run() MUST be overridden in subclasses")

    def _shutdown(self):
        delete_pid_file(self._pid_file)

    def _startup(self):
        create_pid_file(self._pid_file)

    def run(self):
        pid = get_pid()
        try:
            self._log.info("Began process with pid '%d'", pid)
            self._startup()
            self._run()
        except KeyboardInterrupt as e:
            self._log.debug("%s run() except KeyboardInterrupt", __name__)
            self._log.fatal(repr(e))
        except BaseException as e:
            self._log.debug("%s run() except BaseException", __name__)
            log_exception(self._log, e, with_traceback=True)
            self._log.fatal("Aborted process with pid '%d'", pid)
        finally:
            self._log.info("Ended process with pid '%d'", pid)
            self._shutdown()


"""DisabledContent
"""

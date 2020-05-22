#!/bin/false
# Intended to be executed as a Python module:  python3 -m MODULE

from argparse import ArgumentParser
from logging  import DEBUG
from pathlib  import Path

from logzero import logger as log
from logzero import loglevel

from build.helper.Python.my_system                     import recreate_directory
from potrero_cloud_lab.src.pipeline.utility.processing import create_pid_file
from potrero_cloud_lab.src.pipeline.utility.processing import delete_pid_file
from potrero_cloud_lab.src.pipeline.utility.processing import get_pid

from .config                  import Config
from .script_project_activate import render as render_project_activate_script


loglevel(level=DEBUG)
c = Config()


class ContentGeneratorApp:
    def __init__(self, target_directory):
        assert isinstance(target_directory, Path)
        self._target_directory = target_directory

    def _generate(self):
        maybe_create_directory(directory)
        render_project_activate_script(self._target_directory)

    def _prepare(self):
        log.info(
            "Generating scripts into directory '%s'", self._target_directory
            )
        recreate_directory(self._target_directory)

    def _shutdown(self):
        delete_pid_file(c.pid_file)

    def _startup(self):
        create_pid_file(c.pid_file)

    def run(self):
        try:
            self._startup()
            self._prepare()
            self._generate()
        finally:
            self._shutdown()

def _parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'target_directory', help='into which to generate output'
        )
    return parser.parse_args()

def run():
    try:
        log.info("Began ContentGeneratorApp process with pid '%d'", get_pid())
        args = _parse_args()
        ContentGeneratorApp(Path(args.target_directory)).run()
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

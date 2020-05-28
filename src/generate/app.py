#!/bin/false
# Intended to be executed as a Python module:  python3 -m MODULE

from argparse import ArgumentParser
from logging  import DEBUG
from pathlib  import Path

from logzero import logger as log
from logzero import loglevel

from .config                        import Config
from .project_activate_script       import generate as generate_project_activate_script
from .utility.my_system             import recreate_directory
from .utility.singleton_application import SingletonApplication


loglevel(level=DEBUG)


class ContentGeneratorApp(SingletonApplication):
    def __init__(self, pid_file, target_directory):
        super().__init__(pid_file)
        assert isinstance(target_directory, Path)
        self._target_directory = target_directory

    def _generate(self):
        generate_project_activate_script(self._target_directory)

    def _run(self):
        super()._run()
        log.info(
            "Generating content into directory '%s'", self._target_directory
            )
        recreate_directory(self._target_directory)
        self._generate()


def _parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'target_directory', help='into which to generate output'
        )
    return parser.parse_args()

def run():
    args = _parse_args()
    ContentGeneratorApp(
        Config().pid_file,
        Path(args.target_directory)
        ).run()

''' Disabled content
'''


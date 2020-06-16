#!/usr/bin/env false
"""
Intended to be executed as a Python module:  python3 -m MODULE
"""
import sys

from argparse import ArgumentParser
from logging  import DEBUG
from pathlib  import Path

from logzero import logger as log
from logzero import loglevel

from utility.my_system             import recreate_directory
from utility.singleton_application import SingletonApplication

from .config                              import Config
from .script.bash.project_activate_script import generate as generate_project_activate_script
from .document.markdown.all               import generate as generate_markdown_documents
from .script.bash.all                     import generate as generate_bash_scripts
from .script.bash.briteonyx.all           import generate as generate_briteonyx_scripts
from .script.python.all                   import generate as generate_python_scripts


loglevel(level=DEBUG)


class ContentGeneratorApp(SingletonApplication):
    def __init__(self, pid_file):
        super().__init__(pid_file)

    def _generate(self):
        generate_project_activate_script(self._target_directory)

        generate_bash_scripts(self._target_directory)
        generate_briteonyx_scripts(self._target_directory)
        generate_markdown_documents(self._target_directory)
        generate_python_scripts(self._target_directory)

    def _parse_args(self):
        parser = ArgumentParser()
        parser.add_argument(
            'target_directory', help='into which to generate output'
            )
        return parser.parse_args()

    def _prepare(self):
        args = self._parse_args()
        self._target_directory = Path(args.target_directory)
        log.info(
            "Generating content into directory '%s'", self._target_directory
            )
        recreate_directory(self._target_directory)

    def _report(self):
        """Report some interesting system characteristics."""
        log.debug("sys.getdefaultencoding()='%s'", sys.getdefaultencoding())
        log.debug("sys.getfilesystemencoding()='%s'", sys.getfilesystemencoding())
        log.debug("sys.stderr.encoding='%s'", sys.stderr.encoding)
        log.debug("sys.stdin.encoding='%s'", sys.stdin.encoding)
        log.debug("sys.stdout.encoding='%s'", sys.stdout.encoding)

    def _run(self):
        super()._run()
        self._report()
        self._prepare()
        self._generate()


def run():
    ContentGeneratorApp(Config().pid_file).run()

'''DisabledContent
'''


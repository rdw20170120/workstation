#!/usr/bin/env false
"""Generate source for this project.

Intended to be executed as a Python module:  python3 -m MODULE
"""
# Internal packages  (absolute references, distributed with Python)
from   argparse import ArgumentParser
from   pathlib  import Path
import sys
# External packages  (absolute references, NOT distributed with Python)
from logzero import logger as log
# Library modules    (absolute references, NOT packaged, in project)
from utility.my_logging            import configure as configure_logging
from utility.my_system             import recreate_directory
from utility.singleton_application import SingletonApplication
# Co-located modules (relative references, NOT packaged, in project)
from .config                              import Config
from .script.bash.project_activate_script import generate as generate_project_activate_script
from .document.markdown.all               import generate as generate_markdown_documents
from .script.bash.all                     import generate as generate_bash_scripts
from .script.bash.briteonyx.all           import generate as generate_briteonyx_scripts
from .script.python.all                   import generate as generate_python_scripts


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
    c = Config()
    configure_logging(c)
    ContentGeneratorApp(c.pid_file).run()

'''DisabledContent
'''


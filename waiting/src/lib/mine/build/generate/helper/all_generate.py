#!/usr/bin/env python

import argparse
import os
from . import script_briteonyx_bootstrap
from . import script_briteonyx_declare
from . import script_briteonyx_environment
from . import script_gradle_activate
from . import script_linux_activate
from . import script_project_activate
from . import script_project_environment
from . import script_project_maybe_activate
from . import script_python_activate
from . import script_user_environment
import sys

from logging import getLogger
from my_logging import configure_logging
from my_system import maybe_create_directory
from my_system import recreate_directory


LOG = getLogger("all_generate")


def main():
    try:
        configure_logging()
        LOG.debug("main() try = began")

        parser = argparse.ArgumentParser()
        parser.add_argument(
            "source_directory", help="from which to generate output"
        )
        parser.add_argument(
            "target_directory", help="into which to generate output"
        )
        args = parser.parse_args()

        LOG.info(
            "Generating scripts from directory '{0}' into directory '{1}'".format(
                args.source_directory, args.target_directory
            )
        )
        recreate_directory(args.target_directory)

        directory = os.path.join(args.target_directory, "helper", "activation")
        maybe_create_directory(directory)
        script_linux_activate.render(directory, "activate.src")

        directory = os.path.join(
            args.target_directory, "helper", "activation", "add_on"
        )
        maybe_create_directory(directory)
        script_gradle_activate.render(directory, "activate-Gradle.src")
        script_python_activate.render(directory, "activate-Python.src")

        directory = os.path.join(args.target_directory, "sample_project")
        maybe_create_directory(directory)
        script_project_activate.render(directory, "activate.src")

        directory = os.path.join(
            args.target_directory, "sample_project", "BriteOnyx"
        )
        maybe_create_directory(directory)
        script_briteonyx_bootstrap.render(directory, "bootstrap.src")
        script_briteonyx_declare.render(directory, "declare.src")
        script_briteonyx_environment.render(directory, "env.src")
        script_project_maybe_activate.render(directory, "maybeActivate.src")

        directory = os.path.join(
            args.target_directory, "sample_project", "BriteOnyx", "starter"
        )
        maybe_create_directory(directory)
        script_project_environment.render(directory, "project-env.src")
        script_user_environment.render(directory, "user-BriteOnyx.src")
    except Exception as e:
        LOG.error("main() except Exception = failure")
        LOG.exception(e)
        sys.exit(1)
    else:
        LOG.debug("main() else = success")
        sys.exit(0)
    finally:
        LOG.debug("main() finally = ended")


if __name__ == "__main__":
    main()


""" Disabled content
"""

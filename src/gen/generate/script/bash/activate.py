#!/usr/bin/env false
"""Generate script to activate project.
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.renderer import write_to_file

# Project modules   (relative references, NOT packaged, in project)
from .activating.activate import render as render_before_activation
from .briteonyx.activate import render as render_after_activation


def generate(config, directory=None, filename=None):
    write_to_file(
        render_before_activation(config) + render_after_activation(config),
        directory / filename,
    )


"""DisabledContent
"""

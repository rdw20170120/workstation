#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.frame import *

# Project modules   (relative references, NOT packaged, in project)
from .element import *
from .material import *


def header_activation(config):
    return [
        shebang_sourced(),
        comment("Intended to be sourced in a Bash shell during activation."),
        tracing_in_header(config),
        no(set_("-e")),
        no(trap("...", "EXIT")),
        rule(),
    ]


def maybe_copy_file(source, target):
    return [
        command("maybe_copy_file", source, target),
    ]


def remembering(name):
    return [
        command("remembering", name),
    ]


"""DisabledContent
"""

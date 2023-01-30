#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.bash.complete import generate_activation as activation

# Project modules   (relative references, NOT packaged, in project)


def generate(directory):
    activation(directory, "declare-base.bash")


"""DisabledContent
"""

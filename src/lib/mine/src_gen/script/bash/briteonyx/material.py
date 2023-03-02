#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.material import *

# Project modules   (relative references, NOT packaged, in project)
from .frame import *


def require_script(script):
    return command("require_script", script)


"""DisabledContent
"""

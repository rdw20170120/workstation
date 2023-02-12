#!/usr/bin/env false
"""TODO: Write

TODO: Generate tests
NOTE: There is little value in testing "composed" methods,
e.g., those consisting of 'return [...]'.
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.material import *
from src_gen.renderer import Renderer

# Project modules   (relative references, NOT packaged, in project)
from .frame import *
from .material import *
from .render import my_visitor_map


s = Renderer(my_visitor_map)._serialize

"""DisabledContent
"""

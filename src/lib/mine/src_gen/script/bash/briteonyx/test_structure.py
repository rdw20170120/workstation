#!/usr/bin/env false
"""TODO: Write

TODO: Generate tests
NOTE: There is little value in testing "composed" methods,
e.g., those consisting of 'return [...]'.
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from ....renderer import Renderer
from .source import my_visitor_map
from .structure import *


s = Renderer(my_visitor_map)._serialize

"""DisabledContent
"""

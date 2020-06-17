#!/usr/bin/env false
"""
"""
from .source     import my_visitor_map
from .structure  import * 
from ....renderer import Renderer


# NOTE: There is little value in testing "composed" methods,
# e.g., those consisting of 'return [...]'.
# TODO: Generate tests

s = Renderer(my_visitor_map)._serialize

'''DisabledContent
'''


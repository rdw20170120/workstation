#!/usr/bin/env false

from .briteonyx_script    import visitor_map
from .briteonyx_structure import * 
from .renderer            import Renderer


# NOTE: There is little value in testing "composed" methods,
# e.g., those consisting of 'return [...]'.
# TODO: Generate tests

s = Renderer(visitor_map)._serialize


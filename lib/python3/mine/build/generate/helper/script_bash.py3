import os

from renderer import Renderer
from throw_out_your_templates_3_core_visitor_map import VisitorMap
from throw_out_your_templates_4_core_default_visitors import default_visitors_map


VISITOR_MAP = VisitorMap(parent_map=default_visitors_map)


def render(script, visitor_map, target_directory, target_file):
    Renderer(visitor_map).render(script, os.path.join(target_directory, target_file))


class Script(object):
    def __init__(self):
        object.__init__(self)
        self._content = []

    def add(self, content):
        self._content.append(content)
        return self


@VISITOR_MAP.register(Script)
def visit_script(script, walker):
    walker.walk(script._content)


""" Disabled content
"""


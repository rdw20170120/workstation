from tavis_rudd.throw_out_your_templates.section_3 import VisitorMap

from .                 import script
from .script_structure import *


class BashScript(script.Script):
    def __init__(self, content=None):
        super().__init__(content)

    def add(self, content):
        self._content.append(content)
        return self


visitor_map = VisitorMap(parent_map=script.visitor_map)

@visitor_map.register(BashScript)
def _visit_script(script, walker):
    walker.walk(script._content)

def render(parent_directory, filename=None, content=None, visitor_map=visitor_map):
    script.render(parent_directory, filename, content, visitor_map)

""" Disabled content
"""


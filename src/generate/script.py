from tavis_rudd.throw_out_your_templates.section_3 import VisitorMap
from tavis_rudd.throw_out_your_templates.section_4 import default_visitors_map

from build.helper.Python.my_system import maybe_create_directory

from .renderer import Renderer


class Script(object):
    def __init__(self, content=None):
        super().__init__()
        if content is None: self._content = []
        else: self._content = content

    def add(self, content):
        self._content.append(content)
        return self


visitor_map = VisitorMap(parent_map=default_visitors_map)

@visitor_map.register(Script)
def visit_script(script, walker):
    walker.walk(script._content)

def render(
        parent_directory,
        filename=None,
        content=None,
        visitor_map=visitor_map
        ):
    assert content
    filepath = None
    if filename is not None: filepath = parent_directory / filename
    if parent_directory is not None: maybe_create_directory(parent_directory)
    Renderer(visitor_map).render(content, filepath)

""" Disabled content
"""


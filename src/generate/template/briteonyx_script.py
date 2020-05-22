from tavis_rudd.throw_out_your_templates.section_3 import VisitorMap

from . import bash_script


class BriteOnyxScript(bash_script.BashScript):
    def __init__(self, content=None):
        super().__init__(content)


visitor_map = VisitorMap(parent_map=bash_script.visitor_map)

@visitor_map.register(BriteOnyxScript)
def _visit_script(script, walker):
    walker.walk(script._content)

def render(parent_directory, filename=None, content=None, visitor_map=visitor_map):
    bash_script.render(parent_directory, filename, content, visitor_map)


""" Disabled content
"""


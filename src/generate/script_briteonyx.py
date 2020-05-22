from tavis_rudd.throw_out_your_templates.section_3 import VisitorMap

from . import script_bash


class BriteOnyxScript(script_bash.BashScript):
    def __init__(self, content=None):
        super().__init__(content)


visitor_map = VisitorMap(parent_map=script_bash.visitor_map)

@visitor_map.register(BriteOnyxScript)
def visit_script(script, walker):
    walker.walk(script._content)

def render(parent_directory, filename=None, content=None, visitor_map=visitor_map):
    script_bash.render(parent_directory, filename, content, visitor_map)


""" Disabled content
"""


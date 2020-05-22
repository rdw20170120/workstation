from tavis_rudd.throw_out_your_templates.section_3 import VisitorMap
from tavis_rudd.throw_out_your_templates.section_4 import default_visitors_map


class BashScript(object):
    def __init__(self):
        super().__init__(self)
        self._content = []

    def add(self, content):
        self._content.append(content)
        return self


visitor_map = VisitorMap(parent_map=default_visitors_map)

@visitor_map.register(BashScript)
def visit_script(script, walker):
    walker.walk(script._content)


""" Disabled content
"""


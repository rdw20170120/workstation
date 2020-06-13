from throw_out_your_templates.section_3 import VisitorMap

from .bash_script import BashScript
from .bash_script import visitor_map as parent_visitor_map


visitor_map = VisitorMap(parent_map=parent_visitor_map)


class BriteOnyxScript(BashScript):
    def __init__(self, visitor_map,
        relative_directory, filename,
        content
        ):
        super().__init__(
            visitor_map,
            relative_directory, filename,
            content,
            )


''' Disabled content
'''


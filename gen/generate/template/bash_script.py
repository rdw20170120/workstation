from ..tavis_rudd.throw_out_your_templates.section_3 import VisitorMap

from .script           import Script
from .script           import visitor_map as parent_visitor_map
from .script_structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)


class BashScript(Script):
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


#!/usr/bin/env false
"""
"""
from throw_out_your_templates.section_3 import VisitorMap

from ..source    import Script
from ..source    import visitor_map as parent_visitor_map
from ..structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)


class PythonSource(Script):
    def __init__(self, visitor_map,
        relative_directory, filename,
        content
        ):
        super().__init__(
            visitor_map,
            relative_directory, filename,
            content,
            )

'''DisabledContent
'''


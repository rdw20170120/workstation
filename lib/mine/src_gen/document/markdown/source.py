#!/usr/bin/env false
"""
"""
from throw_out_your_templates.section_3 import VisitorMap

from ...source import Content
from ...source import visitor_map as parent_visitor_map


visitor_map = VisitorMap(parent_map=parent_visitor_map)


class Markdown(Content):
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


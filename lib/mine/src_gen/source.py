#!/usr/bin/env false
"""
"""
from pathlib import Path

from utility.my_system import maybe_create_directory

from throw_out_your_templates.section_3 import VisitorMap
from throw_out_your_templates.section_4 import visitor_map as parent_visitor_map
from .renderer                          import Renderer


visitor_map = VisitorMap(parent_map=parent_visitor_map)


class Content(object):
    def __init__(self, visitor_map,
        relative_directory, filename,
        content
        ):
        super().__init__()
        assert isinstance(filename, str)
        assert isinstance(relative_directory, Path)
        assert not relative_directory.is_absolute()
        assert isinstance(visitor_map, VisitorMap)
        self._content = content
        self._filename = filename
        self._relative_directory = relative_directory
        self._visitor_map = visitor_map

    def add(self, content):
        self._content.append(content)
        return self

    def generate(self, target_directory):
        assert isinstance(target_directory, Path)
        directory = target_directory / self._relative_directory
        maybe_create_directory(directory)
        Renderer(self._visitor_map).render(self._content, directory / self._filename)

    def print(self):
        Renderer(self._visitor_map).render(self._content)


@visitor_map.register(Content)
def _visit_content(content, walker):
    walker.walk(content._content)

'''DisabledContent
'''


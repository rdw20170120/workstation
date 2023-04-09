#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.renderer import Renderer
from throw_out_your_templates.section_3 import VisitorMap
from throw_out_your_templates.section_4 import visitor_map
from utility import my_assert as is_
from utility.filesystem import maybe_create_directory

# Project modules   (relative references, NOT packaged, in project)


my_visitor_map = VisitorMap(parent_map=visitor_map)


class Content(object):
    def __init__(
        self,
        content,
        visitor_map=None,
    ):
        super().__init__()
        self._content = content
        if visitor_map is None:
            visitor_map = my_visitor_map
        assert is_.instance(visitor_map, VisitorMap)
        self._visitor_map = visitor_map

    def add(self, content):
        self._content.append(content)
        return self

    def generate(self, directory=None, filename=None):
        if directory is None:
            return Renderer(self._visitor_map).render(self._content)
        elif filename is None:
            return Renderer(self._visitor_map).render(self._content)
        else:
            assert is_.instance(directory, Path)
            maybe_create_directory(directory)
            Renderer(self._visitor_map).render(self._content, directory / filename)


@my_visitor_map.register(Content)
def _visit_content(content, walker):
    walker.walk(content._content)


def generate(content, directory=None, filename=None):
    return Content(content).generate(directory, filename)


"""DisabledContent
"""

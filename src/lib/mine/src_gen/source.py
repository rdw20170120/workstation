#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from throw_out_your_templates.section_3 import VisitorMap
from throw_out_your_templates.section_4 import visitor_map

# Project modules   (relative references, NOT packaged, in project)
from utility.filesystem import maybe_create_directory
from utility import my_assert as is_
from src_gen.renderer import Renderer


my_visitor_map = VisitorMap(parent_map=visitor_map)


class Content(object):
    def __init__(self, visitor_map, content):
        super().__init__()
        assert is_.instance(visitor_map, VisitorMap)
        self._content = content
        self._visitor_map = visitor_map

    def add(self, content):
        self._content.append(content)
        return self

    def generate(self, target_file=None):
        if target_file is None:
            Renderer(self._visitor_map).render(self._content)
        else:
            Renderer(self._visitor_map).render(self._content, target_file)


@my_visitor_map.register(Content)
def _visit_content(content, walker):
    walker.walk(content._content)


def generate(
    content,
    directory=None,
    filename=None,
    visitor_map=None,
):
    # TODO: REFACTOR: Reduce code duplication
    if visitor_map is None:
        visitor_map = my_visitor_map
    source = Content(visitor_map, content)
    if directory is None:
        source.generate()
    elif filename is None:
        source.generate()
    else:
        assert is_.instance(directory, Path)
        maybe_create_directory(directory)
        source.generate(directory / filename)


"""DisabledContent
"""

#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.render import Script
from src_gen.script.render import my_visitor_map as parent_visitor_map
from throw_out_your_templates.section_3 import VisitorMap
from utility import my_assert as is_
from utility.filesystem import maybe_create_directory

# Project modules   (relative references, NOT packaged, in project)


my_visitor_map = VisitorMap(parent_map=parent_visitor_map)


class BashScript(Script):
    def __init__(self, visitor_map, content):
        super().__init__(visitor_map, content)


def generate(
    content,
    directory=None,
    filename=None,
    visitor_map=None,
):
    # TODO: REFACTOR: Reduce code duplication
    if visitor_map is None:
        visitor_map = my_visitor_map
    source = BashScript(visitor_map, content)
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

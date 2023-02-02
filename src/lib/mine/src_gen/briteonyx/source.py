#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from throw_out_your_templates.section_3 import VisitorMap

# Project modules   (relative references, NOT packaged, in project)
from src_gen.bash.source import my_visitor_map as parent_visitor_map


my_visitor_map = VisitorMap(parent_map=parent_visitor_map)



"""DisabledContent
from pathlib import Path
from utility.filesystem import maybe_create_directory
from utility import my_assert as is_
from src_gen.bash.source import BashScript

class BriteOnyxScript(BashScript):
    def __init__(self, visitor_map, content):
        super().__init__(visitor_map, content)


def generate(
    content,
    directory=None,
    filename=None,
    visitor_map=None,
):
    if visitor_map is None:
        visitor_map = my_visitor_map
    source = BriteOnyxScript(visitor_map, content)
    if directory is None:
        source.generate()
    elif filename is None:
        source.generate()
    else:
        assert is_.instance(directory, Path)
        maybe_create_directory(directory)
        source.generate(directory / filename)
"""

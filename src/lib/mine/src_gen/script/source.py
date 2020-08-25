#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
from pathlib import Path
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from throw_out_your_templates.section_3 import VisitorMap
from utility.filesystem import maybe_create_directory
from utility.my_assert import assert_absolute_directory
from utility.my_assert import assert_instance
# Co-located modules (relative references, NOT packaged, in project)
from ..source import Content
from ..source import my_visitor_map as parent_visitor_map


my_visitor_map = VisitorMap(parent_map=parent_visitor_map)


class Script(Content):
    def __init__(self, visitor_map, content):
        super().__init__(visitor_map, content)


def generate(content,
    directory=None, subdirectories=None, filename=None,
    visitor_map=None
    ):
    if visitor_map is None: visitor_map = my_visitor_map
    source = Script(visitor_map, content)
    if directory is None: source.generate()
    elif filename is None: source.generate()
    else:
        assert assert_instance(directory, Path)
        assert assert_absolute_directory(directory)
        directory = directory / subdirectories
        maybe_create_directory(directory)
        source.generate(directory / filename)

'''DisabledContent
'''


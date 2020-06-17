#!/usr/bin/env false
"""
"""
from pathlib import Path

from throw_out_your_templates.section_3 import VisitorMap
from utility.my_system                  import maybe_create_directory

from ..source    import Script
from ..source    import my_visitor_map as parent_visitor_map
from ..structure import *


my_visitor_map = VisitorMap(parent_map=parent_visitor_map)


class BashScript(Script):
    def __init__(self, visitor_map, content):
        super().__init__(visitor_map, content)


def generate(content,
    directory=None, subdirectories=None, filename=None,
    visitor_map=None
    ):
    if visitor_map is None: visitor_map = my_visitor_map
    source = BashScript(visitor_map, content)
    if directory is None: source.generate()
    elif filename is None: source.generate()
    else:
        assert isinstance(directory, Path)
        assert directory.is_absolute()
        directory = directory / subdirectories
        maybe_create_directory(directory)
        source.generate(directory / filename)

'''DisabledContent
'''


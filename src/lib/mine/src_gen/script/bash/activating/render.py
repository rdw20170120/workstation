#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
from pathlib import Path

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.script.bash.render import BashScript
from src_gen.script.bash.render import my_visitor_map as parent_visitor_map
from throw_out_your_templates.section_3 import VisitorMap
from utility import my_assert as is_
from utility.filesystem import maybe_create_directory

# Project modules   (relative references, NOT packaged, in project)


my_visitor_map = VisitorMap(parent_map=parent_visitor_map)


class ActivatingBashScript(BashScript):
    def __init__(
        self,
        content,
        visitor_map=None,
    ):
        if visitor_map is None:
            visitor_map = my_visitor_map
        super().__init__(content, visitor_map)


def generate(content, directory=None, filename=None):
    return ActivatingBashScript(content).generate(directory, filename)


"""DisabledContent
"""

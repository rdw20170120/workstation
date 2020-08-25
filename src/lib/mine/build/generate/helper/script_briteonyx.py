from . import script_bash

from throw_out_your_templates_3_core_visitor_map import VisitorMap


class Script(script_bash.Script):
    def __init__(self):
        script_bash.Script.__init__(self)


VISITOR_MAP = VisitorMap(parent_map=script_bash.VISITOR_MAP)


""" Disabled content
"""


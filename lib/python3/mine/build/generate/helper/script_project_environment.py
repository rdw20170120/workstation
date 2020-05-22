from . import script_bash
from . import script_briteonyx

from throw_out_your_templates_3_core_visitor_map import VisitorMap

from .structure_bash import *
from .structure_briteonyx import *


class Script(script_briteonyx.Script):
    def __init__(self, content):
        script_briteonyx.Script.__init__(self)
        self._content = content


def build():
    return Script([
        source_header(),
        comment('Configure this project'),
        line(),
        comment('TODO: Implement'),
        line('export BO_ProjectName=TODO'),
        disabled_content_footer(),
    ])
    

VISITOR_MAP = VisitorMap(parent_map=script_bash.VISITOR_MAP)


def render(target_directory, target_file):
    script_bash.render(build(), VISITOR_MAP, target_directory, target_file)


""" Disabled content
"""


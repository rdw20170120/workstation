import script_bash
import script_briteonyx

from throw_out_your_templates_3_core_visitor_map import VisitorMap

from structure_bash import *
from structure_briteonyx import *


class Script(script_briteonyx.Script):
    def __init__(self, content):
        script_briteonyx.Script.__init__(self)
        self._content = content


def build():
    return Script([
        source_header(),
        '''# Configure BriteOnyx deployment
# TODO: SOMEDAY: Keep BO_Version updated to latest published revision

[[ -z "$BO_Parent"  ]] && export BO_Parent=$HOME/.BO
[[ -z "$BO_Version" ]] && export BO_Version=rev36
[[ -z "$BO_Home"    ]] && export BO_Home=$BO_Parent/$BO_Version

alias functions='declare -F | sort'
''',
        disabled_content_footer(),
    ])


VISITOR_MAP = VisitorMap(parent_map=script_bash.VISITOR_MAP)


def render(target_directory, target_file):
    script_bash.render(build(), VISITOR_MAP, target_directory, target_file)


""" Disabled content
"""


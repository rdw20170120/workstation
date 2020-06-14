#!/usr/bin/env false
"""
"""
from throw_out_your_templates.section_3 import VisitorMap

from src_gen.script.bash.source    import BashScript
from src_gen.script.bash.source    import visitor_map as parent_visitor_map
from src_gen.script.bash.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _generate(content, directory, subdirectories, file_name):
    source = BashScript(
        visitor_map,
        subdirectories, file_name,
        content
        )
    source.generate(directory)

def _sourced():
    return [
        sourced_header(),
        todo('DESCRIPTION'),
        line(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def generate(directory):
    sub = Path('.')
    _generate(_sourced(), directory, sub, 'alias.bash')
    sub = Path('BriteOnyx', 'bin', 'lib')
    _generate(_sourced(), directory, sub, 'alias-common.bash')
    _generate(_sourced(), directory, sub, 'alias-git.bash')
    _generate(_sourced(), directory, sub, 'pve-activate.bash')
    sub = Path('sample')
    _generate(_sourced(), directory, sub, 'alias.bash')
    _generate(_sourced(), directory, sub, 'context.bash')

'''DisabledContent
'''


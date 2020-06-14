#!/usr/bin/env false
"""
"""
from throw_out_your_templates.section_3 import VisitorMap

from src_gen.script.bash.source    import BashScript
from src_gen.script.bash.source    import visitor_map as parent_visitor_map
from src_gen.script.bash.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _generate(content, target_directory, subdirectories, file_name):
    source = BashScript(
        visitor_map,
        subdirectories, file_name,
        content
        )
    source.generate(target_directory)

def _to_be_executed():
    return [
        executed_header(),
        todo('DESCRIPTION'),
        line(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def _to_be_sourced():
    return [
        sourced_header(),
        todo('DESCRIPTION'),
        line(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def generate(target_directory):
    sub = Path('.')
    _generate(_to_be_sourced(), target_directory, sub, 'alias.bash')
    sub = Path('BriteOnyx', 'bin', 'lib')
    _generate(_to_be_sourced(), target_directory, sub, 'alias-common.bash')
    _generate(_to_be_sourced(), target_directory, sub, 'alias-git.bash')
    _generate(_to_be_sourced(), target_directory, sub, 'pve-activate.bash')
    sub = Path('sample')
    _generate(_to_be_sourced(), target_directory, sub, 'alias.bash')
    _generate(_to_be_sourced(), target_directory, sub, 'context.bash')

'''DisabledContent
    sub = Path('.')
    _generate(target_directory, sub, '')
'''


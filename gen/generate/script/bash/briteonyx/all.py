#!/usr/bin/env false
"""
"""
from throw_out_your_templates.section_3 import VisitorMap

from src_gen.script.bash.briteonyx.source    import BriteOnyxScript
from src_gen.script.bash.briteonyx.source    import visitor_map as parent_visitor_map
from src_gen.script.bash.briteonyx.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _generate(content, target_directory, subdirectories, file_name):
    source = BriteOnyxScript(
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
    sub = Path('BriteOnyx', 'bin')
    _generate(_to_be_executed(), target_directory, sub, 'all-capture')
    _generate(_to_be_executed(), target_directory, sub, 'all-check')
    _generate(_to_be_executed(), target_directory, sub, 'dep-capture')
    _generate(_to_be_executed(), target_directory, sub, 'dep-check')
    _generate(_to_be_executed(), target_directory, sub, 'dep-reinstall')
    _generate(_to_be_executed(), target_directory, sub, 'dep-report')
    _generate(_to_be_executed(), target_directory, sub, 'dep-upgrade')
    _generate(_to_be_executed(), target_directory, sub, 'env-capture')
    _generate(_to_be_executed(), target_directory, sub, 'env-check')
    _generate(_to_be_executed(), target_directory, sub, 'env-report')
    _generate(_to_be_executed(), target_directory, sub, 'prj-clean')
    _generate(_to_be_executed(), target_directory, sub, 'prj-wipe')
    _generate(_to_be_executed(), target_directory, sub, 'pve-create')
    _generate(_to_be_executed(), target_directory, sub, 'pve-recreate')
    _generate(_to_be_executed(), target_directory, sub, 'pve-reinstall')
    _generate(_to_be_executed(), target_directory, sub, 'pve-rm')
    _generate(_to_be_executed(), target_directory, sub, 'py-2to3')
    _generate(_to_be_executed(), target_directory, sub, 'py-capture')
    _generate(_to_be_executed(), target_directory, sub, 'py-check')
    _generate(_to_be_executed(), target_directory, sub, 'py-compile')
    _generate(_to_be_executed(), target_directory, sub, 'py-report')
    _generate(_to_be_executed(), target_directory, sub, 'tool-capture')
    _generate(_to_be_executed(), target_directory, sub, 'tool-check')
    sub = Path('BriteOnyx', 'bin', 'lib')
    _generate(_to_be_sourced(), target_directory, sub, 'configure-Python.bash')
    sub = Path('bin')
    _generate(_to_be_executed(), target_directory, sub, 'app-run')
    _generate(_to_be_executed(), target_directory, sub, 'dep-install')
    _generate(_to_be_executed(), target_directory, sub, 'generate')
    _generate(_to_be_executed(), target_directory, sub, 'test-run')
    _generate(_to_be_executed(), target_directory, sub, 'tool-report')

'''DisabledContent
    sub = Path('.')
    _generate(_to_be_executed(), target_directory, sub, '')
'''


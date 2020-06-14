#!/usr/bin/env false
"""
"""
from throw_out_your_templates.section_3 import VisitorMap

from src_gen.script.bash.briteonyx.source    import BriteOnyxScript
from src_gen.script.bash.briteonyx.source    import visitor_map as parent_visitor_map
from src_gen.script.bash.briteonyx.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _executed():
    return [
        executed_header(),
        todo('DESCRIPTION'),
        line(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def _generate(content, directory, subdirectories, file_name):
    source = BriteOnyxScript(
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
    sub = Path('BriteOnyx', 'bin')
    _generate(_executed(), directory, sub, 'all-capture')
    _generate(_executed(), directory, sub, 'all-check')
    _generate(_executed(), directory, sub, 'dep-capture')
    _generate(_executed(), directory, sub, 'dep-check')
    _generate(_executed(), directory, sub, 'dep-reinstall')
    _generate(_executed(), directory, sub, 'dep-report')
    _generate(_executed(), directory, sub, 'dep-upgrade')
    _generate(_executed(), directory, sub, 'env-capture')
    _generate(_executed(), directory, sub, 'env-check')
    _generate(_executed(), directory, sub, 'env-report')
    _generate(_executed(), directory, sub, 'prj-clean')
    _generate(_executed(), directory, sub, 'prj-wipe')
    _generate(_executed(), directory, sub, 'pve-create')
    _generate(_executed(), directory, sub, 'pve-recreate')
    _generate(_executed(), directory, sub, 'pve-reinstall')
    _generate(_executed(), directory, sub, 'pve-rm')
    _generate(_executed(), directory, sub, 'py-2to3')
    _generate(_executed(), directory, sub, 'py-capture')
    _generate(_executed(), directory, sub, 'py-check')
    _generate(_executed(), directory, sub, 'py-compile')
    _generate(_executed(), directory, sub, 'py-report')
    _generate(_executed(), directory, sub, 'tool-capture')
    _generate(_executed(), directory, sub, 'tool-check')
    sub = Path('BriteOnyx', 'bin', 'lib')
    _generate(_sourced(), directory, sub, 'configure-Python.bash')
    sub = Path('bin')
    _generate(_executed(), directory, sub, 'app-run')
    _generate(_executed(), directory, sub, 'dep-install')
    _generate(_executed(), directory, sub, 'generate')
    _generate(_executed(), directory, sub, 'test-run')
    _generate(_executed(), directory, sub, 'tool-report')

'''DisabledContent
'''


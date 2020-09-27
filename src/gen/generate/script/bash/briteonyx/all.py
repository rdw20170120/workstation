#!/usr/bin/env false
"""Generate all BriteOnyx BASH scripts."""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from src_gen.script.bash.briteonyx.source import generate as gen
from src_gen.script.bash.briteonyx.structure import *
# Co-located modules (relative references, NOT packaged, in project)


def _executed():
    return [
        executed_header(),
        todo('DESCRIPTION'),
        line(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def _generate_BriteOnyx(directory):
    sub = Path('BriteOnyx', 'bin')
    gen(_executed(), directory, sub, 'all-capture')
    gen(_executed(), directory, sub, 'all-check')
    gen(_executed(), directory, sub, 'dep-capture')
    gen(_executed(), directory, sub, 'dep-check')
    gen(_executed(), directory, sub, 'dep-reinstall')
    gen(_executed(), directory, sub, 'dep-report')
    gen(_executed(), directory, sub, 'dep-upgrade')
    gen(_executed(), directory, sub, 'env-capture')
    gen(_executed(), directory, sub, 'env-check')
    gen(_executed(), directory, sub, 'env-report')
    gen(_executed(), directory, sub, 'prj-clean')
    gen(_executed(), directory, sub, 'prj-wipe')
    gen(_executed(), directory, sub, 'pve-create')
    gen(_executed(), directory, sub, 'pve-recreate')
    gen(_executed(), directory, sub, 'pve-reinstall')
    gen(_executed(), directory, sub, 'pve-rm')
    gen(_executed(), directory, sub, 'py-2to3')
    gen(_executed(), directory, sub, 'py-capture')
    gen(_executed(), directory, sub, 'py-check')
    gen(_executed(), directory, sub, 'py-compile')
    gen(_executed(), directory, sub, 'py-report')
    gen(_executed(), directory, sub, 'sig-check')
    gen(_executed(), directory, sub, 'sig-make')
    gen(_executed(), directory, sub, 'tool-capture')
    gen(_executed(), directory, sub, 'tool-check')
    sub = Path('BriteOnyx', 'bin', 'lib')
    gen(_sourced(), directory, sub, 'configure-Python.bash')

def _generate_bin(directory):
    sub = Path('bin')
    gen(_executed(), directory, sub, 'app-run')
    gen(_executed(), directory, sub, 'dep-install')
    gen(_executed(), directory, sub, 'gen-run')
    gen(_executed(), directory, sub, 'test-run')
    gen(_executed(), directory, sub, 'tool-report')
    sub = Path('bin', 'lib')

def _sourced():
    return [
        sourced_header(),
        todo('DESCRIPTION'),
        line(),
        todo('CONTENT'),
        disabled_content_footer(),
    ]

def generate(directory):
    _generate_BriteOnyx(directory)
    _generate_bin(directory)

'''DisabledContent
'''


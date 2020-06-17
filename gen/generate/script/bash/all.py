#!/usr/bin/env false
"""
"""
from src_gen.script.bash.source    import generate as gen
from src_gen.script.bash.structure import *


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
    gen(_sourced(), directory, sub, 'alias.bash')
    sub = Path('BriteOnyx', 'bin', 'lib')
    gen(_sourced(), directory, sub, 'alias-common.bash')
    gen(_sourced(), directory, sub, 'alias-git.bash')
    gen(_sourced(), directory, sub, 'pve-activate.bash')
    sub = Path('sample')
    gen(_sourced(), directory, sub, 'alias.bash')
    gen(_sourced(), directory, sub, 'context.bash')

'''DisabledContent
'''


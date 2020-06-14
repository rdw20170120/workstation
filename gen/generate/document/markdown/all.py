#!/usr/bin/env false
"""
"""
from throw_out_your_templates.section_3 import VisitorMap

from src_gen.document.markdown.source    import Markdown
from src_gen.document.markdown.source    import visitor_map as parent_visitor_map
from src_gen.document.markdown.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _generate(content, target_directory, subdirectories, file_name):
    source = Markdown(
        visitor_map,
        subdirectories, file_name,
        content
        )
    source.generate(target_directory)

def _build():
    return [
        h1('TODO'),
    ]

def generate(target_directory):
    sub = Path('.')
    _generate(_build(), target_directory, sub, 'README.md')
    _generate(_build(), target_directory, sub, 'TODO.md')
    sub = Path('BriteOnyx')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('BriteOnyx', 'bin')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('BriteOnyx', 'bin', 'lib')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('BriteOnyx', 'doc')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('bin')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('bin', 'lib')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('cfg')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('doc')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('gen')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('lib')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('lib', 'mine')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('lib', 'third_party')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('out')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('sample')
    _generate(_build(), target_directory, sub, 'README.md')
    sub = Path('src')
    _generate(_build(), target_directory, sub, 'README.md')

'''DisabledContent
    sub = Path('.')
    _generate(_build(), target_directory, sub, '')
'''


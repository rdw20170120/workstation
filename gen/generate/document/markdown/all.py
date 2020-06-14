#!/usr/bin/env false
"""
"""
from throw_out_your_templates.section_3 import VisitorMap

from src_gen.document.markdown.source    import Markdown
from src_gen.document.markdown.source    import visitor_map as parent_visitor_map
from src_gen.document.markdown.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _document():
    return [
        h1('TODO'),
    ]

def _generate(content, directory, subdirectories, file_name):
    source = Markdown(
        visitor_map,
        subdirectories, file_name,
        content
        )
    source.generate(directory)

def generate(directory):
    sub = Path('.')
    _generate(_document(), directory, sub, 'README.md')
    _generate(_document(), directory, sub, 'TODO.md')
    sub = Path('BriteOnyx')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('BriteOnyx', 'bin')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('BriteOnyx', 'bin', 'lib')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('BriteOnyx', 'doc')
    _generate(_document(), directory, sub, 'HowTo-activate_this_project.md')
    _generate(_document(), directory, sub, 'HowTo-execute_application.md')
    _generate(_document(), directory, sub, 'HowTo-install-packages.md')
    _generate(_document(), directory, sub, 'HowTo-setup-AWS_CLI.md')
    _generate(_document(), directory, sub, 'HowTo-setup-Python_virtual_environment.md')
    _generate(_document(), directory, sub, 'HowTo-setup-source_control.md')
    _generate(_document(), directory, sub, 'HowTo-setup-workstation.md')
    _generate(_document(), directory, sub, 'HowTo-test.md')
    _generate(_document(), directory, sub, 'README.md')
    _generate(_document(), directory, sub, 'project_initiation.md')
    sub = Path('bin')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('bin', 'lib')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('cfg')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('doc')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('gen')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('home')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('home', '.ssh')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('home', 'Linux')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('home', 'bin')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('home', 'bin', 'lib')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('home', 'macOS')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('lib')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('lib', 'mine')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('lib', 'mine', 'src_gen')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('lib', 'mine', 'throw_out_your_templates')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('lib', 'mine', 'utility')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('lib', 'third_party')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('out')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('sample')
    _generate(_document(), directory, sub, 'README.md')
    sub = Path('src')
    _generate(_document(), directory, sub, 'README.md')

'''DisabledContent
'''


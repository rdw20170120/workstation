#!/usr/bin/env false
"""
"""
from src_gen.document.markdown.source    import generate as gen
from src_gen.document.markdown.structure import *


def _document():
    return [
        h1('TODO'),
    ]

def generate(directory):
    sub = Path('.')
    gen(_document(), directory, sub, 'README.md')
    gen(_document(), directory, sub, 'TODO.md')
    sub = Path('BriteOnyx')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('BriteOnyx', 'bin')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('BriteOnyx', 'bin', 'lib')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('BriteOnyx', 'doc')
    gen(_document(), directory, sub, 'HowTo-activate_this_project.md')
    gen(_document(), directory, sub, 'HowTo-execute_application.md')
    gen(_document(), directory, sub, 'HowTo-install-packages.md')
    gen(_document(), directory, sub, 'HowTo-setup-AWS_CLI.md')
    gen(_document(), directory, sub, 'HowTo-setup-Python_virtual_environment.md')
    gen(_document(), directory, sub, 'HowTo-setup-source_control.md')
    gen(_document(), directory, sub, 'HowTo-setup-workstation.md')
    gen(_document(), directory, sub, 'HowTo-test.md')
    gen(_document(), directory, sub, 'README.md')
    gen(_document(), directory, sub, 'project_initiation.md')
    sub = Path('bin')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('bin', 'lib')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('cfg')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('doc')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('gen')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('home')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('home', '.ssh')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('home', 'Linux')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('home', 'bin')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('home', 'bin', 'lib')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('home', 'macOS')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('lib')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('lib', 'mine')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('lib', 'mine', 'src_gen')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('lib', 'mine', 'throw_out_your_templates')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('lib', 'mine', 'utility')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('lib', 'third_party')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('out')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('sample')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('src')
    gen(_document(), directory, sub, 'README.md')

'''DisabledContent
'''


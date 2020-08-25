#!/usr/bin/env false
"""Generate all Markdown documents."""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from src_gen.document.markdown.source import generate as gen
from src_gen.document.markdown.structure import *
# Co-located modules (relative references, NOT packaged, in project)


def _document():
    return [
        h1('TODO'),
    ]

def _generate_BriteOnyx(directory):
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

def _generate_bin(directory):
    sub = Path('bin')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('bin', 'lib')
    gen(_document(), directory, sub, 'README.md')

def _generate_home(directory):
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

def _generate_others(directory):
    sub = Path('cfg')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('cfg', 'sample')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('doc')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('out')
    gen(_document(), directory, sub, 'README.md')

def _generate_project(directory):
    sub = Path('.')
    gen(_document(), directory, sub, 'README.md')
    gen(_document(), directory, sub, 'TODO.md')

def _generate_src(directory):
    sub = Path('src')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('src', 'app')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('src', 'gen')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('src', 'lib')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('src', 'lib', 'mine')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('src', 'lib', 'mine', 'src_gen')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('src', 'lib', 'mine', 'throw_out_your_templates')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('src', 'lib', 'mine', 'utility')
    gen(_document(), directory, sub, 'README.md')
    sub = Path('src', 'lib', 'third_party')
    gen(_document(), directory, sub, 'README.md')

def generate(directory):
    _generate_BriteOnyx(directory)
    _generate_bin(directory)
    _generate_home(directory)
    _generate_others(directory)
    _generate_project(directory)
    _generate_src(directory)

'''DisabledContent
'''


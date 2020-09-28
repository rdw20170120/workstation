#!/usr/bin/env false
"""Generate script to set PATH."""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from src_gen.script.bash.briteonyx.source import generate as gen
from src_gen.script.bash.briteonyx.structure import *
# Co-located modules (relative references, NOT packaged, in project)


def _comments():
    return [
        comment('Set PATH for project'),
        comment(),
        note('This specific ordering of PATH elements is REQUIRED.'),
        comment('The Python virtual environment MUST come first'),
        comment('in order to override the system Python.'),
        comment('For now,'),
        comment('that PATH element also includes the system PATH element,'),
        comment('which is repeated here for when that is eventually fixed.'),
        comment('The system PATH element MUST precede any user PATH elements'),
        comment('in order to make collisions fail-fast'),
        comment('and'),
        comment('to defeat simple attempts at redirecting system commands'),
        comment('as an attack vector.'),
        comment('Similarly,'),
        comment('the project PATH element MUST precede the user PATH element'),
        comment('in order to make collisions fail-fast.'),
        comment('This arrangement is best for ensuring consistent behavior'),
        comment('of the Python virtual environment, the system, and the project.'),
        comment('It puts at-risk only those user-specific commands, tools, and scripts'),
        comment('relevant to the current deployed environment'),
        comment('--where the specific user is best positioned to address them'),
        comment('and failures are most likely limited to affecting only them (as they should).'),
        _remember_path(),
    ]

# TODO: SOMEDAY: Rearrange PATH
# so that the Python virtual environment directory is first,
# followed by the system directories,
# the project 'bin' directory is last,
# links are replaced by the linked directory,
# and duplicates are removed
# while preserving the order of the system directories.
def _remember_path():
    return [
        line(),
        export(vn('PATH'), (
            # PVE path must precede system path to override Python
            vr('BO_PathPve'),
            ':', vr('BO_PathSystem'),
            ':', vr('BO_PathProject'),
            ':', vr('BO_PathUser')
        )), eol(),
        echo_info(
            'Remembering ', sq(vn('PATH')), ' as ', sq(vr('PATH'))
        ), eol(),
    ]

def build():
    return [
        sourced_header(),
        _comments(),
        disabled_content_footer(),
    ]

def generate(directory):
    sub = Path('BriteOnyx', 'bin', 'lib')
    gen(build(), directory, sub, 'set_path.bash')

'''DisabledContent
'''

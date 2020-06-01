from .tavis_rudd.throw_out_your_templates.section_3 import VisitorMap

from .template.briteonyx_script    import BriteOnyxScript
from .template.briteonyx_script    import visitor_map as parent_visitor_map
from .template.briteonyx_structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _abort_if_activated():
    return [
        line(),
        if_(
            string_is_not_null(vr('BO_Project')),
            indent(), echo_fatal(
                'This project is already activated as ',
                sq(vr('BO_Project')),
                ', aborting'
            ), eol(),
            indent(), return_(1), '  ', comment(
                'Exit from the script, but not from the shell'
            ),
        ),
        fi(),
    ]

def _activate_python_virtual_environment():
    return [
        _remember_project_path(),
        _remember_system_path(),
        _remember_user_path(),
        _reset_path_for_pve(),
        _capture_environment(vr('PWD'), 'PVE-prior'), eol(),
        line(),
        _source_script((vr('BO_Project'), '/bin/lib/pve-activate.bash')),
        _capture_environment(vr('PWD'), 'PVE-after'), eol(),
        _remember_pve_path(),
        _remember_path(),
    ]

def _capture_environment(directory_name, file_name):
    return [
        line(),
        command('env'),
        pipe(),
        command('sort', '>', directory_name, '/BO-', file_name, '.env'),
    ]

def _comments():
    return [
        note(
            'We MUST NOT EVER ',
            sq(exit()),
            ' during BriteOnyx bootstrap or activation'
        ),
        no(set_('-e')),
        disabled(set_('-x')),
        rule(),
        # TODO: Redesign to automatically wrap comment paragraphs at a set line length
        comment('Activate the BriteOnyx framework to manage this project directory tree'),
        comment(),
        note('This script, and EVERY script that it calls, must NOT invoke ', sq(exit()), '!'),
        comment('The user calling this script must be allowed to preserve their shell and'),
        comment('every effort must be made to inform the user of problems while continuing'),
        comment('execution where possible.  Terminating the shell robs the user of useful'),
        comment('feedback and interrupts their work, which is unacceptable.  Instead, the BASH'),
        comment(sq(return_()), ' statement should be invoked to end execution with an appropriate'),
        comment('status code.'),
        rule(),
    ]

def _create_random_tmpdir():
    local = 'dir'
    # TODO: Consider capturing this special variable
    tmpdir = 'TMPDIR'
    user = 'USER'
    return [
        line(),
        comment('Create random temporary directory'),
        # TODO: Consider creating method for 'mktemp'
        if_(
            string_equals(vr('BO_OS'), 'macOS'),
            indent(), assign(
                vn(local),
                substitute('mktemp', '-d', '-t', dq('BO-', vr(user)))
            ), eol(),
        ),
        else_(
            indent(), todo('FIX: for Linux'),
            indent(), assign(
                vn(local),
                substitute(
                    'mktemp', '-d', '-t', dq('BO-', vr(user), '-XXXXXXX')
                )
            ), eol(),
        ),
        fi(),
        if_(
            directory_exists(vr(local)),
            indent(), assign(vn(tmpdir), vr(local)), eol(),
            indent(), echo_info(
                'Temporary directory ', sq(vr(tmpdir)), ' created'
            ), eol(),
        ),
        fi(),
        if_(
            directory_exists(vr(tmpdir)),
            indent(), echo_info(
                'Remembering ', vn(tmpdir), '=', sq(vr(tmpdir))
            ), eol(),
            indent(), export(vn(tmpdir)), eol(),
        ),
        else_(
            indent(), echo_fatal(
                'Failed to establish temporary directory ',
                sq(vr(tmpdir)),
                ', aborting'
            ), eol(),
            indent(), return_(1), '  ', comment(
                'Exit from the script, but not from the shell'
            ),
        ),
        fi(),
    ]

def _detect_operating_system():
    # TODO: Make appropriate constants
    local = 'dir'
    return [
        line(),
        comment('Detect operating system'),
        assign(vn(local), substitute('uname')), eol(),
        if_(
            string_equals(vr(local), 'Darwin'),
            indent(), export(vn('BO_OS'), 'macOS'), eol(),
        ),
        else_(
            indent(), export(vn('BO_OS'), 'Linux'), eol(),
        ),
        fi(),
        echo_info('Remembering ', vn('BO_OS'), '=', sq(vr('BO_OS'))), eol(),
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

def _reset_path_for_pve():
    return [
        line(),
        comment('Reset PATH before activating Python virtual environment'),
        export(vn('PATH'), vr('BO_PathSystem')), eol(),
    ]

def _remember_project_path():
    return [
        line(),
        export(vn('BO_PathProject'), (vr('BO_Project'), '/bin')), eol(),
        echo_info(
            'Remembering ', vn('BO_PathProject'), '=', vr('BO_PathProject')
        ), eol(),
    ]

def _remember_project_root():
    return [
        line(),
        echo_info(
            'Activating this directory ', sq(vr('PWD')), ' as the current project'
        ), eol(),
        export(vn('BO_Project'), vr('PWD')), eol(),
    ]

def _remember_pve_path():
    return [
        line(),
        string_is_null(vr('BO_PathPve')), and_(), bs(),
        indent(), export(vn('BO_PathPve'), vr('PATH')), and_(), bs(),
        indent(), echo_info(
            'Remembering ', vn('BO_PathPve'), '=', sq(vr('BO_PathPve'))
        ), eol(),
    ]

def _remember_system_path():
    return [
        line(),
        string_is_null(vr('BO_PathSystem')), and_(), bs(),
        indent(), export(vn('BO_PathSystem'), vr('PATH')), and_(), bs(),
        indent(), echo_info(
            'Remembering ', vn('BO_PathSystem'), '=', sq(vr('BO_PathSystem'))
        ), eol(),
    ]

def _remember_user_path():
    return [
        line(),
        string_is_null(vr('BO_PathUser')), and_(), bs(),
        indent(), export(vn('BO_PathUser'), (vr('HOME'), '/bin')), and_(), bs(),
        indent(), echo_info(
            'Remembering ', vn('BO_PathUser'), '=', sq(vr('BO_PathUser'))
        ), eol(),
    ]

# TODO: Make this reusable
def _source_script(script):
    return [
        assign(vn('Script'), script), eol(),
        if_(
            file_is_readable(vr('Script')),
            indent(), echo_info(
                sq('source'), 'ing script file ', sq(vr('Script'))
            ), eol(),
            indent(), source(vr('Script')), eol(),
        ),
        else_(
            indent(), echo_warn(
                'Script file ', sq(vr('Script')), ' is not readable, ignoring'
            ), eol(),
        ),
        fi(
        ),
    ]

def _source_supporting_scripts():
    return [
        line(),
        _source_script((vr('BO_Project'), '/alias-git.bash')),
        line(),
        _source_script((vr('BO_Project'), '/alias-project.bash')),
        line(),
        _source_script((vr('BO_Project'), '/context.bash')),
    ]

def build():
    return [
        sourced_header(),
        _comments(),
        _abort_if_activated(),
        _capture_environment(vr('PWD'), 'incoming'), eol(),
        _remember_project_root(),
        _detect_operating_system(),
        _create_random_tmpdir(),
        _activate_python_virtual_environment(),
        _source_supporting_scripts(),
        _capture_environment(vr('PWD'), 'outgoing'), eol(),
        disabled_content_footer(),
    ]

def generate(target_directory):
    content = BriteOnyxScript(build(),
        Path(), 'activate.bash'
        )
    content.generate(target_directory)
    content.print()


''' Disabled content
'''


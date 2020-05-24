from tavis_rudd.throw_out_your_templates.section_3 import VisitorMap

from .template                     import briteonyx_script
from .template.briteonyx_structure import *

def _abort_if_activated():
    return [
        line(),
        if_(
            string_is_not_null(vr('BO_Project')),
            indent(), echo_fatal(
                'This project is already activated as ', sq(vr('BO_Project')), ', aborting'
            ), eol(),
            indent(), return_(1), '  ', comment('Exit from the script, but not from the shell'),
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
        _source_script((vr('BO_Project'), '/bin/lib/pve-activate')),
        _capture_environment(vr('PWD'), 'PVE-after'), eol(),
        _remember_pve_path(),
        _remember_path(),
    ]

def _capture_environment(directory_name, file_name):
    return [
        line(),
        command('env'),
        pipe(),
        command('sort', '>', path(directory_name, 'BO-' + file_name + '.env')),
    ]

def _comments():
    return [
        note('We MUST NOT EVER ', sq(exit()), ' during BriteOnyx bootstrap or activation'),
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
        comment(sq(return_()), ' statement should be invoked to end execution with an'),
        comment('appropriate status code.'),
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
        todo('This is macOS syntax.  Also address Ubuntu syntax.'),
        assign(vn(local), substitute('mktemp', '-d', '-t', dq('BO-', vr(user)))), eol(),
        if_(
            directory_exists(vr(local)),
            indent(), assign(vn(tmpdir), vr(local)), eol(),
            indent(), echo_info('Temporary directory ', sq(vr(tmpdir)), ' created'), eol(),
        ),
        fi(),
        if_(
            directory_exists(vr(tmpdir)),
            indent(), echo_info('Remembering ', vn(tmpdir), '=', sq(vr(tmpdir))), eol(),
            indent(), export(vn(tmpdir)), eol(),
        ),
        else_(
            indent(), echo_fatal('Failed to establish temporary directory ', sq(vr(tmpdir)), ', aborting'), eol(),
            indent(), return_(1), '  ', comment('Exit from the script, but not from the shell'),
        ),
        fi(),
    ]

# TODO: SOMEDAY: Rearrange PATH
# so that system directories are first
# followed by the Python virtual environment directory,
# the project 'bin' directory is last,
# links are replaced by the linked directory,
# and duplicates are removed
# while preserving the order of the system directories.
def _remember_path():
    return [
        line(),
        export(vn('PATH'), (
            vr('BO_PathSystem'),
            ':', vr('BO_PathPve'),
            ':', vr('BO_PathProject'),
            ':', vr('BO_PathUser')
        )), eol(),
        echo_info('Remembering ', sq(vn('PATH')), ' as ', sq(vr('PATH'))), eol(),
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
        echo_info('Remembering ', vn('BO_PathProject'), '=', vr('BO_PathProject')), eol(),
    ]

def _remember_project_root():
    return [
        line(),
        echo_info('Activating this directory ', sq(vr('PWD')), ' as the current project'), eol(),
        export(vn('BO_Project'), vr('PWD')), eol(),
    ]

def _remember_pve_path():
    return [
        line(),
        string_is_null(vr('BO_PathPve')), and_(), bs(),
        indent(), export(vn('BO_PathPve'), vr('PATH')), and_(), bs(),
        indent(), echo_info('Remembering ', vn('BO_PathPve'), '=', sq(vr('BO_PathPve'))), eol(),
    ]

def _remember_system_path():
    return [
        line(),
        string_is_null(vr('BO_PathSystem')), and_(), bs(),
        indent(), export(vn('BO_PathSystem'), vr('PATH')), and_(), bs(),
        indent(), echo_info('Remembering ', vn('BO_PathSystem'), '=', sq(vr('BO_PathSystem'))), eol(),
    ]

def _remember_user_path():
    return [
        line(),
        string_is_null(vr('BO_PathUser')), and_(), bs(),
        indent(), export(vn('BO_PathUser'), (vr('HOME'), '/bin')), and_(), bs(),
        indent(), echo_info('Remembering ', vn('BO_PathUser'), '=', sq(vr('BO_PathUser'))), eol(),
    ]

# TODO: Make this reusable
def _source_script(script):
    return [
        assign(vn('Script'), script), eol(),
        if_(
            file_is_readable(vr('Script')),
            indent(), source(vr('Script')), eol(),
            indent(), echo_info('Sourced script file ', sq(vr('Script'))), eol(),
        ),
        else_(
            indent(), echo_warn('Script file ', sq(vr('Script')), ' is not readable, ignoring'), eol(),
        ),
        fi(
        ),
    ]

def _source_supporting_scripts():
    return [
        line(),
        _source_script((vr('BO_Project'), '/alias-git')),
        line(),
        _source_script((vr('BO_Project'), '/alias-project')),
        line(),
        _source_script((vr('BO_Project'), '/context')),
    ]

def _build():
    return briteonyx_script.BriteOnyxScript([
        sourced_header(),
        _comments(),
        _abort_if_activated(),
        _capture_environment(vr('PWD'), 'incoming'), eol(),
        _remember_project_root(),
        _create_random_tmpdir(),
        _activate_python_virtual_environment(),
        _source_supporting_scripts(),
        _capture_environment(vr('PWD'), 'outgoing'), eol(),
        disabled_content_footer(),
    ])


visitor_map = VisitorMap(parent_map=briteonyx_script.visitor_map)

def render(parent_directory, filename='activate', content=None, visitor_map=visitor_map):
    assert content is None
    content = _build()
    briteonyx_script.render(parent_directory, filename, content, visitor_map)


""" Disabled content

def _capture_incoming_environment():
    return [
        line(),
        comment('Capture incoming BASH environment'),
        if_(
            string_is_not_null(vr('TMPDIR')),
            indent(), _capture_environment(vr('TMPDIR'), 'BO-env-incoming.out'), eol(),
        ),
        elif_(
            string_is_not_null(vr('BO_Project')),
            indent(), _capture_environment(vr('BO_Project'), 'BO-env-incoming.out'), eol(),
        ),
        else_(
            indent(), _capture_environment(vr('PWD'), 'BO-env-incoming.out'), eol(),
        ),
        fi(),
    ]

def _capture_outgoing_environment():
    return [
        line(),
        comment('Capture outgoing BASH environment'),
        if_(
            string_is_not_null(vr('TMPDIR')),
            indent(), _capture_environment(vr('TMPDIR'), 'BO-env-outgoing.out'), eol(),
        ),
        elif_(
            string_is_not_null(vr('BO_Project')),
            indent(), _capture_environment(vr('BO_Project'), 'BO-env-outgoing.out'), eol(),
        ),
        else_(
            indent(), _capture_environment(vr('PWD'), 'BO-env-outgoing.out'), eol(),
        ),
        fi(),
    ]

def demonstrate_logging():
    return [
        line(),
        rule(),
        comment('Demonstrate logging'),
        line(),
        log_debug('EXAMPLE: This is a debugging message'), eol(),
        log_info('EXAMPLE: This is an informational message'), eol(),
        log_warn('EXAMPLE: This is a warning message'), eol(),
        log_error('EXAMPLE: This is an error message'), eol(),
        log_fatal('"EXAMPLE: This is a fatal message'), eol(),
    ]

def initialize_logging_file():
    return [
        line(),
        comment('Initialize BriteOnyx logging file'),
        assign(vn('BO_FileLog'), 'BO.log'), eol(),
        if_(
            string_is_not_null(vr('TMPDIR')),
            indent(), export(vn('BO_FileLog'), path(vr('TMPDIR'), vr('BO_FileLog'))), eol(),
        ),
        elif_(
            string_is_not_null(vr('BO_Project')),
            indent(), export(vn('BO_FileLog'), path(vr('BO_Project'), vr('BO_FileLog'))), eol(),
        ),
        else_(
            indent(), export(vn('BO_FileLog'), path(vr('PWD'), vr('BO_FileLog'))), eol(),
        ),
        fi(),
        echo_info('Activating...'), ' >', vr('BO_FileLog'), eol(),
        echo_info('Activating the BriteOnyx framework for this project...'), eol(),
        echo_warn("This script MUST be executed as 'source activate.src', WAS IT?"), eol(),
    ]

def normalize_reference_to_project_root():
    return [
        line(),
        require_variable(sq(vn('BO_Project'))),
        or_(),
        failed(),
        or_(),
        return_last_status(), eol(),
        trace_variable(sq(vn('BO_Project'))), eol(),
        export(vn('BO_Project'), dq(substitute('boNodeCanonical', vr('BO_Project')))), eol(),
        trace_variable(sq(vn('BO_Project'))), eol(),
        bo_log_info(
            'Canonical form of ',
            vn('BO_Project'),
            ' directory pathname is ',
            sq(vr('BO_Project')),
        ), eol(),
        require_directory(vr('BO_Project')),
        or_(),
        failed(),
        or_(),
        return_last_status(), eol(),
    ]

def _remember_project_root():
    return [
        line(),
        rule(),
        comment('Remember the directory containing this script as our project root'),
        line(),
        export(vn('BO_Project'), dq(substitute('dirname', vr('BASH_SOURCE')))), eol(),
        line(),
        todo('REVIEW: Shall we NOT cd into our project directory since it changes'),
        comment("the caller's execution environment?"),
        comment(command('cd', dq(path(vr('BO_Project')))), or_(), return_last_status()),
    ]

##########

        rule(),
        debugging_comment(),
        someday('Add inverse commands to isolate debugging'),
        line(),

##########

        comment(),
        someday(
            'Verify that ',
            vr('BO_Project'),
            ' does indeed point to the root of our project directory tree',
        ),

"""


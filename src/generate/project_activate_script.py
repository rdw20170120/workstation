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


def _comments():
    return [
        note("We MUST NOT EVER 'exit' during BriteOnyx bootstrap or activation"),
        rule(),
        comment('Activate the BriteOnyx framework to manage this project directory tree'),
        comment(),
        note("This script, and EVERY script that it calls, must NOT invoke 'exit'!  The user calling this"),
        comment('  script must be allowed to preserve their shell and every effort must be made to inform the user'),
        comment('  of problems while continuing execution where possible.  Terminating the shell robs the user of'),
        comment("  useful feedback and interrupts their work, which is unacceptable.  Instead, the BASH 'return'"),
        comment('  statement should be invoked to end execution with an appropriate status code.'),
        rule(),
    ]

def _capture_environment(directory_name, file_name):
    return [
        command('env'),
        pipe(),
        command('sort', '>', path(directory_name, file_name)),
    ]

def _create_random_tmpdir():
    # TODO: Consider capturing this special variable
    home = 'HOME'
    local = 'dir'
    # TODO: Consider capturing this special variable
    tmpdir = 'TMPDIR'
    # TODO: Consider capturing this special variable
    user = 'USER'
    return [
        line(),
        assign(vn(tmpdir), '/tmp'), eol(),
        string_is_not_null(vr(user)), and_(), assign(vn(tmpdir), '/tmp/', vr(user)), eol(),
        string_is_not_null(vr(home)), and_(), assign(vn(tmpdir), vr(home), '/tmp'), eol(),
        comment('Create random temporary directory'),
        # TODO: Consider creating method for 'mktemp'
        assign(vn(local), substitute('mktemp', '--tmpdir', '-d', 'BO-XXXXXXXX')), eol(),
        directory_exists(vr(local)), and_(), assign(vn('TMPDIR'), vr(local)), eol(),
        if_(
            path_does_not_exist(vr(tmpdir)),
            indent(), command('mkdir', vr(tmpdir)), eol(),
            indent(), echo_info('Temporary directory ', sq(vr(tmpdir)), ' created'), eol(),
        ),
        elif_(
            path_is_not_directory(vr(tmpdir)),
            indent(), echo_fatal('Path ', sq(vr(tmpdir)), ' is NOT a (temporary) directory, aborting'), eol(),
            indent(), return_(1), '  ', comment('Exit from the script, but not from the shell'),
        ),
        fi(),
        if_(
            directory_exists(vr(tmpdir)),
            indent(), echo_info('Temporary directory ', sq(vr(tmpdir)), ' remembered'), eol(),
            indent(), export(vn(tmpdir)), eol(),
        ),
        else_(
            indent(), echo_fatal('Failed to establish temporary directory ', sq(vr(tmpdir)), ', aborting'), eol(),
            indent(), return_(1), '  ', comment('Exit from the script, but not from the shell'),
        ),
        fi(),
    ]

def _remember_path():
    return [
        line(),
        rule(),
        comment('Remember ', vn('PATH')),
        line(),
        string_is_null(vr('BO_PathSystem')),
        and_(), nl(),
        '  ',
        export(vn('BO_PathSystem'), vr('PATH')),
        and_(), nl(),
        '  ',
        echo_info('Remembering ', vn('BO_PathSystem'), '=', sq(vr('BO_PathSystem'))), eol(),
    ]

def _remember_project_root():
    return [
        line(),
        echo_info('Activating this directory ', sq(vr('PWD')), ' as the current project'), eol(),
        export(vn('BO_Project'), vr('PWD')), eol(),
    ]

def _build():
    return briteonyx_script.BriteOnyxScript([
        sourced_header(),
        _comments(),
        _abort_if_activated(),
#       _capture_incoming_environment(),
        line(),
        comment('Capture incoming BASH environment'),
        '  ', _capture_environment(vr('PWD'), 'BO-env-incoming.out'), eol(),
        _create_random_tmpdir(),
        _remember_project_root(),
#       initialize_logging_file(),
#       normalize_reference_to_project_root(),
#       configure_for_user(),
#       configure_for_project(),
#       configure_for_briteonyx(),
#       verify_briteonyx_bootstrap(),
        _remember_path(),
#       activate_for_linux(),
#       set_tmpdir(),
#       declare_for_project(),
#       demonstrate_logging(),
#       shutdown(),
        line(),
        comment('Capture outgoing BASH environment'),
        '  ', _capture_environment(vr('PWD'), 'BO-env-outgoing.out'), eol(),
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
            '  ',
            _capture_environment(vr('TMPDIR'), 'BO-env-incoming.out'), eol(),
        ),
        elif_(
            string_is_not_null(vr('BO_Project')),
            '  ',
            _capture_environment(vr('BO_Project'), 'BO-env-incoming.out'), eol(),
        ),
        else_(
            '  ',
            _capture_environment(vr('PWD'), 'BO-env-incoming.out'), eol(),
        ),
        fi(),
    ]

def _capture_outgoing_environment():
    return [
        line(),
        comment('Capture outgoing BASH environment'),
        if_(
            string_is_not_null(vr('TMPDIR')),
            '  ',
            _capture_environment(vr('TMPDIR'), 'BO-env-outgoing.out'), eol(),
        ),
        elif_(
            string_is_not_null(vr('BO_Project')),
            '  ',
            _capture_environment(vr('BO_Project'), 'BO-env-outgoing.out'), eol(),
        ),
        else_(
            '  ',
            _capture_environment(vr('PWD'), 'BO-env-outgoing.out'), eol(),
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
            '  ',
            export(vn('BO_FileLog'), path(vr('TMPDIR'), vr('BO_FileLog'))), eol(),
        ),
        elif_(
            string_is_not_null(vr('BO_Project')),
            '  ',
            export(vn('BO_FileLog'), path(vr('BO_Project'), vr('BO_FileLog'))), eol(),
        ),
        else_(
            '  ',
            export(vn('BO_FileLog'), path(vr('PWD'), vr('BO_FileLog'))), eol(),
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
        ),
        eol(),
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


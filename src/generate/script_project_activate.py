from tavis_rudd.throw_out_your_templates.section_3 import VisitorMap

from .                    import script_briteonyx
from .structure_briteonyx import *

def abort_if_activated():
    return [
        line(),
        rule(),
        note('ABORT: if project is already activated'),
        string_is_not_null(vr('BO_Project')),
        and_(),
        echo_fatal('Project ', sq(vr('BO_Project')), ' is already activated, aborting'),
        and_(),
        exit(100), eol(),
    ]

def comments():
    return [
        note("We MUST NOT EVER 'exit' during BriteOnyx bootstrap or activation"),
        rule(),
        debugging_comment(),
        someday('Add inverse commands to isolate debugging'),
        line(),
        rule(),
        comment('Activate the BriteOnyx framework to manage this project directory tree'),
        comment(),
        note("This script, and EVERY script that it calls, must NOT invoke 'exit'!  The user calling this"),
        comment('  script must be allowed to preserve their shell and every effort must be made to inform the user'),
        comment('  of problems while continuing execution where possible.  Terminating the shell robs the user of'),
        comment("  useful feedback and interrupts their work, which is unacceptable.  Instead, the BASH 'return'"),
        comment('  statement should be invoked to end execution with an appropriate status code.'),
        comment(),
        someday(
            'Verify that ',
            vr('BO_Project'),
            ' does indeed point to the root of our project directory tree',
        ),
    ]

def capture_environment(directory_name, file_name):
    return [
        command('env'),
        pipe(),
        command('sort', '>', path(directory_name, file_name)),
    ]

def capture_incoming_environment():
    return [
        line(),
        comment('Capture incoming BASH environment'),
        if_(
            string_is_not_null(vr('TMPDIR')),
            '  ',
            capture_environment(vr('TMPDIR'), 'BO-env-incoming.out'), eol(),
        ),
        elif_(
            string_is_not_null(vr('BO_Project')),
            '  ',
            capture_environment(vr('BO_Project'), 'BO-env-incoming.out'), eol(),
        ),
        else_(
            '  ',
            capture_environment(vr('PWD'), 'BO-env-incoming.out'), eol(),
        ),
        fi(),
    ]

def capture_outgoing_environment():
    return [
        line(),
        comment('Capture outgoing BASH environment'),
        if_(
            string_is_not_null(vr('TMPDIR')),
            '  ',
            capture_environment(vr('TMPDIR'), 'BO-env-outgoing.out'), eol(),
        ),
        elif_(
            string_is_not_null(vr('BO_Project')),
            '  ',
            capture_environment(vr('BO_Project'), 'BO-env-outgoing.out'), eol(),
        ),
        else_(
            '  ',
            capture_environment(vr('PWD'), 'BO-env-outgoing.out'), eol(),
        ),
        fi(),
    ]

def create_random_tmpdir():
    return [
        line(),
        comment('Create random ', vn('TMPDIR')),
        assign(vn('Dir'), substitute('mktemp', '--tmpdir', '-d', 'BO-XXXXXXXX')), eol(),
        directory_exists(vr('Dir')),
        and_(),
        export(vn('TMPDIR'), vr('Dir')), eol(),
    ]

def remember_path():
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

def remember_project_root():
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

def build():
    return script_briteonyx.BriteOnyxScript([
#       source_header(),
        comments(),
        abort_if_activated(),
        create_random_tmpdir(),
#       initialize_logging_file(),
        capture_incoming_environment(),
        remember_project_root(),
#       normalize_reference_to_project_root(),
#       configure_for_user(),
#       configure_for_project(),
#       configure_for_briteonyx(),
#       verify_briteonyx_bootstrap(),
        remember_path(),
#       activate_for_linux(),
#       set_tmpdir(),
#       declare_for_project(),
#       demonstrate_logging(),
#       shutdown(),
        disabled_content_footer(),
    ])
    

visitor_map = VisitorMap(parent_map=script_briteonyx.visitor_map)

def render(parent_directory, filename=None, content=None, visitor_map=visitor_map):
    assert content is None
    content = build()
    if filename is None: filename = 'activate'
    script_briteonyx.render(parent_directory, filename, content, visitor_map)


""" Disabled content
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

"""


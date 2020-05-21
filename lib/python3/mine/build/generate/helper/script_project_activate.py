import script_bash
import script_briteonyx

from throw_out_your_templates_3_core_visitor_map import VisitorMap

from structure_bash import *
from structure_briteonyx import *


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

def activate_for_linux():
    return [
        line(),
        rule(),
        comment('Activate as a Linux project'),
        line(),
        source_script(dq(path(vr('BO_Home'), 'helper', 'activation', 'activate.src'))),
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

def configure_for_briteonyx():
    return [
        line(),
        rule(),
        comment('Configure for BriteOnyx'),
        line(),
        source_script(dq(path(vr('BO_Project'), 'BriteOnyx', 'env.src'))),
    ]

def configure_for_project():
    return [
        line(),
        rule(),
        comment('Configure for this project'),
        line(),
        source_script(path(vr('BO_Project'), 'env.src')),
    ]

def configure_for_user():
    return [
        line(),
        rule(),
        comment('Configure for this user'),
        line(),
        source_script(path(vr('HOME'), '.BriteOnyx.src')),
    ]

def copy_starter_files():
    return [
        line(),
        rule(),
        comment('Copy starter files into place as necessary'),
        line(),
        assign(vn('DirSrc'), path(vr('BO_Project'), 'BriteOnyx', 'starter')), eol(),
        line(),
        require_variable(vn('HOME')), eol(),
        assign(vn('DirTgt'), vr('HOME')), eol(),
        path_does_not_exist(vr('DirTgt')), and_(),
        command('mkdir', '-p', vr('DirTgt')), eol(),
        line(),
        assign(vn('FileTgt'), path(vr('DirTgt'), '.BriteOnyx.src')), eol(),
        comment('Move previous scripts to new path'),
        file_exists(path(vr('DirTgt'), 'BriteOnyx.src')),
        and_(),
        command('mv', path(vr('DirTgt'), 'BriteOnyx.src'), vr('FileTgt')), eol(),
        file_exists(path(vr('DirTgt'), 'BriteOnyx-env.bash')),
        and_(),
        command('mv', path(vr('DirTgt'), 'BriteOnyx-env.bash'), vr('FileTgt')), eol(),
        file_exists(path(vr('DirTgt'), 'BriteOnyx-env.src')),
        and_(),
        command('mv', path(vr('DirTgt'), 'BriteOnyx-env.src'),  vr('FileTgt')), eol(),
        comment('Copy starter script, if necessary'),
        path_is_not_file(vr('FileTgt')),
        and_(),
        command('cp', path(vr('DirSrc'), 'user-BriteOnyx.src'), vr('FileTgt')), eol(),
        line(),
        assign(vn('DirTgt'), path(vr('BO_Project'))), eol(),
        path_does_not_exist(vr('DirTgt')),
        and_(),
        command('mkdir', '-p', vr('DirTgt')), eol(),
        line(),
        assign(vn('FileTgt'), path(vr('DirTgt'), 'env.src')), eol(),
        path_is_not_file(vr('FileTgt')),
        and_(),
        command('cp', path(vr('DirSrc'), 'project-env.src'), vr('FileTgt')), eol(),
        line(),
        assign(vn('FileTgt'), path(vr('DirTgt'), '.hgignore')), eol(),
        path_is_not_file(vr('FileTgt')),
        and_(),
        command('cp', path(vr('DirSrc'), 'project.hgignore'), vr('FileTgt')), eol(),
        line(),
        assign(vn('DirTgt'), path(vr('BO_Project'), 'bin')), eol(),
        path_does_not_exist(vr('DirTgt')),
        and_(),
        command('mkdir', '-p', vr('DirTgt')), eol(),
        line(),
        assign(vn('FileTgt'), path(vr('DirTgt'), 'project-fix-permissions.bash')), eol(),
        comment('Move previous scripts to new path'),
        file_exists(path(vr('DirTgt'), 'all-fix-permissions.bash')),
        and_(),
        command('mv', path(vr('DirTgt'), 'all-fix-permissions.bash'), vr('FileTgt')), eol(),
        comment('Copy starter script, if necessary'),
        path_is_not_file(vr('FileTgt')),
        and_(),
        command('cp', path(vr('DirSrc'), 'project-fix-permissions.bash'), vr('FileTgt')), eol(),
        line(),
        line(": <<'DisabledContent'"),
        assign(vn('FileTgt'), path(vr('DirTgt'), 'declare.src')), eol(),
        path_is_not_file(vr('FileTgt')),
        and_(),
        command('cp', path(vr('DirSrc'), 'project-declare.src'), vr('FileTgt')), eol(),
        line(),
        assign(vn('FileTgt'), path(vr('DirTgt'), 'development.rst')), eol(),
        path_is_not_file(vr('FileTgt')),
        and_(),
        command('cp', path(vr('DirSrc'), 'project-development.rst'), vr('FileTgt')), eol(),
        line(),
        assign(vn('FileTgt'), path(vr('DirTgt'), 'README.rst')), eol(),
        path_is_not_file(vr('FileTgt')),
        and_(),
        command('cp', path(vr('DirSrc'), 'project-README.rst'), vr('FileTgt')), eol(),
        line(),
        assign(vn('DirTgt'), path(vr('BO_Project'), 'bin', 'helper', 'Linux')), eol(),
        path_does_not_exist(vr('DirTgt')),
        and_(),
        command('mkdir', '-p', vr('DirTgt')), eol(),
        line(),
        assign(vn('FileTgt'), path(vr('DirTgt'), 'declare-BASH.src')), eol(),
        path_is_not_file(vr('FileTgt')),
        and_(),
        command('cp', path(vr('DirSrc'), 'project-declare-BASH.src'), vr('FileTgt')), eol(),
        line('DisabledContent'),
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

def declare_for_bootstrap():
    return [
        line(),
        rule(),
        comment('Declare BriteOnyx support functionality'),
        line(),
        assign(vn('Script'), dq(path(vr('BO_Project'), 'BriteOnyx', 'declare.src'))), eol(),
        path_is_not_file(vr('Script')),
        and_(),
        echo_fatal('Missing script ', sq(vr('Script'))),
        and_(),
        return_(63), eol(),
        source(dq(vr('Script'))), seq(), remember_status(), eol(),
        status_is_failure(), and_(), report_status(), and_(), return_status(), eol(),
        line(),
        rule(),
        note('Now that we have our support functionality declared, we can use it from here on'),
    ]

def declare_for_project():
    return [
        line(),
        rule(),
        comment('Declare optional project functionality'),
        line(),
        assign(vn('Script'), dq(path(vr('BO_Project'), 'declare.src'))), eol(),
        if_(
            file_exists(vr('Script')),
            '  ',
            source(dq(vr('Script'))), seq(), remember_status(), eol(),
            '  ',
            status_is_failure(), and_(), report_status(), and_(), return_status(), eol(),
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

def set_tmpdir():
    return [
        line(),
        rule(),
        comment('Set ', vn('TMPDIR'), ' '),
        comment('DISABLED: MOVED: to Linux activation script'),
        line(),
        comment(export(vn('TMPDIR'), path(vr('TMPDIR'), vr('BO_ProjectName')))),
        comment(echo_info('Remembering ', vn('TMPDIR'), '=', sq(vr('TMPDIR')))),
    ]

def shutdown():
    return [
        line(),
        rule(),
        comment('Shutdown'),
        line(),
        log_info(
            'Project ',
            sq(vr('BO_ProjectName')),
            ' in directory ',
            sq(vr('BO_Project')),
            ' is now activated, done.',
        ),
        eol(),
        capture_outgoing_environment(),
    ]

def verify_briteonyx_bootstrap():
    return [
        line(),
        rule(),
        comment('Verify BriteOnyx bootstrap configuration'),
        line(),
        require_variable(vn('BO_Home')),
        or_(),
        failed(),
        or_(),
        return_last_status(), eol(),
        require_directory(vr('BO_Home')),
        or_(),
        failed(),
        or_(),
        return_last_status(), eol(),
        line(),
        require_variable(vn('BO_ProjectName')),
        or_(),
        failed(),
        or_(),
        return_last_status(), eol(),
    ]


class Script(script_briteonyx.Script):
    def __init__(self, content):
        script_briteonyx.Script.__init__(self)
        self._content = content


def build():
    return Script([
        source_header(),
        comments(),
        abort_if_activated(),
        create_random_tmpdir(),
        initialize_logging_file(),
        capture_incoming_environment(),
        remember_project_root(),
        declare_for_bootstrap(),
        normalize_reference_to_project_root(),
        copy_starter_files(),
        configure_for_user(),
        configure_for_project(),
        configure_for_briteonyx(),
        verify_briteonyx_bootstrap(),
        remember_path(),
        activate_for_linux(),
        set_tmpdir(),
        declare_for_project(),
        demonstrate_logging(),
        shutdown(),
        disabled_content_footer(),
    ])
    

VISITOR_MAP = VisitorMap(parent_map=script_briteonyx.VISITOR_MAP)


def render(target_directory, target_file):
    script_bash.render(build(), VISITOR_MAP, target_directory, target_file)


""" Disabled content
"""


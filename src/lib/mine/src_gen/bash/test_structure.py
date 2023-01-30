#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_
from src_gen.renderer import Renderer
from src_gen.bash.source import my_visitor_map
from src_gen.bash.structure import *

# Project modules   (relative references, NOT packaged, in project)


# NOTE: There is little value in testing "composed" methods,
# e.g., those consisting of 'return [...]'.
# TODO: Generate tests

s = Renderer(my_visitor_map)._serialize


def test_and_():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(and_()), " &&")
    with raises(TypeError):
        and_(None)


def test_assign():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        assign()
    assert is_.equal(s(assign(None)), "=")
    assert is_.equal(s(assign("")), "=")
    assert is_.equal(s(assign("Test")), "Test=")
    assert is_.equal(s(assign("Test", None)), "Test=")
    assert is_.equal(s(assign("Test", "")), "Test=")
    assert is_.equal(s(assign("Test", "123")), "Test=123")


def test_bs():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(bs()), "\\\n")
    with raises(TypeError):
        bs(None)


def test_directory_exists():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        directory_exists()
    assert is_.equal(s(directory_exists(None)), "[[ -d ]]")
    assert is_.equal(s(directory_exists("")), "[[ -d ]]")
    assert is_.equal(s(directory_exists("Test")), "[[ -d Test ]]")
    with raises(TypeError):
        directory_exists("Test", None)


def test_disabled():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(disabled()), "# DISABLED: \n")
    assert is_.equal(s(disabled(None)), "# DISABLED: \n")
    assert is_.equal(s(disabled("")), "# DISABLED: \n")
    assert is_.equal(s(disabled("Test")), "# DISABLED: Test\n")
    assert is_.equal(s(disabled("Test", None)), "# DISABLED: Test\n")
    assert is_.equal(s(disabled("Test", "")), "# DISABLED: Test\n")
    assert is_.equal(s(disabled("Test", "123")), "# DISABLED: Test123\n")


def test_echo():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(echo()), "echo")
    assert is_.equal(s(echo(None)), "echo")
    assert is_.equal(s(echo("")), "echo")
    assert is_.equal(s(echo("Test")), "echo Test")
    assert is_.equal(s(echo("Test", None)), "echo Test")
    assert is_.equal(s(echo("Test", "")), "echo Test")
    assert is_.equal(s(echo("Test", "123")), "echo Test 123")


def test_echo_debug():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(echo_debug()), '1>&2 echo "DEBUG: "')
    assert is_.equal(s(echo_debug(None)), '1>&2 echo "DEBUG: "')
    assert is_.equal(s(echo_debug("")), '1>&2 echo "DEBUG: "')
    assert is_.equal(s(echo_debug("Test")), '1>&2 echo "DEBUG: Test"')
    assert is_.equal(s(echo_debug("Test", None)), '1>&2 echo "DEBUG: Test"')
    assert is_.equal(s(echo_debug("Test", "")), '1>&2 echo "DEBUG: Test"')
    assert is_.equal(
        s(echo_debug("Test", "123")), '1>&2 echo "DEBUG: Test123"'
    )


def test_echo_error():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(echo_error()), '1>&2 echo "ERROR: "')
    assert is_.equal(s(echo_error(None)), '1>&2 echo "ERROR: "')
    assert is_.equal(s(echo_error("")), '1>&2 echo "ERROR: "')
    assert is_.equal(s(echo_error("Test")), '1>&2 echo "ERROR: Test"')
    assert is_.equal(s(echo_error("Test", None)), '1>&2 echo "ERROR: Test"')
    assert is_.equal(s(echo_error("Test", "")), '1>&2 echo "ERROR: Test"')
    assert is_.equal(
        s(echo_error("Test", "123")), '1>&2 echo "ERROR: Test123"'
    )


def test_echo_info():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(echo_info()), '1>&2 echo "INFO:  "')
    assert is_.equal(s(echo_info(None)), '1>&2 echo "INFO:  "')
    assert is_.equal(s(echo_info("")), '1>&2 echo "INFO:  "')
    assert is_.equal(s(echo_info("Test")), '1>&2 echo "INFO:  Test"')
    assert is_.equal(s(echo_info("Test", None)), '1>&2 echo "INFO:  Test"')
    assert is_.equal(s(echo_info("Test", "")), '1>&2 echo "INFO:  Test"')
    assert is_.equal(s(echo_info("Test", "123")), '1>&2 echo "INFO:  Test123"')


def test_echo_warn():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(echo_warn()), '1>&2 echo "WARN:  "')
    assert is_.equal(s(echo_warn(None)), '1>&2 echo "WARN:  "')
    assert is_.equal(s(echo_warn("")), '1>&2 echo "WARN:  "')
    assert is_.equal(s(echo_warn("Test")), '1>&2 echo "WARN:  Test"')
    assert is_.equal(s(echo_warn("Test", None)), '1>&2 echo "WARN:  Test"')
    assert is_.equal(s(echo_warn("Test", "")), '1>&2 echo "WARN:  Test"')
    assert is_.equal(s(echo_warn("Test", "123")), '1>&2 echo "WARN:  Test123"')


def test_elif_():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        elif_()
    with raises(AssertionError):
        elif_(None)
    with raises(AssertionError):
        elif_("")
    with raises(AssertionError):
        elif_("Test")
    with raises(AssertionError):
        elif_("Test", None)
    with raises(AssertionError):
        elif_("Test", "")
    assert is_.equal(s(elif_("Test", "123")), "elif Test ; then\n123")


def test_else_():
    # TODO: Break up tests into individual test methods
    with raises(AssertionError):
        else_()
    with raises(AssertionError):
        else_(None)
    with raises(AssertionError):
        else_("")
    assert is_.equal(s(else_("Test")), "else\nTest")
    assert is_.equal(s(else_("Test", None)), "else\nTest")
    assert is_.equal(s(else_("Test", "")), "else\nTest")
    assert is_.equal(s(else_("Test", "123")), "else\nTest123")


def test_exit():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(exit()), "exit")
    assert is_.equal(s(exit(None)), "exit")
    assert is_.equal(s(exit("")), "exit")
    assert is_.equal(s(exit("Test")), "exit Test")
    with raises(TypeError):
        exit("Test", None)


def test_export():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        export()
    assert is_.equal(s(export(None)), "export")
    assert is_.equal(s(export("")), "export")
    assert is_.equal(s(export("Test")), "export Test")
    assert is_.equal(s(export("Test", None)), "export Test")
    assert is_.equal(s(export("Test", "")), "export Test=")
    assert is_.equal(s(export("Test", "123")), "export Test=123")


def test_fi():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(fi()), "fi\n")
    with raises(TypeError):
        fi(None)


def test_file_exists():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        file_exists()
    assert is_.equal(s(file_exists(None)), "[[ -f ]]")
    assert is_.equal(s(file_exists("")), "[[ -f ]]")
    assert is_.equal(s(file_exists("Test")), "[[ -f Test ]]")
    with raises(TypeError):
        file_exists("Test", None)


def test_file_is_readable():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        file_is_readable()
    assert is_.equal(s(file_is_readable(None)), "[[ -r ]]")
    assert is_.equal(s(file_is_readable("")), "[[ -r ]]")
    assert is_.equal(s(file_is_readable("Test")), "[[ -r Test ]]")
    with raises(TypeError):
        file_is_readable("Test", None)


def test_fix():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(fix()), "# TODO: FIX: \n")
    assert is_.equal(s(fix(None)), "# TODO: FIX: \n")
    assert is_.equal(s(fix("")), "# TODO: FIX: \n")
    assert is_.equal(s(fix("Test")), "# TODO: FIX: Test\n")
    assert is_.equal(s(fix("Test", None)), "# TODO: FIX: Test\n")
    assert is_.equal(s(fix("Test", "")), "# TODO: FIX: Test\n")
    assert is_.equal(s(fix("Test", "123")), "# TODO: FIX: Test123\n")


def test_if_():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        if_()
    with raises(AssertionError):
        if_(None)
    with raises(AssertionError):
        if_("")
    with raises(AssertionError):
        if_("Test")
    with raises(AssertionError):
        if_("Test", None)
    with raises(AssertionError):
        if_("Test", "")
    assert is_.equal(s(if_("Test", "123")), "if Test ; then\n123")


def test_indent():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(indent()), 4 * " ")
    with raises(TypeError):
        indent(None)
    assert is_.equal(s(indent(-1)), -1 * 4 * " ")
    assert is_.equal(s(indent(0)), 0 * 4 * " ")
    assert is_.equal(s(indent(1)), 1 * 4 * " ")
    assert is_.equal(s(indent(2)), 2 * 4 * " ")
    assert is_.equal(s(indent(9)), 9 * 4 * " ")


def test_integer_not_equal():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        integer_not_equal()
    with raises(TypeError):
        integer_not_equal(None)
    with raises(TypeError):
        integer_not_equal("")
    with raises(TypeError):
        integer_not_equal("Test")
    assert is_.equal(s(integer_not_equal(None, 123)), "[[ -ne 123 ]]")
    assert is_.equal(s(integer_not_equal("", 123)), "[[ -ne 123 ]]")
    assert is_.equal(s(integer_not_equal("Test", 123)), "[[ Test -ne 123 ]]")


def test_log_debug():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(log_debug()), 'log_debug ""')
    assert is_.equal(s(log_debug(None)), 'log_debug ""')
    assert is_.equal(s(log_debug("")), 'log_debug ""')
    assert is_.equal(s(log_debug("Test")), 'log_debug "Test"')
    assert is_.equal(s(log_debug("Test", None)), 'log_debug "Test"')
    assert is_.equal(s(log_debug("Test", "")), 'log_debug "Test"')
    assert is_.equal(s(log_debug("Test", "123")), 'log_debug "Test123"')


def test_log_error():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(log_error()), 'log_error ""')
    assert is_.equal(s(log_error(None)), 'log_error ""')
    assert is_.equal(s(log_error("")), 'log_error ""')
    assert is_.equal(s(log_error("Test")), 'log_error "Test"')
    assert is_.equal(s(log_error("Test", None)), 'log_error "Test"')
    assert is_.equal(s(log_error("Test", "")), 'log_error "Test"')
    assert is_.equal(s(log_error("Test", "123")), 'log_error "Test123"')


def test_log_good():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(log_good()), 'log_good ""')
    assert is_.equal(s(log_good(None)), 'log_good ""')
    assert is_.equal(s(log_good("")), 'log_good ""')
    assert is_.equal(s(log_good("Test")), 'log_good "Test"')
    assert is_.equal(s(log_good("Test", None)), 'log_good "Test"')
    assert is_.equal(s(log_good("Test", "")), 'log_good "Test"')
    assert is_.equal(s(log_good("Test", "123")), 'log_good "Test123"')


def test_log_info():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(log_info()), 'log_info ""')
    assert is_.equal(s(log_info(None)), 'log_info ""')
    assert is_.equal(s(log_info("")), 'log_info ""')
    assert is_.equal(s(log_info("Test")), 'log_info "Test"')
    assert is_.equal(s(log_info("Test", None)), 'log_info "Test"')
    assert is_.equal(s(log_info("Test", "")), 'log_info "Test"')
    assert is_.equal(s(log_info("Test", "123")), 'log_info "Test123"')


def test_log_warn():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(log_warn()), 'log_warn ""')
    assert is_.equal(s(log_warn(None)), 'log_warn ""')
    assert is_.equal(s(log_warn("")), 'log_warn ""')
    assert is_.equal(s(log_warn("Test")), 'log_warn "Test"')
    assert is_.equal(s(log_warn("Test", None)), 'log_warn "Test"')
    assert is_.equal(s(log_warn("Test", "")), 'log_warn "Test"')
    assert is_.equal(s(log_warn("Test", "123")), 'log_warn "Test123"')


def test_no():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(no()), "# NO: \n")
    assert is_.equal(s(no(None)), "# NO: \n")
    assert is_.equal(s(no("")), "# NO: \n")
    assert is_.equal(s(no("Test")), "# NO: Test\n")
    assert is_.equal(s(no("Test", None)), "# NO: Test\n")
    assert is_.equal(s(no("Test", "")), "# NO: Test\n")
    assert is_.equal(s(no("Test", "123")), "# NO: Test123\n")


def test_note():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(note()), "# NOTE: \n")
    assert is_.equal(s(note(None)), "# NOTE: \n")
    assert is_.equal(s(note("")), "# NOTE: \n")
    assert is_.equal(s(note("Test")), "# NOTE: Test\n")
    assert is_.equal(s(note("Test", None)), "# NOTE: Test\n")
    assert is_.equal(s(note("Test", "")), "# NOTE: Test\n")
    assert is_.equal(s(note("Test", "123")), "# NOTE: Test123\n")


def test_or_():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(or_()), " || ")
    with raises(TypeError):
        or_(None)


def test_path_not_exists():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        path_not_exists()
    assert is_.equal(s(path_not_exists(None)), "[[ ! -e ]]")
    assert is_.equal(s(path_not_exists("")), "[[ ! -e ]]")
    assert is_.equal(s(path_not_exists("Test")), "[[ ! -e Test ]]")
    with raises(TypeError):
        path_not_exists("Test", None)


def test_path_is_not_directory():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        path_is_not_directory()
    assert is_.equal(s(path_is_not_directory(None)), "[[ ! -d ]]")
    assert is_.equal(s(path_is_not_directory("")), "[[ ! -d ]]")
    assert is_.equal(s(path_is_not_directory("Test")), "[[ ! -d Test ]]")
    with raises(TypeError):
        path_is_not_directory("Test", None)


def test_path_is_not_file():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        path_is_not_file()
    assert is_.equal(s(path_is_not_file(None)), "[[ ! -f ]]")
    assert is_.equal(s(path_is_not_file("")), "[[ ! -f ]]")
    assert is_.equal(s(path_is_not_file("Test")), "[[ ! -f Test ]]")
    with raises(TypeError):
        path_is_not_file("Test", None)


def test_pipe():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(pipe()), " | ")
    with raises(TypeError):
        pipe(None)


def test_remember_last_status():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(remember_last_status()), "Status=$?")
    assert is_.equal(s(remember_last_status(None)), "=$?")
    assert is_.equal(s(remember_last_status("")), "=$?")
    assert is_.equal(s(remember_last_status("Test")), "Test=$?")


def test_research():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(research()), "# TODO: RESEARCH: \n")
    assert is_.equal(s(research(None)), "# TODO: RESEARCH: \n")
    assert is_.equal(s(research("")), "# TODO: RESEARCH: \n")
    assert is_.equal(s(research("Test")), "# TODO: RESEARCH: Test\n")
    assert is_.equal(s(research("Test", None)), "# TODO: RESEARCH: Test\n")
    assert is_.equal(s(research("Test", "")), "# TODO: RESEARCH: Test\n")
    assert is_.equal(s(research("Test", "123")), "# TODO: RESEARCH: Test123\n")


def test_return_():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(return_()), "return")
    assert is_.equal(s(return_(None)), "return")
    assert is_.equal(s(return_("")), "return")
    assert is_.equal(s(return_("Test")), "return Test")
    with raises(TypeError):
        return_("Test", None)


def test_return_with_status():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(return_with_status()), "return ${Status}")
    assert is_.equal(s(return_with_status(None)), "return ${}")
    assert is_.equal(s(return_with_status("")), "return ${}")
    assert is_.equal(s(return_with_status("Test")), "return ${Test}")


def test_rule():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(rule()), 79 * "#" + "\n")
    with raises(TypeError):
        rule(None)


def test_seq():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(seq()), " ; ")
    with raises(TypeError):
        seq(None)


def test_set_():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(set_()), "set")
    assert is_.equal(s(set_(None)), "set")
    assert is_.equal(s(set_("")), "set")
    assert is_.equal(s(set_("Test")), "set Test")
    assert is_.equal(s(set_("Test", None)), "set Test")
    assert is_.equal(s(set_("Test", "")), "set Test")
    assert is_.equal(s(set_("Test", "Test")), "set Test Test")


def test_shebang_bash():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(shebang_bash()), "#!/usr/bin/env bash\n")
    with raises(TypeError):
        shebang_bash(None)


def test_someday():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(someday()), "# TODO: SOMEDAY: \n")
    assert is_.equal(s(someday(None)), "# TODO: SOMEDAY: \n")
    assert is_.equal(s(someday("")), "# TODO: SOMEDAY: \n")
    assert is_.equal(s(someday("Test")), "# TODO: SOMEDAY: Test\n")
    assert is_.equal(s(someday("Test", None)), "# TODO: SOMEDAY: Test\n")
    assert is_.equal(s(someday("Test", "")), "# TODO: SOMEDAY: Test\n")
    assert is_.equal(s(someday("Test", "123")), "# TODO: SOMEDAY: Test123\n")


def test_source():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        source()
    assert is_.equal(s(source(None)), "source")
    assert is_.equal(s(source("")), "source")
    assert is_.equal(s(source("Test")), "source Test")
    with raises(TypeError):
        source("Test", None)


def test_status_is_failure():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(status_is_failure()), "[[ ${Status} -ne 0 ]]")
    assert is_.equal(s(status_is_failure(None)), "[[ ${} -ne 0 ]]")
    assert is_.equal(s(status_is_failure("")), "[[ ${} -ne 0 ]]")
    assert is_.equal(s(status_is_failure("Test")), "[[ ${Test} -ne 0 ]]")


def test_string_equals():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        string_equals()
    with raises(TypeError):
        string_equals(None)
    with raises(TypeError):
        string_equals("")
    with raises(TypeError):
        string_equals("Test")
    assert is_.equal(s(string_equals("Test", None)), "[[ Test == ]]")
    assert is_.equal(s(string_equals("Test", "")), "[[ Test == ]]")
    assert is_.equal(s(string_equals("Test", "123")), "[[ Test == 123 ]]")


def test_string_is_not_null():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        string_is_not_null()
    assert is_.equal(s(string_is_not_null(None)), "[[ -n ]]")
    assert is_.equal(s(string_is_not_null("")), "[[ -n ]]")
    assert is_.equal(s(string_is_not_null("Test")), "[[ -n Test ]]")
    with raises(TypeError):
        string_is_not_null("Test", None)


def test_string_is_null():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        string_is_null()
    assert is_.equal(s(string_is_null(None)), "[[ -z ]]")
    assert is_.equal(s(string_is_null("")), "[[ -z ]]")
    assert is_.equal(s(string_is_null("Test")), "[[ -z Test ]]")
    with raises(TypeError):
        string_is_null("Test", None)


def test_substitute():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        substitute()
    with raises(AssertionError):
        substitute(None)
    with raises(AssertionError):
        substitute("")
    assert is_.equal(s(substitute("Test")), "$(Test)")
    assert is_.equal(s(substitute("Test", None)), "$(Test)")
    assert is_.equal(s(substitute("Test", "")), "$(Test)")
    assert is_.equal(s(substitute("Test", "123")), "$(Test 123)")


def test_todo():
    # TODO: Break up tests into individual test methods
    assert is_.equal(s(todo()), "# TODO: \n")
    assert is_.equal(s(todo(None)), "# TODO: \n")
    assert is_.equal(s(todo("")), "# TODO: \n")
    assert is_.equal(s(todo("Test")), "# TODO: Test\n")
    assert is_.equal(s(todo("Test", None)), "# TODO: Test\n")
    assert is_.equal(s(todo("Test", "")), "# TODO: Test\n")
    assert is_.equal(s(todo("Test", "123")), "# TODO: Test123\n")


def test_vn():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        vn()
    assert is_.equal(s(vn(None)), "")
    assert is_.equal(s(vn("")), "")
    assert is_.equal(s(vn("Test")), "Test")
    with raises(TypeError):
        vn("Test", None)


def test_vr():
    # TODO: Break up tests into individual test methods
    with raises(TypeError):
        vr()
    assert is_.equal(s(vr(None)), "${}")
    assert is_.equal(s(vr("")), "${}")
    assert is_.equal(s(vr("Test")), "${Test}")
    with raises(TypeError):
        vr("Test", None)


"""DisabledContent
"""

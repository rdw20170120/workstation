#!/usr/bin/env false
"""Test corresponding source-generation module."""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
from pytest import raises

# Library modules   (absolute references, NOT packaged, in project)
from src_gen.common import *
from src_gen.renderer import Renderer
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .material import *
from .render import my_visitor_map

s = Renderer(my_visitor_map)._serialize


def test_assign_00():
    with raises(TypeError):
        assign()
def test_assign_01():
    assert is_.equal(s(assign(None)), "=")
def test_assign_02():
    assert is_.equal(s(assign("")), "=")
def test_assign_03():
    assert is_.equal(s(assign("Test")), "Test=")
def test_assign_04():
    assert is_.equal(s(assign("Test", None)), "Test=")
def test_assign_05():
    assert is_.equal(s(assign("Test", "")), "Test=")
def test_assign_06():
    assert is_.equal(s(assign("Test", "123")), "Test=123")


# TODO: def test_cc():


def test_directory_exists_00():
    with raises(TypeError):
        directory_exists()
def test_directory_exists_01():
    assert is_.equal(s(directory_exists(None)), "[[ -d ]]")
def test_directory_exists_02():
    assert is_.equal(s(directory_exists("")), "[[ -d ]]")
def test_directory_exists_03():
    assert is_.equal(s(directory_exists("Test")), "[[ -d Test ]]")
def test_directory_exists_04():
    with raises(TypeError):
        directory_exists("Test", None)


def test_disabled_00():
    assert is_.equal(s(disabled()), "# DISABLED: \n")
def test_disabled_01():
    assert is_.equal(s(disabled(None)), "# DISABLED: \n")
def test_disabled_02():
    assert is_.equal(s(disabled("")), "# DISABLED: \n")
def test_disabled_03():
    assert is_.equal(s(disabled("Test")), "# DISABLED: Test\n")
def test_disabled_04():
    assert is_.equal(s(disabled("Test", None)), "# DISABLED: Test\n")
def test_disabled_05():
    assert is_.equal(s(disabled("Test", "")), "# DISABLED: Test\n")
def test_disabled_06():
    assert is_.equal(s(disabled("Test", "123")), "# DISABLED: Test123\n")


def test_echo_00():
    assert is_.equal(s(echo()), "echo")
def test_echo_01():
    assert is_.equal(s(echo(None)), "echo")
def test_echo_02():
    assert is_.equal(s(echo("")), "echo")
def test_echo_03():
    assert is_.equal(s(echo("Test")), "echo Test")
def test_echo_04():
    assert is_.equal(s(echo("Test", None)), "echo Test")
def test_echo_05():
    assert is_.equal(s(echo("Test", "")), "echo Test")
def test_echo_06():
    assert is_.equal(s(echo("Test", "123")), "echo Test 123")


def test_echo_debug_00():
    assert is_.equal(s(echo_debug()), '1>&2 echo "DEBUG: "')
def test_echo_debug_01():
    assert is_.equal(s(echo_debug(None)), '1>&2 echo "DEBUG: "')
def test_echo_debug_02():
    assert is_.equal(s(echo_debug("")), '1>&2 echo "DEBUG: "')
def test_echo_debug_03():
    assert is_.equal(s(echo_debug("Test")), '1>&2 echo "DEBUG: Test"')
def test_echo_debug_04():
    assert is_.equal(s(echo_debug("Test", None)), '1>&2 echo "DEBUG: Test"')
def test_echo_debug_05():
    assert is_.equal(s(echo_debug("Test", "")), '1>&2 echo "DEBUG: Test"')
def test_echo_debug_06():
    assert is_.equal(s(echo_debug("Test", "123")), '1>&2 echo "DEBUG: Test123"')


def test_echo_error_00():
    assert is_.equal(s(echo_error()), '1>&2 echo "ERROR: "')
def test_echo_error_01():
    assert is_.equal(s(echo_error(None)), '1>&2 echo "ERROR: "')
def test_echo_error_02():
    assert is_.equal(s(echo_error("")), '1>&2 echo "ERROR: "')
def test_echo_error_03():
    assert is_.equal(s(echo_error("Test")), '1>&2 echo "ERROR: Test"')
def test_echo_error_04():
    assert is_.equal(s(echo_error("Test", None)), '1>&2 echo "ERROR: Test"')
def test_echo_error_05():
    assert is_.equal(s(echo_error("Test", "")), '1>&2 echo "ERROR: Test"')
def test_echo_error_06():
    assert is_.equal(s(echo_error("Test", "123")), '1>&2 echo "ERROR: Test123"')


def test_echo_info_00():
    assert is_.equal(s(echo_info()), '1>&2 echo "INFO:  "')
def test_echo_info_01():
    assert is_.equal(s(echo_info(None)), '1>&2 echo "INFO:  "')
def test_echo_info_02():
    assert is_.equal(s(echo_info("")), '1>&2 echo "INFO:  "')
def test_echo_info_03():
    assert is_.equal(s(echo_info("Test")), '1>&2 echo "INFO:  Test"')
def test_echo_info_04():
    assert is_.equal(s(echo_info("Test", None)), '1>&2 echo "INFO:  Test"')
def test_echo_info_05():
    assert is_.equal(s(echo_info("Test", "")), '1>&2 echo "INFO:  Test"')
def test_echo_info_06():
    assert is_.equal(s(echo_info("Test", "123")), '1>&2 echo "INFO:  Test123"')


def test_echo_warn_00():
    assert is_.equal(s(echo_warn()), '1>&2 echo "WARN:  "')
def test_echo_warn_01():
    assert is_.equal(s(echo_warn(None)), '1>&2 echo "WARN:  "')
def test_echo_warn_02():
    assert is_.equal(s(echo_warn("")), '1>&2 echo "WARN:  "')
def test_echo_warn_03():
    assert is_.equal(s(echo_warn("Test")), '1>&2 echo "WARN:  Test"')
def test_echo_warn_04():
    assert is_.equal(s(echo_warn("Test", None)), '1>&2 echo "WARN:  Test"')
def test_echo_warn_05():
    assert is_.equal(s(echo_warn("Test", "")), '1>&2 echo "WARN:  Test"')
def test_echo_warn_06():
    assert is_.equal(s(echo_warn("Test", "123")), '1>&2 echo "WARN:  Test123"')


def test_elif_00():
    with raises(TypeError):
        elif_()
def test_elif_01():
    with raises(AssertionError):
        elif_(None)
def test_elif_02():
    with raises(AssertionError):
        elif_("")
def test_elif_03():
    with raises(AssertionError):
        elif_("Test")
def test_elif_04():
    with raises(AssertionError):
        elif_("Test", None)
def test_elif_05():
    with raises(AssertionError):
        elif_("Test", "")
def test_elif_06():
    assert is_.equal(s(elif_("Test", "123")), "elif Test ; then\n123")


def test_else_00():
    with raises(AssertionError):
        else_()
def test_else_01():
    with raises(AssertionError):
        else_(None)
def test_else_02():
    with raises(AssertionError):
        else_("")
def test_else_03():
    assert is_.equal(s(else_("Test")), "else\nTest")
def test_else_04():
    assert is_.equal(s(else_("Test", None)), "else\nTest")
def test_else_05():
    assert is_.equal(s(else_("Test", "")), "else\nTest")
def test_else_06():
    assert is_.equal(s(else_("Test", "123")), "else\nTest123")


def test_exit_00():
    assert is_.equal(s(exit()), "exit")
def test_exit_01():
    assert is_.equal(s(exit(None)), "exit")
def test_exit_02():
    assert is_.equal(s(exit("")), "exit")
def test_exit_03():
    assert is_.equal(s(exit("Test")), "exit Test")
def test_exit_04():
    with raises(TypeError):
        exit("Test", None)


# TODO: def test_exit_with_status():


def test_export_00():
    with raises(TypeError):
        export()
def test_export_01():
    assert is_.equal(s(export(None)), "export")
def test_export_02():
    assert is_.equal(s(export("")), "export")
def test_export_03():
    assert is_.equal(s(export("Test")), "export Test")
def test_export_04():
    assert is_.equal(s(export("Test", None)), "export Test")
def test_export_05():
    assert is_.equal(s(export("Test", "")), "export Test=")
def test_export_06():
    assert is_.equal(s(export("Test", "123")), "export Test=123")


def test_fi_00():
    assert is_.equal(s(fi()), "fi\n")
def test_fi_01():
    with raises(TypeError):
        fi(None)


def test_file_exists_00():
    with raises(TypeError):
        file_exists()
def test_file_exists_01():
    assert is_.equal(s(file_exists(None)), "[[ -f ]]")
def test_file_exists_02():
    assert is_.equal(s(file_exists("")), "[[ -f ]]")
def test_file_exists_03():
    assert is_.equal(s(file_exists("Test")), "[[ -f Test ]]")
def test_file_exists_04():
    with raises(TypeError):
        file_exists("Test", None)


def test_file_is_readable_00():
    with raises(TypeError):
        file_is_readable()
def test_file_is_readable_01():
    assert is_.equal(s(file_is_readable(None)), "[[ -r ]]")
def test_file_is_readable_02():
    assert is_.equal(s(file_is_readable("")), "[[ -r ]]")
def test_file_is_readable_03():
    assert is_.equal(s(file_is_readable("Test")), "[[ -r Test ]]")
def test_file_is_readable_04():
    with raises(TypeError):
        file_is_readable("Test", None)


def test_fix_00():
    assert is_.equal(s(fix()), "# TODO: FIX: \n")
def test_fix_01():
    assert is_.equal(s(fix(None)), "# TODO: FIX: \n")
def test_fix_02():
    assert is_.equal(s(fix("")), "# TODO: FIX: \n")
def test_fix_03():
    assert is_.equal(s(fix("Test")), "# TODO: FIX: Test\n")
def test_fix_04():
    assert is_.equal(s(fix("Test", None)), "# TODO: FIX: Test\n")
def test_fix_05():
    assert is_.equal(s(fix("Test", "")), "# TODO: FIX: Test\n")
def test_fix_06():
    assert is_.equal(s(fix("Test", "123")), "# TODO: FIX: Test123\n")


def test_if_00():
    with raises(TypeError):
        if_()
def test_if_01():
    with raises(AssertionError):
        if_(None)
def test_if_02():
    with raises(AssertionError):
        if_("")
def test_if_03():
    with raises(AssertionError):
        if_("Test")
def test_if_04():
    with raises(AssertionError):
        if_("Test", None)
def test_if_05():
    with raises(AssertionError):
        if_("Test", "")
def test_if_06():
    assert is_.equal(s(if_("Test", "123")), "if Test ; then\n123")


# TODO: def test_integer_equal():


def test_integer_not_equal_00():
    with raises(TypeError):
        integer_not_equal()
def test_integer_not_equal_01():
    with raises(TypeError):
        integer_not_equal(None)
def test_integer_not_equal_02():
    with raises(TypeError):
        integer_not_equal("")
def test_integer_not_equal_03():
    with raises(TypeError):
        integer_not_equal("Test")
def test_integer_not_equal_04():
    assert is_.equal(s(integer_not_equal(None, 123)), "[[ -ne 123 ]]")
def test_integer_not_equal_05():
    assert is_.equal(s(integer_not_equal("", 123)), "[[ -ne 123 ]]")
def test_integer_not_equal_06():
    assert is_.equal(s(integer_not_equal("Test", 123)), "[[ Test -ne 123 ]]")


# TODO: def test_local():


def test_path_is_not_directory_00():
    with raises(TypeError):
        path_is_not_directory()
def test_path_is_not_directory_01():
    assert is_.equal(s(path_is_not_directory(None)), "[[ ! -d ]]")
def test_path_is_not_directory_02():
    assert is_.equal(s(path_is_not_directory("")), "[[ ! -d ]]")
def test_path_is_not_directory_03():
    assert is_.equal(s(path_is_not_directory("Test")), "[[ ! -d Test ]]")
def test_path_is_not_directory_04():
    with raises(TypeError):
        path_is_not_directory("Test", None)


def test_path_is_not_file_00():
    with raises(TypeError):
        path_is_not_file()
def test_path_is_not_file_01():
    assert is_.equal(s(path_is_not_file(None)), "[[ ! -f ]]")
def test_path_is_not_file_02():
    assert is_.equal(s(path_is_not_file("")), "[[ ! -f ]]")
def test_path_is_not_file_03():
    assert is_.equal(s(path_is_not_file("Test")), "[[ ! -f Test ]]")
def test_path_is_not_file_04():
    with raises(TypeError):
        path_is_not_file("Test", None)


def test_path_not_exists_00():
    with raises(TypeError):
        path_not_exists()
def test_path_not_exists_01():
    assert is_.equal(s(path_not_exists(None)), "[[ ! -e ]]")
def test_path_not_exists_02():
    assert is_.equal(s(path_not_exists("")), "[[ ! -e ]]")
def test_path_not_exists_03():
    assert is_.equal(s(path_not_exists("Test")), "[[ ! -e Test ]]")
def test_path_not_exists_04():
    with raises(TypeError):
        path_not_exists("Test", None)


def test_remember_last_status_00():
    assert is_.equal(s(remember_last_status()), "Status=$?")
def test_remember_last_status_01():
    assert is_.equal(s(remember_last_status(None)), "=$?")
def test_remember_last_status_02():
    assert is_.equal(s(remember_last_status("")), "=$?")
def test_remember_last_status_03():
    assert is_.equal(s(remember_last_status("Test")), "Test=$?")


def test_research_00():
    assert is_.equal(s(research()), "# TODO: RESEARCH: \n")
def test_research_01():
    assert is_.equal(s(research(None)), "# TODO: RESEARCH: \n")
def test_research_02():
    assert is_.equal(s(research("")), "# TODO: RESEARCH: \n")
def test_research_03():
    assert is_.equal(s(research("Test")), "# TODO: RESEARCH: Test\n")
def test_research_04():
    assert is_.equal(s(research("Test", None)), "# TODO: RESEARCH: Test\n")
def test_research_05():
    assert is_.equal(s(research("Test", "")), "# TODO: RESEARCH: Test\n")
def test_research_06():
    assert is_.equal(s(research("Test", "123")), "# TODO: RESEARCH: Test123\n")


def test_return_00():
    assert is_.equal(s(return_()), "return")
def test_return_01():
    assert is_.equal(s(return_(None)), "return")
def test_return_02():
    assert is_.equal(s(return_("")), "return")
def test_return_03():
    assert is_.equal(s(return_("Test")), "return Test")
def test_return_04():
    with raises(TypeError):
        return_("Test", None)


def test_return_with_status_00():
    assert is_.equal(s(return_with_status()), "return ${Status}")
def test_return_with_status_01():
    assert is_.equal(s(return_with_status(None)), "return ${}")
def test_return_with_status_02():
    assert is_.equal(s(return_with_status("")), "return ${}")
def test_return_with_status_03():
    assert is_.equal(s(return_with_status("Test")), "return ${Test}")


def test_rule_00():
    assert is_.equal(s(rule()), 79 * "#" + "\n")
def test_rule_01():
    with raises(TypeError):
        rule(None)


def test_set_00():
    assert is_.equal(s(set_()), "set")
def test_set_01():
    assert is_.equal(s(set_(None)), "set")
def test_set_02():
    assert is_.equal(s(set_("")), "set")
def test_set_03():
    assert is_.equal(s(set_("Test")), "set Test")
def test_set_04():
    assert is_.equal(s(set_("Test", None)), "set Test")
def test_set_05():
    assert is_.equal(s(set_("Test", "")), "set Test")
def test_set_06():
    assert is_.equal(s(set_("Test", "Test")), "set Test Test")


def test_shebang_bash_00():
    assert is_.equal(s(shebang_bash()), "#!/usr/bin/env bash\n")
def test_shebang_bash_01():
    with raises(TypeError):
        shebang_bash(None)


def test_someday_00():
    assert is_.equal(s(someday()), "# TODO: SOMEDAY: \n")
def test_someday_01():
    assert is_.equal(s(someday(None)), "# TODO: SOMEDAY: \n")
def test_someday_02():
    assert is_.equal(s(someday("")), "# TODO: SOMEDAY: \n")
def test_someday_03():
    assert is_.equal(s(someday("Test")), "# TODO: SOMEDAY: Test\n")
def test_someday_04():
    assert is_.equal(s(someday("Test", None)), "# TODO: SOMEDAY: Test\n")
def test_someday_05():
    assert is_.equal(s(someday("Test", "")), "# TODO: SOMEDAY: Test\n")
def test_someday_06():
    assert is_.equal(s(someday("Test", "123")), "# TODO: SOMEDAY: Test123\n")


def test_source_00():
    with raises(TypeError):
        source()
def test_source_01():
    assert is_.equal(s(source(None)), "source")
def test_source_02():
    assert is_.equal(s(source("")), "source")
def test_source_03():
    assert is_.equal(s(source("Test")), "source Test")
def test_source_04():
    with raises(TypeError):
        source("Test", None)


def test_status_is_failure_00():
    assert is_.equal(s(status_is_failure()), "[[ ${Status} -ne 0 ]]")
def test_status_is_failure_01():
    assert is_.equal(s(status_is_failure(None)), "[[ ${} -ne 0 ]]")
def test_status_is_failure_02():
    assert is_.equal(s(status_is_failure("")), "[[ ${} -ne 0 ]]")
def test_status_is_failure_03():
    assert is_.equal(s(status_is_failure("Test")), "[[ ${Test} -ne 0 ]]")


# TODO: def test_status_is_success():


def test_string_equals_00():
    with raises(TypeError):
        string_equals()
def test_string_equals_01():
    with raises(TypeError):
        string_equals(None)
def test_string_equals_02():
    with raises(TypeError):
        string_equals("")
def test_string_equals_03():
    with raises(TypeError):
        string_equals("Test")
def test_string_equals_04():
    assert is_.equal(s(string_equals("Test", None)), "[[ Test == ]]")
def test_string_equals_05():
    assert is_.equal(s(string_equals("Test", "")), "[[ Test == ]]")
def test_string_equals_06():
    assert is_.equal(s(string_equals("Test", "123")), "[[ Test == 123 ]]")


def test_string_is_not_null_00():
    with raises(TypeError):
        string_is_not_null()
def test_string_is_not_null_01():
    assert is_.equal(s(string_is_not_null(None)), "[[ -n ]]")
def test_string_is_not_null_02():
    assert is_.equal(s(string_is_not_null("")), "[[ -n ]]")
def test_string_is_not_null_03():
    assert is_.equal(s(string_is_not_null("Test")), "[[ -n Test ]]")
def test_string_is_not_null_04():
    with raises(TypeError):
        string_is_not_null("Test", None)


def test_string_is_null_00():
    with raises(TypeError):
        string_is_null()
def test_string_is_null_01():
    assert is_.equal(s(string_is_null(None)), "[[ -z ]]")
def test_string_is_null_02():
    assert is_.equal(s(string_is_null("")), "[[ -z ]]")
def test_string_is_null_03():
    assert is_.equal(s(string_is_null("Test")), "[[ -z Test ]]")
def test_string_is_null_04():
    with raises(TypeError):
        string_is_null("Test", None)


def test_substitute_00():
    with raises(TypeError):
        substitute()
def test_substitute_01():
    with raises(AssertionError):
        substitute(None)
def test_substitute_02():
    with raises(AssertionError):
        substitute("")
def test_substitute_03():
    assert is_.equal(s(substitute("Test")), "$(Test)")
def test_substitute_04():
    assert is_.equal(s(substitute("Test", None)), "$(Test)")
def test_substitute_05():
    assert is_.equal(s(substitute("Test", "")), "$(Test)")
def test_substitute_06():
    assert is_.equal(s(substitute("Test", "123")), "$(Test 123)")


def test_todo_00():
    assert is_.equal(s(todo()), "# TODO: \n")
def test_todo_01():
    assert is_.equal(s(todo(None)), "# TODO: \n")
def test_todo_02():
    assert is_.equal(s(todo("")), "# TODO: \n")
def test_todo_03():
    assert is_.equal(s(todo("Test")), "# TODO: Test\n")
def test_todo_04():
    assert is_.equal(s(todo("Test", None)), "# TODO: Test\n")
def test_todo_05():
    assert is_.equal(s(todo("Test", "")), "# TODO: Test\n")
def test_todo_06():
    assert is_.equal(s(todo("Test", "123")), "# TODO: Test123\n")


def test_vn_00():
    with raises(TypeError):
        vn()
def test_vn_01():
    assert is_.equal(s(vn(None)), "")
def test_vn_02():
    assert is_.equal(s(vn("")), "")
def test_vn_03():
    assert is_.equal(s(vn("Test")), "Test")
def test_vn_04():
    with raises(TypeError):
        vn("Test", None)


def test_vr_00():
    with raises(TypeError):
        vr()
def test_vr_01():
    assert is_.equal(s(vr(None)), "${}")
def test_vr_02():
    assert is_.equal(s(vr("")), "${}")
def test_vr_03():
    assert is_.equal(s(vr("Test")), "${Test}")
def test_vr_04():
    with raises(TypeError):
        vr("Test", None)


"""DisabledContent
"""

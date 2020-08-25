#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
from pytest import raises
# Library modules    (absolute references, NOT packaged, in project)
from utility.my_assert import assert_equal
# Co-located modules (relative references, NOT packaged, in project)
from ...renderer import Renderer
from .source import my_visitor_map
from .structure import *


# NOTE: There is little value in testing "composed" methods,
# e.g., those consisting of 'return [...]'.
# TODO: Generate tests

s = Renderer(my_visitor_map)._serialize

def test_and_():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(and_()), ' && ')
    with raises(TypeError): and_(None)

def test_assign():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): assign()
    assert assert_equal(s(assign(None)), '=')
    assert assert_equal(s(assign('')), '=')
    assert assert_equal(s(assign('Test')), 'Test=')
    assert assert_equal(s(assign('Test', None)), 'Test=')
    assert assert_equal(s(assign('Test', '')), 'Test=')
    assert assert_equal(s(assign('Test', '123')), 'Test=123')

def test_bs():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(bs()), '\\\n')
    with raises(TypeError): bs(None)

def test_directory_exists():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): directory_exists()
    assert assert_equal(s(directory_exists(None)), '[[ -d "" ]]')
    assert assert_equal(s(directory_exists('')), '[[ -d "" ]]')
    assert assert_equal(s(directory_exists('Test')), '[[ -d "Test" ]]')
    with raises(TypeError): directory_exists('Test', None)

def test_disabled():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(disabled()), '# DISABLED: \n')
    assert assert_equal(s(disabled(None)), '# DISABLED: \n')
    assert assert_equal(s(disabled('')), '# DISABLED: \n')
    assert assert_equal(s(disabled('Test')), '# DISABLED: Test\n')
    assert assert_equal(s(disabled('Test', None)), '# DISABLED: Test\n')
    assert assert_equal(s(disabled('Test', '')), '# DISABLED: Test\n')
    assert assert_equal(s(disabled('Test', '123')), '# DISABLED: Test123\n')

def test_echo():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(echo()), 'echo')
    assert assert_equal(s(echo(None)), 'echo')
    assert assert_equal(s(echo('')), 'echo')
    assert assert_equal(s(echo('Test')), 'echo Test')
    assert assert_equal(s(echo('Test', None)), 'echo Test')
    assert assert_equal(s(echo('Test', '')), 'echo Test')
    assert assert_equal(s(echo('Test', '123')), 'echo Test 123')

def test_echo_fatal():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(echo_fatal()), 'echo "FATAL: "')
    assert assert_equal(s(echo_fatal(None)), 'echo "FATAL: "')
    assert assert_equal(s(echo_fatal('')), 'echo "FATAL: "')
    assert assert_equal(s(echo_fatal('Test')), 'echo "FATAL: Test"')
    assert assert_equal(s(echo_fatal('Test', None)), 'echo "FATAL: Test"')
    assert assert_equal(s(echo_fatal('Test', '')), 'echo "FATAL: Test"')
    assert assert_equal(s(echo_fatal('Test', '123')), 'echo "FATAL: Test123"')

def test_echo_info():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(echo_info()), 'echo "INFO:  "')
    assert assert_equal(s(echo_info(None)), 'echo "INFO:  "')
    assert assert_equal(s(echo_info('')), 'echo "INFO:  "')
    assert assert_equal(s(echo_info('Test')), 'echo "INFO:  Test"')
    assert assert_equal(s(echo_info('Test', None)), 'echo "INFO:  Test"')
    assert assert_equal(s(echo_info('Test', '')), 'echo "INFO:  Test"')
    assert assert_equal(s(echo_info('Test', '123')), 'echo "INFO:  Test123"')

def test_echo_trace():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(echo_trace()), 'echo "TRACE: "')
    assert assert_equal(s(echo_trace(None)), 'echo "TRACE: "')
    assert assert_equal(s(echo_trace('')), 'echo "TRACE: "')
    assert assert_equal(s(echo_trace('Test')), 'echo "TRACE: Test"')
    assert assert_equal(s(echo_trace('Test', None)), 'echo "TRACE: Test"')
    assert assert_equal(s(echo_trace('Test', '')), 'echo "TRACE: Test"')
    assert assert_equal(s(echo_trace('Test', '123')), 'echo "TRACE: Test123"')

def test_echo_warn():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(echo_warn()), 'echo "WARN:  "')
    assert assert_equal(s(echo_warn(None)), 'echo "WARN:  "')
    assert assert_equal(s(echo_warn('')), 'echo "WARN:  "')
    assert assert_equal(s(echo_warn('Test')), 'echo "WARN:  Test"')
    assert assert_equal(s(echo_warn('Test', None)), 'echo "WARN:  Test"')
    assert assert_equal(s(echo_warn('Test', '')), 'echo "WARN:  Test"')
    assert assert_equal(s(echo_warn('Test', '123')), 'echo "WARN:  Test123"')

def test_elif_():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): elif_()
    with raises(AssertionError): elif_(None)
    with raises(AssertionError): elif_('')
    with raises(AssertionError): elif_('Test')
    with raises(AssertionError): elif_('Test', None)
    with raises(AssertionError): elif_('Test', '')
    assert assert_equal(s(elif_('Test', '123')), 'elif Test ; then\n123')

def test_else_():
    # TODO: Break up tests into individual test methods
    with raises(AssertionError): else_()
    with raises(AssertionError): else_(None)
    with raises(AssertionError): else_('')
    assert assert_equal(s(else_('Test')), 'else\nTest')
    assert assert_equal(s(else_('Test', None)), 'else\nTest')
    assert assert_equal(s(else_('Test', '')), 'else\nTest')
    assert assert_equal(s(else_('Test', '123')), 'else\nTest123')

def test_exit():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(exit()), 'exit')
    assert assert_equal(s(exit(None)), 'exit')
    assert assert_equal(s(exit('')), 'exit')
    assert assert_equal(s(exit('Test')), 'exit Test')
    with raises(TypeError): exit('Test', None)

def test_export():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): export()
    assert assert_equal(s(export(None)), 'export')
    assert assert_equal(s(export('')), 'export')
    assert assert_equal(s(export('Test')), 'export Test')
    assert assert_equal(s(export('Test', None)), 'export Test')
    assert assert_equal(s(export('Test', '')), 'export Test=')
    assert assert_equal(s(export('Test', '123')), 'export Test=123')

def test_fi():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(fi()), 'fi\n')
    with raises(TypeError): fi(None)

def test_file_exists():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): file_exists()
    assert assert_equal(s(file_exists(None)), '[[ -f "" ]]')
    assert assert_equal(s(file_exists('')), '[[ -f "" ]]')
    assert assert_equal(s(file_exists('Test')), '[[ -f "Test" ]]')
    with raises(TypeError): file_exists('Test', None)

def test_file_is_readable():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): file_is_readable()
    assert assert_equal(s(file_is_readable(None)), '[[ -r "" ]]')
    assert assert_equal(s(file_is_readable('')), '[[ -r "" ]]')
    assert assert_equal(s(file_is_readable('Test')), '[[ -r "Test" ]]')
    with raises(TypeError): file_is_readable('Test', None)

def test_fix():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(fix()), '# TODO: FIX: \n')
    assert assert_equal(s(fix(None)), '# TODO: FIX: \n')
    assert assert_equal(s(fix('')), '# TODO: FIX: \n')
    assert assert_equal(s(fix('Test')), '# TODO: FIX: Test\n')
    assert assert_equal(s(fix('Test', None)), '# TODO: FIX: Test\n')
    assert assert_equal(s(fix('Test', '')), '# TODO: FIX: Test\n')
    assert assert_equal(s(fix('Test', '123')), '# TODO: FIX: Test123\n')

def test_if_():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): if_()
    with raises(AssertionError): if_(None)
    with raises(AssertionError): if_('')
    with raises(AssertionError): if_('Test')
    with raises(AssertionError): if_('Test', None)
    with raises(AssertionError): if_('Test', '')
    assert assert_equal(s(if_('Test', '123')), 'if Test ; then\n123')

def test_indent():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(indent()), 4 * ' ')
    with raises(TypeError): indent(None)

def test_integer_is_not_equal():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): integer_is_not_equal()
    with raises(TypeError): integer_is_not_equal(None)
    with raises(TypeError): integer_is_not_equal('')
    with raises(TypeError): integer_is_not_equal('Test')
    assert assert_equal(s(integer_is_not_equal(None, 123)), '[[ "" -ne 123 ]]')
    assert assert_equal(s(integer_is_not_equal('', 123)), '[[ "" -ne 123 ]]')
    assert assert_equal(s(integer_is_not_equal('Test', 123)), '[[ "Test" -ne 123 ]]')

def test_no():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(no()), '# NO: \n')
    assert assert_equal(s(no(None)), '# NO: \n')
    assert assert_equal(s(no('')), '# NO: \n')
    assert assert_equal(s(no('Test')), '# NO: Test\n')
    assert assert_equal(s(no('Test', None)), '# NO: Test\n')
    assert assert_equal(s(no('Test', '')), '# NO: Test\n')
    assert assert_equal(s(no('Test', '123')), '# NO: Test123\n')

def test_note():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(note()), '# NOTE: \n')
    assert assert_equal(s(note(None)), '# NOTE: \n')
    assert assert_equal(s(note('')), '# NOTE: \n')
    assert assert_equal(s(note('Test')), '# NOTE: Test\n')
    assert assert_equal(s(note('Test', None)), '# NOTE: Test\n')
    assert assert_equal(s(note('Test', '')), '# NOTE: Test\n')
    assert assert_equal(s(note('Test', '123')), '# NOTE: Test123\n')

def test_or_():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(or_()), ' || ')
    with raises(TypeError): or_(None)

def test_path_does_not_exist():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): path_does_not_exist()
    assert assert_equal(s(path_does_not_exist(None)), '[[ ! -e "" ]]')
    assert assert_equal(s(path_does_not_exist('')), '[[ ! -e "" ]]')
    assert assert_equal(s(path_does_not_exist('Test')), '[[ ! -e "Test" ]]')
    with raises(TypeError): path_does_not_exist('Test', None)

def test_path_is_not_directory():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): path_is_not_directory()
    assert assert_equal(s(path_is_not_directory(None)), '[[ ! -d "" ]]')
    assert assert_equal(s(path_is_not_directory('')), '[[ ! -d "" ]]')
    assert assert_equal(s(path_is_not_directory('Test')), '[[ ! -d "Test" ]]')
    with raises(TypeError): path_is_not_directory('Test', None)

def test_path_is_not_file():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): path_is_not_file()
    assert assert_equal(s(path_is_not_file(None)), '[[ ! -f "" ]]')
    assert assert_equal(s(path_is_not_file('')), '[[ ! -f "" ]]')
    assert assert_equal(s(path_is_not_file('Test')), '[[ ! -f "Test" ]]')
    with raises(TypeError): path_is_not_file('Test', None)

def test_pipe():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(pipe()), ' | ')
    with raises(TypeError): pipe(None)

def test_remember_status():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(remember_status()), 'Status=$?')
    with raises(TypeError): remember_status(None)

def test_report_exit_status():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(report_exit_status()), 'echo "FATAL: Script exited with \'$Status\'"')
    with raises(TypeError): report_exit_status(None)

def test_research():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(research()), '# TODO: RESEARCH: \n')
    assert assert_equal(s(research(None)), '# TODO: RESEARCH: \n')
    assert assert_equal(s(research('')), '# TODO: RESEARCH: \n')
    assert assert_equal(s(research('Test')), '# TODO: RESEARCH: Test\n')
    assert assert_equal(s(research('Test', None)), '# TODO: RESEARCH: Test\n')
    assert assert_equal(s(research('Test', '')), '# TODO: RESEARCH: Test\n')
    assert assert_equal(s(research('Test', '123')), '# TODO: RESEARCH: Test123\n')

def test_return_():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(return_()), 'return')
    assert assert_equal(s(return_(None)), 'return')
    assert assert_equal(s(return_('')), 'return')
    assert assert_equal(s(return_('Test')), 'return Test')
    with raises(TypeError): return_('Test', None)

def test_return_last_status():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(return_last_status()), 'return $?')
    with raises(TypeError): return_last_status(None)

def test_return_status():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(return_status()), 'return $Status')
    with raises(TypeError): return_status(None)

def test_rule():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(rule()), 79 * '#' + '\n')
    with raises(TypeError): rule(None)

def test_seq():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(seq()), ' ; ')
    with raises(TypeError): seq(None)

def test_set_():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): set_()
    assert assert_equal(s(set_(None)), 'set')
    assert assert_equal(s(set_('')), 'set')
    assert assert_equal(s(set_('Test')), 'set Test')
    with raises(TypeError): set_('Test', None)

def test_shebang_bash():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(shebang_bash()), '#!/usr/bin/env bash\n')
    with raises(TypeError): shebang_bash(None)

def test_someday():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(someday()), '# TODO: SOMEDAY: \n')
    assert assert_equal(s(someday(None)), '# TODO: SOMEDAY: \n')
    assert assert_equal(s(someday('')), '# TODO: SOMEDAY: \n')
    assert assert_equal(s(someday('Test')), '# TODO: SOMEDAY: Test\n')
    assert assert_equal(s(someday('Test', None)), '# TODO: SOMEDAY: Test\n')
    assert assert_equal(s(someday('Test', '')), '# TODO: SOMEDAY: Test\n')
    assert assert_equal(s(someday('Test', '123')), '# TODO: SOMEDAY: Test123\n')

def test_source():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): source()
    assert assert_equal(s(source(None)), 'source')
    assert assert_equal(s(source('')), 'source')
    assert assert_equal(s(source('Test')), 'source Test')
    with raises(TypeError): source('Test', None)

def test_status_is_failure():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(status_is_failure()), '[[ "$Status" -ne 0 ]]')
    with raises(TypeError): status_is_failure(None)

def test_string_equals():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): string_equals()
    with raises(TypeError): string_equals(None)
    with raises(TypeError): string_equals('')
    with raises(TypeError): string_equals('Test')
    assert assert_equal(s(string_equals('Test', None)), '[[ "Test" == "" ]]')
    assert assert_equal(s(string_equals('Test', '')), '[[ "Test" == "" ]]')
    assert assert_equal(s(string_equals('Test', '123')), '[[ "Test" == "123" ]]')

def test_string_is_not_null():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): string_is_not_null()
    assert assert_equal(s(string_is_not_null(None)), '[[ -n "" ]]')
    assert assert_equal(s(string_is_not_null('')), '[[ -n "" ]]')
    assert assert_equal(s(string_is_not_null('Test')), '[[ -n "Test" ]]')
    with raises(TypeError): string_is_not_null('Test', None)

def test_string_is_null():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): string_is_null()
    assert assert_equal(s(string_is_null(None)), '[[ -z "" ]]')
    assert assert_equal(s(string_is_null('')), '[[ -z "" ]]')
    assert assert_equal(s(string_is_null('Test')), '[[ -z "Test" ]]')
    with raises(TypeError): string_is_null('Test', None)

def test_substitute():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): substitute()
    with raises(AssertionError): substitute(None)
    with raises(AssertionError): substitute('')
    assert assert_equal(s(substitute('Test')), '$(Test)')
    assert assert_equal(s(substitute('Test', None)), '$(Test)')
    assert assert_equal(s(substitute('Test', '')), '$(Test)')
    assert assert_equal(s(substitute('Test', '123')), '$(Test 123)')

def test_todo():
    # TODO: Break up tests into individual test methods
    assert assert_equal(s(todo()), '# TODO: \n')
    assert assert_equal(s(todo(None)), '# TODO: \n')
    assert assert_equal(s(todo('')), '# TODO: \n')
    assert assert_equal(s(todo('Test')), '# TODO: Test\n')
    assert assert_equal(s(todo('Test', None)), '# TODO: Test\n')
    assert assert_equal(s(todo('Test', '')), '# TODO: Test\n')
    assert assert_equal(s(todo('Test', '123')), '# TODO: Test123\n')

def test_vn():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): vn()
    assert assert_equal(s(vn(None)), '')
    assert assert_equal(s(vn('')), '')
    assert assert_equal(s(vn('Test')), 'Test')
    with raises(TypeError): vn('Test', None)

def test_vr():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): vr()
    assert assert_equal(s(vr(None)), '$')
    assert assert_equal(s(vr('')), '$')
    assert assert_equal(s(vr('Test')), '$Test')
    with raises(TypeError): vr('Test', None)

'''DisabledContent
'''


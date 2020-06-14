#!/usr/bin/env false

from pytest import raises

from .source     import visitor_map
from .structure  import * 
from ...renderer import Renderer


# NOTE: There is little value in testing "composed" methods,
# e.g., those consisting of 'return [...]'.
# TODO: Generate tests

s = Renderer(visitor_map)._serialize

def test_and_():
    # TODO: Break up tests into individual test methods
    assert s(and_()) == ' && '
    with raises(TypeError): and_(None)

def test_assign():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): assign()
    with raises(AssertionError): assign(None)
    with raises(AssertionError): assign('')
    assert s(assign('Test')) == 'Test='
    assert s(assign('Test', None)) == 'Test='
    assert s(assign('Test', '')) == 'Test='
    assert s(assign('Test', '123')) == 'Test=123'

def test_bs():
    # TODO: Break up tests into individual test methods
    assert s(bs()) == '\\\n'
    with raises(TypeError): bs(None)

def test_directory_exists():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): directory_exists()
    with raises(AssertionError): directory_exists(None)
    with raises(AssertionError): directory_exists('')
    assert s(directory_exists('Test')) == '[[ -d "Test" ]]'
    with raises(TypeError): directory_exists('Test', None)

def test_disabled():
    # TODO: Break up tests into individual test methods
    assert s(disabled()) == '# DISABLED: \n'
    assert s(disabled(None)) == '# DISABLED: \n'
    assert s(disabled('')) == '# DISABLED: \n'
    assert s(disabled('Test')) == '# DISABLED: Test\n'
    assert s(disabled('Test', None)) == '# DISABLED: Test\n'
    assert s(disabled('Test', '')) == '# DISABLED: Test\n'
    assert s(disabled('Test', '123')) == '# DISABLED: Test123\n'

def test_echo():
    # TODO: Break up tests into individual test methods
    assert s(echo()) == 'echo'
    assert s(echo(None)) == 'echo'
    assert s(echo('')) == 'echo'
    assert s(echo('Test')) == 'echo Test'
    assert s(echo('Test', None)) == 'echo Test'
    assert s(echo('Test', '')) == 'echo Test'
    assert s(echo('Test', '123')) == 'echo Test 123'

def test_echo_fatal():
    # TODO: Break up tests into individual test methods
    assert s(echo_fatal()) == 'echo "FATAL: "'
    assert s(echo_fatal(None)) == 'echo "FATAL: "'
    assert s(echo_fatal('')) == 'echo "FATAL: "'
    assert s(echo_fatal('Test')) == 'echo "FATAL: Test"'
    assert s(echo_fatal('Test', None)) == 'echo "FATAL: Test"'
    assert s(echo_fatal('Test', '')) == 'echo "FATAL: Test"'
    assert s(echo_fatal('Test', '123')) == 'echo "FATAL: Test123"'

def test_echo_info():
    # TODO: Break up tests into individual test methods
    assert s(echo_info()) == 'echo "INFO:  "'
    assert s(echo_info(None)) == 'echo "INFO:  "'
    assert s(echo_info('')) == 'echo "INFO:  "'
    assert s(echo_info('Test')) == 'echo "INFO:  Test"'
    assert s(echo_info('Test', None)) == 'echo "INFO:  Test"'
    assert s(echo_info('Test', '')) == 'echo "INFO:  Test"'
    assert s(echo_info('Test', '123')) == 'echo "INFO:  Test123"'

def test_echo_trace():
    # TODO: Break up tests into individual test methods
    assert s(echo_trace()) == 'echo "TRACE: "'
    assert s(echo_trace(None)) == 'echo "TRACE: "'
    assert s(echo_trace('')) == 'echo "TRACE: "'
    assert s(echo_trace('Test')) == 'echo "TRACE: Test"'
    assert s(echo_trace('Test', None)) == 'echo "TRACE: Test"'
    assert s(echo_trace('Test', '')) == 'echo "TRACE: Test"'
    assert s(echo_trace('Test', '123')) == 'echo "TRACE: Test123"'

def test_echo_warn():
    # TODO: Break up tests into individual test methods
    assert s(echo_warn()) == 'echo "WARN:  "'
    assert s(echo_warn(None)) == 'echo "WARN:  "'
    assert s(echo_warn('')) == 'echo "WARN:  "'
    assert s(echo_warn('Test')) == 'echo "WARN:  Test"'
    assert s(echo_warn('Test', None)) == 'echo "WARN:  Test"'
    assert s(echo_warn('Test', '')) == 'echo "WARN:  Test"'
    assert s(echo_warn('Test', '123')) == 'echo "WARN:  Test123"'

def test_elif_():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): elif_()
    with raises(AssertionError): elif_(None)
    with raises(AssertionError): elif_('')
    with raises(AssertionError): elif_('Test')
    with raises(AssertionError): elif_('Test', None)
    with raises(AssertionError): elif_('Test', '')
    assert s(elif_('Test', '123')) == 'elif Test ; then\n123'

def test_else_():
    # TODO: Break up tests into individual test methods
    with raises(AssertionError): else_()
    with raises(AssertionError): else_(None)
    with raises(AssertionError): else_('')
    assert s(else_('Test')) == 'else\nTest'
    assert s(else_('Test', None)) == 'else\nTest'
    assert s(else_('Test', '')) == 'else\nTest'
    assert s(else_('Test', '123')) == 'else\nTest123'

def test_exit():
    # TODO: Break up tests into individual test methods
    assert s(exit()) == 'exit'
    assert s(exit(None)) == 'exit'
    assert s(exit('')) == 'exit'
    assert s(exit('Test')) == 'exit Test'
    with raises(TypeError): exit('Test', None)

def test_export():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): export()
    with raises(AssertionError): export(None)
    with raises(AssertionError): export('')
    assert s(export('Test')) == 'export Test'
    assert s(export('Test', None)) == 'export Test'
    assert s(export('Test', '')) == 'export Test='
    assert s(export('Test', '123')) == 'export Test=123'

def test_fi():
    # TODO: Break up tests into individual test methods
    assert s(fi()) == 'fi\n'
    with raises(TypeError): fi(None)

def test_file_exists():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): file_exists()
    with raises(AssertionError): file_exists(None)
    with raises(AssertionError): file_exists('')
    assert s(file_exists('Test')) == '[[ -f "Test" ]]'
    with raises(TypeError): file_exists('Test', None)

def test_file_is_readable():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): file_is_readable()
    with raises(AssertionError): file_is_readable(None)
    with raises(AssertionError): file_is_readable('')
    assert s(file_is_readable('Test')) == '[[ -r "Test" ]]'
    with raises(TypeError): file_is_readable('Test', None)

def test_fix():
    # TODO: Break up tests into individual test methods
    assert s(fix()) == '# TODO: FIX: \n'
    assert s(fix(None)) == '# TODO: FIX: \n'
    assert s(fix('')) == '# TODO: FIX: \n'
    assert s(fix('Test')) == '# TODO: FIX: Test\n'
    assert s(fix('Test', None)) == '# TODO: FIX: Test\n'
    assert s(fix('Test', '')) == '# TODO: FIX: Test\n'
    assert s(fix('Test', '123')) == '# TODO: FIX: Test123\n'

def test_if_():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): if_()
    with raises(AssertionError): if_(None)
    with raises(AssertionError): if_('')
    with raises(AssertionError): if_('Test')
    with raises(AssertionError): if_('Test', None)
    with raises(AssertionError): if_('Test', '')
    assert s(if_('Test', '123')) == 'if Test ; then\n123'

def test_indent():
    # TODO: Break up tests into individual test methods
    assert s(indent()) == 4 * ' '
    with raises(TypeError): indent(None)

def test_integer_is_not_equal():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): integer_is_not_equal()
    with raises(TypeError): integer_is_not_equal(None)
    with raises(TypeError): integer_is_not_equal('')
    with raises(TypeError): integer_is_not_equal('Test')
    with raises(AssertionError): integer_is_not_equal('Test', None)
    with raises(AssertionError): integer_is_not_equal('Test', '')
    assert s(integer_is_not_equal('Test', 123)) == '[[ "Test" -ne 123 ]]'

def test_no():
    # TODO: Break up tests into individual test methods
    assert s(no()) == '# NO: \n'
    assert s(no(None)) == '# NO: \n'
    assert s(no('')) == '# NO: \n'
    assert s(no('Test')) == '# NO: Test\n'
    assert s(no('Test', None)) == '# NO: Test\n'
    assert s(no('Test', '')) == '# NO: Test\n'
    assert s(no('Test', '123')) == '# NO: Test123\n'

def test_note():
    # TODO: Break up tests into individual test methods
    assert s(note()) == '# NOTE: \n'
    assert s(note(None)) == '# NOTE: \n'
    assert s(note('')) == '# NOTE: \n'
    assert s(note('Test')) == '# NOTE: Test\n'
    assert s(note('Test', None)) == '# NOTE: Test\n'
    assert s(note('Test', '')) == '# NOTE: Test\n'
    assert s(note('Test', '123')) == '# NOTE: Test123\n'

def test_or_():
    # TODO: Break up tests into individual test methods
    assert s(or_()) == ' || '
    with raises(TypeError): or_(None)

def test_path_does_not_exist():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): path_does_not_exist()
    with raises(AssertionError): path_does_not_exist(None)
    with raises(AssertionError): path_does_not_exist('')
    assert s(path_does_not_exist('Test')) == '[[ ! -e "Test" ]]'
    with raises(TypeError): path_does_not_exist('Test', None)

def test_path_is_not_directory():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): path_is_not_directory()
    with raises(AssertionError): path_is_not_directory(None)
    with raises(AssertionError): path_is_not_directory('')
    assert s(path_is_not_directory('Test')) == '[[ ! -d "Test" ]]'
    with raises(TypeError): path_is_not_directory('Test', None)

def test_path_is_not_file():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): path_is_not_file()
    with raises(AssertionError): path_is_not_file(None)
    with raises(AssertionError): path_is_not_file('')
    assert s(path_is_not_file('Test')) == '[[ ! -f "Test" ]]'
    with raises(TypeError): path_is_not_file('Test', None)

def test_pipe():
    # TODO: Break up tests into individual test methods
    assert s(pipe()) == ' | '
    with raises(TypeError): pipe(None)

def test_remember_status():
    # TODO: Break up tests into individual test methods
    assert s(remember_status()) == 'Status=$?'
    with raises(TypeError): remember_status(None)

def test_report_exit_status():
    # TODO: Break up tests into individual test methods
    assert s(report_exit_status()) == 'echo "FATAL: Script exited with \'$Status\'"'
    with raises(TypeError): report_exit_status(None)

def test_research():
    # TODO: Break up tests into individual test methods
    assert s(research()) == '# TODO: RESEARCH: \n'
    assert s(research(None)) == '# TODO: RESEARCH: \n'
    assert s(research('')) == '# TODO: RESEARCH: \n'
    assert s(research('Test')) == '# TODO: RESEARCH: Test\n'
    assert s(research('Test', None)) == '# TODO: RESEARCH: Test\n'
    assert s(research('Test', '')) == '# TODO: RESEARCH: Test\n'
    assert s(research('Test', '123')) == '# TODO: RESEARCH: Test123\n'

def test_return_():
    # TODO: Break up tests into individual test methods
    assert s(return_()) == 'return'
    assert s(return_(None)) == 'return'
    assert s(return_('')) == 'return'
    assert s(return_('Test')) == 'return Test'
    with raises(TypeError): return_('Test', None)

def test_return_last_status():
    # TODO: Break up tests into individual test methods
    assert s(return_last_status()) == 'return $?'
    with raises(TypeError): return_last_status(None)

def test_return_status():
    # TODO: Break up tests into individual test methods
    assert s(return_status()) == 'return $Status'
    with raises(TypeError): return_status(None)

def test_rule():
    # TODO: Break up tests into individual test methods
    assert s(rule()) == 79 * '#' + '\n'
    with raises(TypeError): rule(None)

def test_seq():
    # TODO: Break up tests into individual test methods
    assert s(seq()) == ' ; '
    with raises(TypeError): seq(None)

def test_set_():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): set_()
    assert s(set_(None)) == 'set'
    assert s(set_('')) == 'set'
    assert s(set_('Test')) == 'set Test'
    with raises(TypeError): set_('Test', None)

def test_shebang_bash():
    # TODO: Break up tests into individual test methods
    assert s(shebang_bash()) == '#!/usr/bin/env bash\n'
    with raises(TypeError): shebang_bash(None)

def test_someday():
    # TODO: Break up tests into individual test methods
    assert s(someday()) == '# TODO: SOMEDAY: \n'
    assert s(someday(None)) == '# TODO: SOMEDAY: \n'
    assert s(someday('')) == '# TODO: SOMEDAY: \n'
    assert s(someday('Test')) == '# TODO: SOMEDAY: Test\n'
    assert s(someday('Test', None)) == '# TODO: SOMEDAY: Test\n'
    assert s(someday('Test', '')) == '# TODO: SOMEDAY: Test\n'
    assert s(someday('Test', '123')) == '# TODO: SOMEDAY: Test123\n'

def test_source():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): source()
    with raises(AssertionError): source(None)
    with raises(AssertionError): source('')
    assert s(source('Test')) == 'source Test'
    with raises(TypeError): source('Test', None)

def test_status_is_failure():
    # TODO: Break up tests into individual test methods
    assert s(status_is_failure()) == '[[ "$Status" -ne 0 ]]'
    with raises(TypeError): status_is_failure(None)

def test_string_equals():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): string_equals()
    with raises(TypeError): string_equals(None)
    with raises(TypeError): string_equals('')
    with raises(TypeError): string_equals('Test')
    with raises(AssertionError): string_equals('Test', None)
    with raises(AssertionError): string_equals('Test', '')
    assert s(string_equals('Test', '123')) == '[[ "Test" == "123" ]]'

def test_string_is_not_null():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): string_is_not_null()
    with raises(AssertionError): string_is_not_null(None)
    with raises(AssertionError): string_is_not_null('')
    assert s(string_is_not_null('Test')) == '[[ -n "Test" ]]'
    with raises(TypeError): string_is_not_null('Test', None)

def test_string_is_null():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): string_is_null()
    with raises(AssertionError): string_is_null(None)
    with raises(AssertionError): string_is_null('')
    assert s(string_is_null('Test')) == '[[ -z "Test" ]]'
    with raises(TypeError): string_is_null('Test', None)

def test_substitute():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): substitute()
    with raises(AssertionError): substitute(None)
    with raises(AssertionError): substitute('')
    assert s(substitute('Test')) == '$(Test)'
    assert s(substitute('Test', None)) == '$(Test)'
    assert s(substitute('Test', '')) == '$(Test)'
    assert s(substitute('Test', '123')) == '$(Test 123)'

def test_todo():
    # TODO: Break up tests into individual test methods
    assert s(todo()) == '# TODO: \n'
    assert s(todo(None)) == '# TODO: \n'
    assert s(todo('')) == '# TODO: \n'
    assert s(todo('Test')) == '# TODO: Test\n'
    assert s(todo('Test', None)) == '# TODO: Test\n'
    assert s(todo('Test', '')) == '# TODO: Test\n'
    assert s(todo('Test', '123')) == '# TODO: Test123\n'

def test_vn():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): vn()
    with raises(AssertionError): vn(None)
    with raises(AssertionError): vn('')
    assert s(vn('Test')) == 'Test'
    with raises(TypeError): vn('Test', None)

def test_vr():
    # TODO: Break up tests into individual test methods
    with raises(TypeError): vr()
    with raises(AssertionError): vr(None)
    with raises(AssertionError): vr('')
    assert s(vr('Test')) == '$Test'
    with raises(TypeError): vr('Test', None)


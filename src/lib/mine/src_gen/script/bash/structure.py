#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages  (absolute references, distributed with Python)
# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
from utility.my_assert import assert_instance
from utility.my_assert import assert_not_none
# Co-located modules (relative references, NOT packaged, in project)
from ..source import my_visitor_map
from ..structure import *
from ..structure import _Command


###############################################################################

def and_(): return ' && '

def bs(): return ['\\', eol()]

def indent(): return '    '

def or_(): return ' || '

def pipe(): return ' | '

def seq(): return ' ; '

###############################################################################

def echo(*argument):
    return command('echo', argument)

def echo_fatal(*element):
    return echo(dq('FATAL: ', element))

def echo_info(*element):
    return echo(dq('INFO:  ', element))

def echo_trace(*element):
    return echo(dq('TRACE: ', element))

def echo_warn(*element):
    return echo(dq('WARN:  ', element))

###############################################################################

def cc(command_embedded_within_comment):
    assert assert_instance(command_embedded_within_comment, _Command)
    return bt(command_embedded_within_comment)

def debugging_comment():
    return [
        note('Uncomment the following two lines for debugging'),
        comment(set_('-o', 'verbose')),
        comment(set_('-o', 'xtrace')),
    ]

def disabled_content_footer():
    return [
        line(),
        rule(),
        command(':', '<<', sq('DisabledContent')), eol(),
        line('DisabledContent'),
        line(),
    ]

###############################################################################

def exit(argument=None):
    return command('exit', argument)

def return_(argument=None):
    return command('return', argument)

def return_last_status():
    return return_('$?')

###############################################################################

def remember_status():
    return assign(vn('Status'), '$?')

def report_exit_status():
    return echo_fatal('Script exited with ', sq(vr('Status')))

def return_status():
    return return_(vr('Status'))

def status_is_failure():
    return integer_is_not_equal(vr('Status'), 0)

###############################################################################

def set_(argument):
    return command('set', argument)

###############################################################################


class _Substitution(object):
    def __init__(self, command):
        super().__init__()
        assert assert_instance(command, _Command)
        self.command = command

    def __repr__(self):
        return "_Substitution({})".format(self.command)


@my_visitor_map.register(_Substitution)
def _visit_substitution(element, walker):
    walker.emit('$(')
    walker.walk(element.command)
    walker.emit(')')

def substitute(executable, *argument):
    return _Substitution(command(executable, argument))

###############################################################################


class _Assign(object):
    def __init__(self, variable, *expression):
        super().__init__()
        self.variable = squashed(variable)
        self.expressions = squashed(expression)

    def __repr__(self):
        return "_Assign({}, {})".format(self.variable, self.expressions)


@my_visitor_map.register(_Assign)
def _visit_assign(element, walker):
    walker.walk(element.variable)
    walker.emit('=')
    walker.walk(element.expressions)

def assign(variable, *expression):
    return _Assign(variable, expression)

def export(variable, expression=None):
    if expression is None:
        return command('export', variable)
    else:
        return command('export', assign(variable, expression))

###############################################################################

def condition(executable, *argument):
    return command(executable, argument)

def directory_exists(directory_name):
    return condition('[[', '-d', dq(directory_name), ']]')

def file_exists(file_name):
    return condition('[[', '-f', dq(file_name), ']]')

def file_is_readable(file_name):
    return condition('[[', '-r', dq(file_name), ']]')

def integer_is_not_equal(left, right):
    return condition('[[', dq(left), '-ne', right, ']]')

def path_does_not_exist(path_name):
    return condition('[[', '!', '-e', dq(path_name), ']]')

def path_is_not_directory(path_name):
    return condition('[[', '!', '-d', dq(path_name), ']]')

def path_is_not_file(path_name):
    return condition('[[', '!', '-f', dq(path_name), ']]')

def string_equals(left, right):
    return condition('[[', dq(left), '==', dq(right), ']]')

def string_is_not_null(expression):
    return condition('[[', '-n', dq(expression), ']]')

def string_is_null(expression):
    return condition('[[', '-z', dq(expression), ']]')

###############################################################################


class _Else(object):
    def __init__(self, *statement):
        super().__init__()
        self.statements = squashed(statement)
        assert assert_not_none(self.statements)

    def __repr__(self):
        return "_Else({})".format(self.statements)


@my_visitor_map.register(_Else)
def _visit_else(element, walker):
    walker.emit('else')
    walker.walk(eol())
    walker.walk(element.statements)


def else_(*statement):
    return _Else(statement)

###############################################################################


class _ElseIf(object):
    def __init__(self, condition, *statement):
        super().__init__()
        self.condition = squashed(condition)
        assert assert_not_none(self.condition)
        self.statements = squashed(statement)
        assert assert_not_none(self.statements)

    def __repr__(self):
        return "_ElseIf({}, {})".format(self.condition, self.statements)


@my_visitor_map.register(_ElseIf)
def _visit_elif(element, walker):
    walker.emit('elif ')
    walker.walk(element.condition)
    walker.walk(seq())
    walker.emit('then')
    walker.walk(eol())
    walker.walk(element.statements)

def elif_(condition, *statement):
    return _ElseIf(condition, statement)

###############################################################################


class _Fi(object):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "_Fi()"


@my_visitor_map.register(_Fi)
def _visit_fi(element, walker):
    walker.emit('fi')
    walker.walk(eol())

def fi():
    return _Fi()

###############################################################################


class _If(object):
    def __init__(self, condition, *statement):
        super().__init__()
        self.condition = squashed(condition)
        assert assert_not_none(self.condition)
        self.statements = squashed(statement)
        assert assert_not_none(self.statements)

    def __repr__(self):
        return "_If({}, {})".format(self.condition, self.statements)


@my_visitor_map.register(_If)
def _visit_if(element, walker):
    walker.emit('if ')
    walker.walk(element.condition)
    walker.walk(seq())
    walker.emit('then')
    walker.walk(eol())
    walker.walk(element.statements)

def if_(condition, *statement):
    return _If(condition, statement)

###############################################################################

def executed_header():
    return [
        shebang_bash(),
#       execution_trace(),
        no(set_('-e')),
        disabled(set_('-x')),
        comment('Intended to be executed directly by the user.'),
        rule(),
    ]

def shebang_bash():
    return shebang_thru_env('bash')

def shebang_sourced():
    return shebang_false()

def source(file_name):
    return command('source', file_name)

def sourced_header():
    return [
        shebang_sourced(),
#       execution_trace(),
        no(set_('-e')),
        disabled(set_('-x')),
        comment('Intended to be sourced in a BASH shell by the user.'),
        rule(),
    ]

###############################################################################


class _VariableName(object):
    def __init__(self, name):
        super().__init__()
        self.name = squashed(name)

    def __repr__(self):
        return "_VariableName({})".format(self.name)


@my_visitor_map.register(_VariableName)
def _visit_variable_name(element, walker):
    walker.walk(element.name)

def vn(name):
    return _VariableName(name)


class _VariableReference(object):
    def __init__(self, name):
        super().__init__()
        self.name = squashed(name)

    def __repr__(self):
        return "_VariableReference({})".format(self.name)


@my_visitor_map.register(_VariableReference)
def _visit_variable_reference(element, walker):
    walker.emit('$')
    walker.walk(element.name)

def vr(name):
    return _VariableReference(name)

'''DisabledContent
'''


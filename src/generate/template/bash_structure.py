# TODO: RESEARCH: Does this need conversion for Python3?
import itertools

from .bash_script      import visitor_map
from .script_structure import *
from .script_structure import _Command
from .script_structure import _Shebang
from .script_structure import _Statement


####################################################################################################

def and_(): return ' && '

def eol(): return '\n'

def indent(): return '    '

def line(text=None): return [text, eol()]

def nl(): return line('\\')

def or_(): return ' || '

def pipe(): return ' | '

def seq(): return ' ; '

def then(): return 'then'

####################################################################################################

def echo(*argument):
    return command('echo', *argument)

def echo_fatal(*elements):
    return echo(dq('FATAL: ', *elements))

def echo_info(*elements):
    return echo(dq('INFO:  ', *elements))

def echo_trace(*elements):
    return echo(dq('TRACE: ', *elements))

def echo_warn(*elements):
    return echo(dq('WARN:  ', *elements))

####################################################################################################

def debugging_comment():
    return [
        note('Uncomment the following two lines for debugging'),
        comment(set('-o', 'verbose')),
        comment(set('-o', 'xtrace')),
    ]

def disabled_content_footer():
    return [
        line(),
        rule(),
        command(':', '<<', sq('DisabledContent')), eol(),
        line('DisabledContent'),
        line(),
    ]

def note(*elements):
    return comment('NOTE: ', *elements)

def rule():
    # TODO: Make line length configurable
    return line('#' * 79)

def someday(*elements):
    return todo('SOMEDAY: ', *elements)

def todo(*elements):
    return comment('TODO: ', *elements)

####################################################################################################

def exit(*argument):
    return command('exit', *argument)

def remember_status():
    return assign(vn('Status'), '$?')

def report_status():
    return echo_fatal('Script exited with ', sq(vr('Status')))

def return_(status):
    return command('return', status)

def return_last_status():
    return return_('$?')

def return_status():
    return return_(vr('Status'))

def status_is_failure():
    return integer_is_not_equal(dq(vr('Status')), 0)

####################################################################################################

def set(*argument):
    return command('set', *argument)

####################################################################################################

def source(file_name):
    return command('source', file_name)

def sourced_header():
    return [
        shebang_sourced(),
        note('Intended to be sourced into a BASH shell by the user.'),
#       execution_trace(),
        rule(),
    ]

####################################################################################################

class _Substitution(_Command):
    def __init__(self, command, *argument):
        _Command.__init__(self, command, *argument)

@visitor_map.register(_Substitution)
def _visit_substitution(element, walker):
    walker.emit('$(')
    walker.walk(element.command)
    walker.walk(element.arguments)
    walker.emit(')')

def substitute(command, *argument):
    return _Substitution(command, *argument)

####################################################################################################

class _Assign(_Statement):
    def __init__(self, variable, *expression):
        self.expressions = expression
        self.variable = variable

@visitor_map.register(_Assign)
def _visit_assign(element, walker):
    walker.walk(element.variable)
    walker.emit('=')
    walker.walk(element.expressions)

def assign(variable, *expression):
    return _Assign(variable, *expression)

def export(variable, expression=None):
    if expression is None:
        return command('export', variable)
    else:
        return command('export', _Assign(variable, expression))

####################################################################################################

class _Condition(_Command):
    def __init__(self, *argument):
        _Command.__init__(self, *argument)

def directory_exists(directory_name):
    return _Condition('[[', '-d', dq(directory_name), ']]')

def file_exists(file_name):
    return _Condition('[[', '-f', dq(file_name), ']]')

def integer_is_not_equal(left, right):
    return _Condition('[[', left, '-ne', right, ']]')

def path_does_not_exist(path_name):
    return _Condition('[[', '!', '-e', dq(path_name), ']]')

def path_is_not_directory(path_name):
    return _Condition('[[', '!', '-d', dq(path_name), ']]')

def path_is_not_file(path_name):
    return _Condition('[[', '!', '-f', dq(path_name), ']]')

def string_is_not_null(expression):
    return _Condition('[[', '-n', dq(expression), ']]')

def string_is_null(expression):
    return _Condition('[[', '-z', dq(expression), ']]')

####################################################################################################

class _DoubleQuoted(object):
    def __init__(self, *element):
        object.__init__(self)
        self.content = element

@visitor_map.register(_DoubleQuoted)
def _visit_double_quoted(element, walker):
    walker.emit('"')
    walker.walk(element.content)
    walker.emit('"')

def dq(*element):
    return _DoubleQuoted(*element)

####################################################################################################

class _Else(object):
    def __init__(self, *statement):
        object.__init__(self)
        self.statements = statement

@visitor_map.register(_Else)
def _visit_else(element, walker):
    walker.emit('else')
    walker.emit(eol())
    walker.walk(element.statements)

def else_(*statement):
    return _Else(*statement)

####################################################################################################

class _ElseIf(object):
    def __init__(self, condition, *statement):
        object.__init__(self)
        self.condition = condition
        self.statements = statement

@visitor_map.register(_ElseIf)
def _visit_elif(element, walker):
    walker.emit('elif ')
    walker.walk(element.condition)
    walker.emit(seq())
    walker.emit(then())
    walker.emit(eol())
    walker.walk(element.statements)

def elif_(condition, *statement):
    return _ElseIf(condition, *statement)

####################################################################################################

class _Fi(object):
    def __init__(self):
        object.__init__(self)

@visitor_map.register(_Fi)
def _visit_fi(element, walker):
    walker.emit('fi')
    walker.emit(eol())

def fi():
    return _Fi()

####################################################################################################

class _FileSystemPath(object):
    def __init__(self, *element):
        object.__init__(self)
        self.elements = element

@visitor_map.register(_FileSystemPath)
def _visit_file_system_path(element, walker):
    if element.elements is not None:
        past_first = False
        for e in element.elements:
            if past_first: walker.emit('/')
            walker.walk(e)
            past_first = True

def path(*element):
    return _FileSystemPath(*element)

####################################################################################################

class _If(object):
    def __init__(self, condition, *statement):
        object.__init__(self)
        self.condition = condition
        self.statements = statement

@visitor_map.register(_If)
def _visit_if(element, walker):
    walker.emit('if ')
    walker.walk(element.condition)
    walker.emit(seq())
    walker.emit(then())
    walker.emit(eol())
    walker.walk(element.statements)

def if_(condition, *statement):
    return _If(condition, *statement)

####################################################################################################

def shebang_bash():
    return shebang_thru_env('bash')

def shebang_sourced():
    return shebang_false()

####################################################################################################

class _SingleQuoted(object):
    def __init__(self, *element):
        object.__init__(self)
        self.content = element

@visitor_map.register(_SingleQuoted)
def _visit_single_quoted(element, walker):
    walker.emit("'")
    walker.walk(element.content)
    walker.emit("'")

def sq(*element):
    return _SingleQuoted(*element)

####################################################################################################

class _Variable(object):
    def __init__(self, variable_name):
        object.__init__(self)
        self.name = variable_name

@visitor_map.register(_Variable)
def _visit_variable(element, walker):
    walker.walk(element.name)

def vn(variable_name):
    return _Variable(variable_name)

####################################################################################################

class _VariableReference(object):
    def __init__(self, variable_name):
        object.__init__(self)
        self.name = variable_name

@visitor_map.register(_VariableReference)
def _visit_variable_reference(element, walker):
    walker.emit('$')
    walker.walk(element.name)

def vr(variable_name):
    return _VariableReference(variable_name)

####################################################################################################

""" Disabled content
"""


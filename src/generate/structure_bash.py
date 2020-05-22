# TODO: RESEARCH: Does this need conversion for Python3?
import itertools

from .script_bash      import visitor_map
from .structure_script import *
from .structure_script import _Statement


####################################################################################################

def and_():
    return ' && '

def eol():
    return '\n'

def line(text=None):
    return [text, eol()]

def nl():
    return line('\\')

def or_():
    return ' || '

def pipe():
    return ' | '

def seq():
    return ' ; '

def then():
    return 'then'

####################################################################################################

class _Arguments(object):
    def __init__(self, *argument):
        object.__init__(self)
        self.arguments = argument

@visitor_map.register(_Arguments)
def visit_arguments(element, walker):
    if element.arguments is not None:
        for a in element.arguments:
            walker.emit(' ')
            walker.walk(a)

class _Command(_Statement):
    def __init__(self, command, *argument):
        _Statement.__init__(self, '_Command')
        self.arguments = _Arguments(*argument)
        self.command = command

@visitor_map.register(_Command)
def visit_command(element, walker):
    walker.walk(element.command)
    walker.walk(element.arguments)

class _Substitution(_Command):
    def __init__(self, command, *argument):
        _Command.__init__(self, command, *argument)

@visitor_map.register(_Substitution)
def visit_substitution(element, walker):
    walker.emit('$(')
    walker.walk(element.command)
    walker.walk(element.arguments)
    walker.emit(')')

def command(command, *argument):
    return _Command(command, *argument)

def echo(*argument):
    return command('echo', *argument)

def exit(*argument):
    return command('exit', *argument)

def return_(status):
    return command('return', status)

def return_last_status():
    return return_('$?')

def set(*argument):
    return command('set', *argument)

def source(file_name):
    return command('source', file_name)

def substitute(command, *argument):
    return _Substitution(command, *argument)

####################################################################################################

class _Assign(_Command):
    def __init__(self, command, variable, *expression):
        self.command = command
        self.expressions = expression
        self.variable = variable

@visitor_map.register(_Assign)
def visit_assign(element, walker):
    if element.command is not None:
        walker.walk(element.command)
        walker.emit(' ')
    walker.walk(element.variable)
    walker.emit('=')
    walker.walk(element.expressions)

def assign(variable, *expression):
    return _Assign(None, variable, *expression)

def export(variable, *expression):
    return _Assign('export', variable, *expression)

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
def visit_double_quoted(element, walker):
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
def visit_else(element, walker):
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
def visit_elif(element, walker):
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
def visit_fi(element, walker):
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
def visit_file_system_path(element, walker):
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
def visit_if(element, walker):
    walker.emit('if ')
    walker.walk(element.condition)
    walker.emit(seq())
    walker.emit(then())
    walker.emit(eol())
    walker.walk(element.statements)

def if_(condition, *statement):
    return _If(condition, *statement)

####################################################################################################

def shebang_execute():
    return _Shebang(_Command(path('/bin', 'bash')))

def shebang_source():
    return _Shebang(_Command(path('/bin', 'cat')))

####################################################################################################

class _SingleQuoted(object):
    def __init__(self, *element):
        object.__init__(self)
        self.content = element

@visitor_map.register(_SingleQuoted)
def visit_single_quoted(element, walker):
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
def visit_variable(element, walker):
    walker.walk(element.name)

def vn(variable_name):
    return _Variable(variable_name)

####################################################################################################

class _VariableReference(object):
    def __init__(self, variable_name):
        object.__init__(self)
        self.name = variable_name

@visitor_map.register(_VariableReference)
def visit_variable_reference(element, walker):
    walker.emit('$')
    walker.walk(element.name)

def vr(variable_name):
    return _VariableReference(variable_name)

####################################################################################################

""" Disabled content
"""


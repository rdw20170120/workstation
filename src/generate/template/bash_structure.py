from .bash_script      import visitor_map
from .script_structure import *
from .script_structure import _Command
from .script_structure import _Shebang
from .script_structure import _Statement

###############################################################################

def and_(): return ' && '

def bs(): return eol('\\')

def indent(): return '    '

def or_(): return ' || '

def pipe(): return ' | '

def seq(): return ' ; '

def then(): return 'then'

###############################################################################

def echo(*argument):
    return command('echo', *argument)

def echo_fatal(*element):
    return echo(dq('FATAL: ', *element))

def echo_info(*element):
    return echo(dq('INFO:  ', *element))

def echo_trace(*element):
    return echo(dq('TRACE: ', *element))

def echo_warn(*element):
    return echo(dq('WARN:  ', *element))

###############################################################################

def debugging_comment():
    return [
        note('Uncomment the following two lines for debugging'),
        comment(set('-o', 'verbose')),
        comment(set('-o', 'xtrace')),
    ]

def disabled(*element):
    return comment('DISABLED: ', *element)

def disabled_content_footer():
    return [
        line(),
        rule(),
        command(':', '<<', sq('DisabledContent')), eol(),
        line('DisabledContent'),
        line(),
    ]

def no(*element):
    return note('NO: ', *element)

def note(*element):
    return comment('NOTE: ', *element)

def rule():
    # TODO: Make line length configurable
    return line('#' * 79)

def someday(*element):
    return todo('SOMEDAY: ', *element)

def todo(*element):
    return comment('TODO: ', *element)

###############################################################################

def exit(*argument):
    return command('exit', *argument)

def return_(*argument):
    return command('return', *argument)

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
    return integer_is_not_equal(dq(vr('Status')), 0)

###############################################################################

def set_(*argument):
    return command('set', *argument)

###############################################################################

def source(file_name):
    return command('source', file_name)

def sourced_header():
    return [
        shebang_sourced(),
        note('Intended to be sourced into a BASH shell by the user.'),
#       execution_trace(),
        rule(),
    ]

###############################################################################

class _Substitution(_Command):
    def __init__(self, command, *argument):
        super().__init__(command, *argument)

@visitor_map.register(_Substitution)
def _visit_substitution(element, walker):
    walker.emit('$(')
    walker.walk(element.command)
    walker.walk(element.arguments)
    walker.emit(')')

def substitute(command, *argument):
    return _Substitution(command, *argument)

###############################################################################

class _Assign(object):
    def __init__(self, variable, *expression):
        super().__init__()
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

###############################################################################

class _Condition(_Command):
    def __init__(self, *argument):
        super().__init__(*argument)

def directory_exists(directory_name):
    return _Condition('[[', '-d', dq(directory_name), ']]')

def file_exists(file_name):
    return _Condition('[[', '-f', dq(file_name), ']]')

def file_is_readable(file_name):
    return _Condition('[[', '-r', dq(file_name), ']]')

def integer_is_not_equal(left, right):
    return _Condition('[[', left, '-ne', right, ']]')

def path_does_not_exist(path_name):
    return _Condition('[[', '!', '-e', dq(path_name), ']]')

def path_is_not_directory(path_name):
    return _Condition('[[', '!', '-d', dq(path_name), ']]')

def path_is_not_file(path_name):
    return _Condition('[[', '!', '-f', dq(path_name), ']]')

def string_equals(left, right):
    return _Condition('[[', dq(left), '==', dq(right), ']]')

def string_is_not_null(expression):
    return _Condition('[[', '-n', dq(expression), ']]')

def string_is_null(expression):
    return _Condition('[[', '-z', dq(expression), ']]')

###############################################################################

class _Else(object):
    def __init__(self, *statement):
        super().__init__()
        self.statements = statement

@visitor_map.register(_Else)
def _visit_else(element, walker):
    walker.emit('else')
    walker.emit('\n')
    walker.walk(element.statements)

def else_(*statement):
    return _Else(*statement)

###############################################################################

class _ElseIf(object):
    def __init__(self, condition, *statement):
        super().__init__()
        self.condition = condition
        self.statements = statement

@visitor_map.register(_ElseIf)
def _visit_elif(element, walker):
    walker.emit('elif ')
    walker.walk(element.condition)
    walker.emit(seq())
    walker.emit(then())
    walker.emit('\n')
    walker.walk(element.statements)

def elif_(condition, *statement):
    return _ElseIf(condition, *statement)

###############################################################################

class _Fi(object):
    def __init__(self):
        super().__init__()

@visitor_map.register(_Fi)
def _visit_fi(element, walker):
    walker.emit('fi')
    walker.emit('\n')

def fi():
    return _Fi()

###############################################################################

class _FileSystemPath(object):
    def __init__(self, *element):
        super().__init__()
        self.element = element

@visitor_map.register(_FileSystemPath)
def _visit_file_system_path(element, walker):
    if element.element is not None:
        past_first = False
        for e in element.element:
            if past_first: walker.emit('/')
            walker.walk(e)
            past_first = True

def path(*element):
    return _FileSystemPath(*element)

###############################################################################

class _If(object):
    def __init__(self, condition, *statement):
        super().__init__()
        self.condition = condition
        self.statements = statement

@visitor_map.register(_If)
def _visit_if(element, walker):
    walker.emit('if ')
    walker.walk(element.condition)
    walker.emit(seq())
    walker.emit(then())
    walker.emit('\n')
    walker.walk(element.statements)

def if_(condition, *statement):
    return _If(condition, *statement)

###############################################################################

def shebang_bash():
    return shebang_thru_env('bash')

def shebang_sourced():
    return shebang_false()

###############################################################################

class _Variable(object):
    def __init__(self, variable_name):
        super().__init__()
        self.name = variable_name

@visitor_map.register(_Variable)
def _visit_variable(element, walker):
    walker.walk(element.name)

def vn(variable_name):
    return _Variable(variable_name)

###############################################################################

class _VariableReference(object):
    def __init__(self, variable_name):
        super().__init__()
        self.name = variable_name

@visitor_map.register(_VariableReference)
def _visit_variable_reference(element, walker):
    walker.emit('$')
    walker.walk(element.name)

def vr(variable_name):
    return _VariableReference(variable_name)

###############################################################################

''' Disabled content
'''

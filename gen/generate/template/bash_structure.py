from .bash_script       import visitor_map
from .content_structure import _ContentElement
from .script_structure  import *
from .script_structure  import _Command
from .script_structure  import _Shebang


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

def debugging_comment():
    return [
        note('Uncomment the following two lines for debugging'),
        comment(set_('-o', 'verbose')),
        comment(set_('-o', 'xtrace')),
    ]

def disabled(*element):
    return comment('DISABLED: ', element)

def disabled_content_footer():
    return [
        line(),
        rule(),
        command(':', '<<', sq('DisabledContent')), eol(),
        line('DisabledContent'),
        line(),
    ]

def fix(*element):
    return todo('FIX: ', element)

def no(*element):
    return comment('NO: ', element)

def note(*element):
    return comment('NOTE: ', element)

def rule():
    # TODO: Make line length configurable
    return line('#' * 79)

def research(*element):
    return todo('RESEARCH: ', element)

def someday(*element):
    return todo('SOMEDAY: ', element)

def todo(*element):
    return comment('TODO: ', element)

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

def source(file_name):
    assert file_name
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
    def __init__(self, command, arguments, typename='_Substitution'):
        super().__init__(command, arguments, typename)


@visitor_map.register(_Substitution)
def _visit_substitution(element, walker):
    walker.emit('$(')
    walker.walk(element.command)
    walker.walk(element.arguments)
    walker.emit(')')

def substitute(command, *argument):
    return _Substitution(command, argument)

###############################################################################


class _Assign(_ContentElement):
    def __init__(self, variable, expressions, typename='_Assign'):
        super().__init__(None, typename)
        assert variable
        self.expressions = expressions
        self.variable = variable


@visitor_map.register(_Assign)
def _visit_assign(element, walker):
    walker.walk(element.variable)
    walker.emit('=')
    walker.walk(element.expressions)

def assign(variable, *expression):
    return _Assign(variable, expression)

def export(variable, expression=None):
    assert variable
    if expression is None:
        return command('export', variable)
    else:
        return command('export', assign(variable, expression))

###############################################################################


class _Condition(_Command):
    def __init__(self, command, argument, typename='_Condition'):
        super().__init__(command, argument, typename)


def condition(command, *argument):
    return _Condition(command, argument)

def directory_exists(directory_name):
    assert directory_name
    return condition('[[', '-d', dq(directory_name), ']]')

def file_exists(file_name):
    assert file_name
    return condition('[[', '-f', dq(file_name), ']]')

def file_is_readable(file_name):
    assert file_name
    return condition('[[', '-r', dq(file_name), ']]')

def integer_is_not_equal(left, right):
    assert left
    assert right is not None and right != ''
    return condition('[[', dq(left), '-ne', right, ']]')

def path_does_not_exist(path_name):
    assert path_name
    return condition('[[', '!', '-e', dq(path_name), ']]')

def path_is_not_directory(path_name):
    assert path_name
    return condition('[[', '!', '-d', dq(path_name), ']]')

def path_is_not_file(path_name):
    assert path_name
    return condition('[[', '!', '-f', dq(path_name), ']]')

def string_equals(left, right):
    assert left is not None and left != ''
    assert right is not None and right != ''
    return condition('[[', dq(left), '==', dq(right), ']]')

def string_is_not_null(expression):
    assert expression
    return condition('[[', '-n', dq(expression), ']]')

def string_is_null(expression):
    assert expression
    return condition('[[', '-z', dq(expression), ']]')

###############################################################################

def else_(*statement):
    statement = squashed(statement)
    assert statement
    assert len(statement)
    return _ContentElement(['else', eol(), statement])

###############################################################################


class _ElseIf(_Command):
    def __init__(self, condition, statement, typename='_ElseIf'):
        super().__init__(condition, statement, typename)
        self.condition = condition
        self.statements = statement


@visitor_map.register(_ElseIf)
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


class _Fi(_ContentElement):
    def __init__(self, typename='_Fi'):
        super().__init__(['fi', eol()], typename)


def fi():
    return _Fi()

###############################################################################


class _If(_Command):
    def __init__(self, condition, statement, typename='_If'):
        super().__init__(condition, statement, typename)
        self.condition = condition
        self.statements = statement


@visitor_map.register(_If)
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

def shebang_bash():
    return shebang_thru_env('bash')

def shebang_sourced():
    return shebang_false()

###############################################################################

def vn(variable_name):
    assert variable_name
    return _ContentElement(variable_name, typename='vn')

def vr(variable_name):
    assert variable_name
    return _ContentElement(['$', variable_name], typename='vr')


''' Disabled content
'''


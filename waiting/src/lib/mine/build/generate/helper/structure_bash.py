import itertools

from .script_bash import VISITOR_MAP


####################################################################################################


def flatten_via_chain(list_):
    return list(itertools.chain.from_iterable(*list_))


def flatten(sequence, types=(list, tuple)):
    """Flatten sequence made of types, returned as the same outer type as sequence.
    REF: http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
    """
    sequence_type = type(sequence)
    sequence = list(sequence)
    i = 0
    while i < len(sequence):
        while isinstance(sequence[i], types):
            if not sequence[i]:
                sequence.pop(i)
                i -= 1
                break
            else:
                sequence[i : i + 1] = sequence[i]
        i += 1
    return sequence_type(sequence)


####################################################################################################


def and_():
    return " && "


def eol():
    return "\n"


def line(text=None):
    return [text, eol()]


def nl():
    return line("\\")


def or_():
    return " || "


def pipe():
    return " | "


def seq():
    return " ; "


def then():
    return "then"


####################################################################################################


class _Statement(object):
    def __init__(self, statement):
        object.__init__(self)
        self.statement = statement


@VISITOR_MAP.register(_Statement)
def visit_statement(element, walker):
    walker.walk(element.statement)


####################################################################################################


class _Arguments(object):
    def __init__(self, *argument):
        object.__init__(self)
        self.arguments = argument


@VISITOR_MAP.register(_Arguments)
def visit_arguments(element, walker):
    if element.arguments is not None:
        for a in element.arguments:
            walker.emit(" ")
            walker.walk(a)


class _Command(_Statement):
    def __init__(self, command, *argument):
        _Statement.__init__(self, "_Command")
        self.arguments = _Arguments(*argument)
        self.command = command


@VISITOR_MAP.register(_Command)
def visit_command(element, walker):
    walker.walk(element.command)
    walker.walk(element.arguments)


class _Substitution(_Command):
    def __init__(self, command, *argument):
        _Command.__init__(self, command, *argument)


@VISITOR_MAP.register(_Substitution)
def visit_substitution(element, walker):
    walker.emit("$(")
    walker.walk(element.command)
    walker.walk(element.arguments)
    walker.emit(")")


def command(command, *argument):
    return _Command(command, *argument)


def echo(*argument):
    return command("echo", *argument)


def exit(*argument):
    return command("exit", *argument)


def return_(status):
    return command("return", status)


def return_last_status():
    return return_("$?")


def set(*argument):
    return command("set", *argument)


def source(file_name):
    return command("source", file_name)


def substitute(command, *argument):
    return _Substitution(command, *argument)


####################################################################################################


class _Assign(_Command):
    def __init__(self, command, variable, *expression):
        self.command = command
        self.expressions = expression
        self.variable = variable


@VISITOR_MAP.register(_Assign)
def visit_assign(element, walker):
    if element.command is not None:
        walker.walk(element.command)
        walker.emit(" ")
    walker.walk(element.variable)
    walker.emit("=")
    walker.walk(element.expressions)


def assign(variable, *expression):
    return _Assign(None, variable, *expression)


def export(variable, *expression):
    return _Assign("export", variable, *expression)


####################################################################################################


class _Comment(_Statement):
    def __init__(self, *element):
        _Statement.__init__(self, "_Comment")
        self.content = element


@VISITOR_MAP.register(_Comment)
def visit_comment(element, walker):
    walker.emit("#")
    if isinstance(element.content, tuple):
        if len(element.content) > 0:
            walker.emit(" ")
            walker.walk(element.content)
    walker.emit("\n")


def comment(*element):
    return _Comment(*element)


####################################################################################################


class _Condition(_Command):
    def __init__(self, *argument):
        _Command.__init__(self, *argument)


def directory_exists(directory_name):
    return _Condition("[[", "-d", dq(directory_name), "]]")


def file_exists(file_name):
    return _Condition("[[", "-f", dq(file_name), "]]")


def integer_is_not_equal(left, right):
    return _Condition("[[", left, "-ne", right, "]]")


def path_does_not_exist(path_name):
    return _Condition("[[", "!", "-e", dq(path_name), "]]")


def path_is_not_file(path_name):
    return _Condition("[[", "!", "-f", dq(path_name), "]]")


def string_is_not_null(expression):
    return _Condition("[[", "-n", dq(expression), "]]")


def string_is_null(expression):
    return _Condition("[[", "-z", dq(expression), "]]")


####################################################################################################


class _DoubleQuoted(object):
    def __init__(self, *element):
        object.__init__(self)
        self.content = element


@VISITOR_MAP.register(_DoubleQuoted)
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


@VISITOR_MAP.register(_Else)
def visit_else(element, walker):
    walker.emit("else")
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


@VISITOR_MAP.register(_ElseIf)
def visit_elif(element, walker):
    walker.emit("elif ")
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


@VISITOR_MAP.register(_Fi)
def visit_fi(element, walker):
    walker.emit("fi")
    walker.emit(eol())


def fi():
    return _Fi()


####################################################################################################


class _FileSystemPath(object):
    def __init__(self, *element):
        object.__init__(self)
        self.elements = element


@VISITOR_MAP.register(_FileSystemPath)
def visit_file_system_path(element, walker):
    if element.elements is not None:
        past_first = False
        for e in element.elements:
            if past_first:
                walker.emit("/")
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


@VISITOR_MAP.register(_If)
def visit_if(element, walker):
    walker.emit("if ")
    walker.walk(element.condition)
    walker.emit(seq())
    walker.emit(then())
    walker.emit(eol())
    walker.walk(element.statements)


def if_(condition, *statement):
    return _If(condition, *statement)


####################################################################################################


class _Shebang(_Comment):
    def __init__(self, content):
        _Comment.__init__(self, content)


@VISITOR_MAP.register(_Shebang)
def visit_comment(element, walker):
    walker.emit("#!")
    walker.walk(element.content)
    walker.emit("\n")


def shebang_execute():
    return _Shebang(_Command(path("/bin", "bash")))


def shebang_source():
    return _Shebang(_Command(path("/bin", "cat")))


####################################################################################################


class _SingleQuoted(object):
    def __init__(self, *element):
        object.__init__(self)
        self.content = element


@VISITOR_MAP.register(_SingleQuoted)
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


@VISITOR_MAP.register(_Variable)
def visit_variable(element, walker):
    walker.walk(element.name)


def vn(variable_name):
    return _Variable(variable_name)


####################################################################################################


class _VariableReference(object):
    def __init__(self, variable_name):
        object.__init__(self)
        self.name = variable_name


@VISITOR_MAP.register(_VariableReference)
def visit_variable_reference(element, walker):
    walker.emit("$")
    walker.walk(element.name)


def vr(variable_name):
    return _VariableReference(variable_name)


####################################################################################################
""" Disabled content
"""

#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from src_gen.common import *
from src_gen.script.element import *
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)
from .render import my_visitor_map


class Assign(object):
    def __init__(self, variable, *expression):
        super().__init__()
        self.variable = squashed(variable)
        self.expressions = squashed(expression)

    def __repr__(self):
        return "Assign({}, {})".format(self.variable, self.expressions)


class Else(object):
    def __init__(self, *statement):
        super().__init__()
        self.statements = squashed(statement)
        assert is_.not_none(self.statements)

    def __repr__(self):
        return "Else({})".format(self.statements)


class ElseIf(object):
    def __init__(self, condition, *statement):
        super().__init__()
        self.condition = squashed(condition)
        assert is_.not_none(self.condition)
        self.statements = squashed(statement)
        assert is_.not_none(self.statements)

    def __repr__(self):
        return "ElseIf({}, {})".format(self.condition, self.statements)


class Fi(object):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "Fi()"


class Function(object):
    def __init__(self, name, *statement):
        super().__init__()
        self.name = squashed(name)
        self.statements = squashed(statement)
        assert is_.not_none(self.statements)

    def __repr__(self):
        return "Function({})".format(self.statements)


class If(object):
    def __init__(self, condition, *statement):
        super().__init__()
        self.condition = squashed(condition)
        assert is_.not_none(self.condition)
        self.statements = squashed(statement)
        assert is_.not_none(self.statements)

    def __repr__(self):
        return "If({}, {})".format(self.condition, self.statements)


class Substitution(object):
    def __init__(self, command):
        super().__init__()
        assert is_.instance(command, Command)
        self.command = command

    def __repr__(self):
        return "Substitution({})".format(self.command)


class VariableName(object):
    def __init__(self, name):
        super().__init__()
        self.name = squashed(name)

    def __repr__(self):
        return "VariableName({})".format(self.name)


class VariableReference(object):
    def __init__(self, name):
        super().__init__()
        self.name = squashed(name)

    def __repr__(self):
        return "VariableReference({})".format(self.name)


@my_visitor_map.register(Assign)
def _visit_assign(element, walker):
    walker.walk(element.variable)
    walker.emit("=")
    walker.walk(element.expressions)


@my_visitor_map.register(Else)
def _visit_else(element, walker):
    walker.emit("else")
    walker.walk(eol())
    walker.walk(element.statements)


@my_visitor_map.register(ElseIf)
def _visit_elif(element, walker):
    walker.emit("elif ")
    walker.walk(element.condition)
    walker.walk(seq())
    walker.emit("then")
    walker.walk(eol())
    walker.walk(element.statements)


@my_visitor_map.register(Fi)
def _visit_fi(element, walker):
    walker.emit("fi")
    walker.walk(eol())


@my_visitor_map.register(Function)
def _visit_function(element, walker):
    walker.emit(element.name)
    walker.emit("() {")
    walker.walk(eol())
    walker.walk(element.statements)
    walker.emit("}")


@my_visitor_map.register(If)
def _visit_if(element, walker):
    walker.emit("if ")
    walker.walk(element.condition)
    walker.walk(seq())
    walker.emit("then")
    walker.walk(eol())
    walker.walk(element.statements)


@my_visitor_map.register(Substitution)
def _visit_substitution(element, walker):
    walker.emit("$(")
    walker.walk(element.command)
    walker.emit(")")


@my_visitor_map.register(VariableName)
def _visit_variable_name(element, walker):
    walker.walk(element.name)


@my_visitor_map.register(VariableReference)
def _visit_variable_reference(element, walker):
    walker.emit("${")
    walker.walk(element.name)
    walker.emit("}")


def and_():
    return " &&"


def bs():
    return ["\\", eol()]


def or_():
    return " || "


def pipe():
    return " | "


def seq():
    return " ; "


"""DisabledContent
"""

#!/usr/bin/env false
"""TODO: Write

# 4:  Default serialization visitors for standard Python types
"""
# Internal packages  (absolute references, distributed with Python)
from decimal import Decimal
from types import BuiltinMethodType
from types import FunctionType
from types import GeneratorType
from types import MethodType

# External packages  (absolute references, NOT distributed with Python)
# Library modules    (absolute references, NOT packaged, in project)
# Co-located modules (relative references, NOT packaged, in project)
from .section_3 import DEFAULT
from .section_3 import VisitorMap


# visitor signature = "f(obj_to_be_walked, walker)", return value ignored
# o = obj_to_be_walked, w = walker (aka serializer)

visitor_map = VisitorMap()


@visitor_map.register(DEFAULT)
def _visit_default(element, walker):
    walker.emit("\n")
    walker.emit("NO VISITOR FOR ")
    walker.walk(repr(element))
    walker.emit("\n")


@visitor_map.register(int)
def _visit_int(element, walker):
    walker.emit(str(element))


@visitor_map.register(list)
def _visit_list(element, walker):
    for item in element:
        walker.walk(item)


@visitor_map.register(type(None))
def _visit_none(element, walker):
    pass


@visitor_map.register(str)
def _visit_str(element, walker):
    walker.emit(element)


@visitor_map.register(tuple)
def _visit_tuple(element, walker):
    for item in element:
        walker.walk(item)


"""DisabledContent
from .section_1 import safe_bytes
from .section_1 import safe_unicode

default_visitor_map = VisitorMap({
#   str: (lambda o, w: w.walk(str(o, w.input_encoding, 'strict'))),
    str: (lambda o, w: w.emit(o)),
#   safe_bytes: (lambda o, w: w.emit(str(o, w.input_encoding, 'strict'))),
#   safe_unicode: (lambda o, w: w.emit(o)),
    type(None): (lambda o, w: None),
    bool: (lambda o, w: w.emit(str(o))),
    type: (lambda o, w: w.walk(str(o))),
    DEFAULT: (lambda o, w: w.walk(repr(o)))})

func_types = (FunctionType, BuiltinMethodType, MethodType)
number_types = (int, int, Decimal, float, complex)
sequence_types = (tuple, list, set, frozenset, range, GeneratorType)

for typeset, visitor in (
    (number_types, (lambda o, w: w.emit(str(o)))),
    (sequence_types, (lambda o, w: [w.walk(i) for i in o])),
    (func_types, (lambda o, w: w.walk(o())))):
    for type_ in typeset:
        default_visitor_map[type_] = visitor
"""

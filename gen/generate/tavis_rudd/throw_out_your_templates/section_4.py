# -*- coding: utf-8 -*-

from decimal import Decimal
from types   import BuiltinMethodType
from types   import FunctionType
from types   import GeneratorType
from types   import MethodType

from .section_1 import safe_bytes
from .section_1 import safe_unicode
from .section_3 import DEFAULT
from .section_3 import VisitorMap


################################################################################
# 4:  Default serialization visitors for standard Python types

# visitor signature = "f(obj_to_be_walked, walker)", return value ignored
# o = obj_to_be_walked, w = walker (aka serializer)
default_visitor_map = VisitorMap({
    str: (lambda o, w: w.walk(str(o, w.input_encoding, 'strict'))),
    str: (lambda o, w: w.emit(o)),
    safe_bytes: (lambda o, w: w.emit(str(o, w.input_encoding, 'strict'))),
    safe_unicode: (lambda o, w: w.emit(o)),
    type(None): (lambda o, w: None),
    bool: (lambda o, w: w.emit(str(o))),
    type: (lambda o, w: w.walk(str(o))),
    DEFAULT: (lambda o, w: w.walk(repr(o)))})

number_types = (int, int, Decimal, float, complex)
func_types = (FunctionType, BuiltinMethodType, MethodType)
sequence_types = (tuple, list, set, frozenset, range, GeneratorType)

for typeset, visitor in (
    (number_types, (lambda o, w: w.emit(str(o)))),
    (sequence_types, (lambda o, w: [w.walk(i) for i in o])),
    (func_types, (lambda o, w: w.walk(o())))):
    for type_ in typeset:
        default_visitor_map[type_] = visitor


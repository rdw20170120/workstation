# -*- coding: utf-8 -*-

import types

from decimal import Decimal
from throw_out_your_templates_1_core_wrappers import safe_bytes
from throw_out_your_templates_1_core_wrappers import safe_unicode
from throw_out_your_templates_3_core_visitor_map import DEFAULT
from throw_out_your_templates_3_core_visitor_map import VisitorMap

################################################################################
# 4:  Default serialization visitors for standard Python types

# visitor signature = "f(obj_to_be_walked, walker)", return value ignored
# o = obj_to_be_walked, w = walker (aka serializer)
default_visitors_map = VisitorMap({
    str: (lambda o,w: w.walk(unicode(o, w.input_encoding, 'strict'))),
    unicode: (lambda o, w: w.emit(o)),
    safe_bytes: (lambda o, w: w.emit(unicode(o, w.input_encoding, 'strict'))),
    safe_unicode: (lambda o, w: w.emit(o)),
    types.NoneType: (lambda o, w: None),
    bool: (lambda o, w: w.emit(str(o))),
    type: (lambda o, w: w.walk(unicode(o))),
    DEFAULT: (lambda o, w: w.walk(repr(o)))})

number_types = (int, long, Decimal, float, complex)
func_types = (types.FunctionType, types.BuiltinMethodType, types.MethodType)
sequence_types = (tuple, list, set, frozenset, xrange, types.GeneratorType)

for typeset, visitor in (
    (number_types, (lambda o, w: w.emit(str(o)))),
    (sequence_types, (lambda o, w: [w.walk(i) for i in o])),
    (func_types, (lambda o, w: w.walk(o())))):
    for type_ in typeset:
        default_visitors_map[type_] = visitor


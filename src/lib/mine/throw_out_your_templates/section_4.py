#!/usr/bin/env false
"""4:  Default serialization visitors for standard Python types"""
# Internal packages (absolute references, distributed with Python)
from decimal import Decimal
from types import BuiltinMethodType
from types import FunctionType
from types import GeneratorType
from types import MethodType

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)
from .section_3 import DEFAULT
from .section_3 import VisitorMap


# visitor signature = "f(o, w)",
# o = obj_to_be_walked, w = walker (aka serializer)
# return value ignored

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
"""

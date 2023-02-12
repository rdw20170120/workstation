#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
# Project modules   (relative references, NOT packaged, in project)
from .render import my_visitor_map


class _Import(object):
    def __init__(self, package, as_):
        super().__init__()
        self.package = squashed(package)
        assert is_.not_none(self.package)
        self.as_ = squashed(as_)

    def __repr__(self):
        return "_Import({}, {})".format(self.package, self.as_)


class _ImportFrom(object):
    def __init__(self, package, item, as_):
        super().__init__()
        self.package = squashed(package)
        assert is_.not_none(self.package)
        self.item = squashed(item)
        assert is_.not_none(self.item)
        self.as_ = squashed(as_)

    def __repr__(self):
        return "_ImportFrom({}, {}, {})".format(self.package, self.item, self.as_)


@my_visitor_map.register(_Import)
def _visit_import(element, walker):
    walker.emit("import ")
    walker.walk(element.package)
    if element.as_ is not None:
        walker.emit(" as ")
        walker.walk(element.as_)
    walker.emit("\n")


@my_visitor_map.register(_ImportFrom)
def _visit_import_from(element, walker):
    walker.emit("from ")
    walker.walk(element.package)
    walker.emit(" import ")
    walker.walk(element.item)
    if element.as_ is not None:
        walker.emit(" as ")
        walker.walk(element.as_)
    walker.emit("\n")


"""DisabledContent
"""

#!/usr/bin/env false
"""TODO: Write
"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_
# Project modules   (relative references, NOT packaged, in project)
from .render import my_visitor_map


class _TableRow(object):
    def __init__(self, *column):
        super().__init__()
        self.columns = squashed(column)

    def __repr__(self):
        return "_TableRow({})".format(self.columns)


@my_visitor_map.register(_TableRow)
def _visit_table_row(element, walker):
    if is_nonstring_iterable(element.columns):
        for c in element.columns:
            walker.emit("|")
            walker.walk(c)
    else:
        walker.emit("|")
        walker.walk(element.columns)
    walker.emit("|")
    walker.walk(eol())


"""DisabledContent
"""

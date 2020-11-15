#!/usr/bin/env false
"""3: VisitorMap"""
# Internal packages (absolute references, distributed with Python)
# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from utility import my_assert as is_

# Project modules   (relative references, NOT packaged, in project)


class VisitorMap(dict):
    """Maps Python types to visitors that know how to serialize them.

    A `VisitorMap` can be chained to a `parent_map` that it will
    fall-back to if it doesn't have a visitor registered for a
    specific type (or one of that type's base classes).
    """

    def __init__(self, map_or_seq=(), parent_map=None):
        super(VisitorMap, self).__init__(map_or_seq)
        self.parent_map = parent_map

    def get_visitor(self, obj, use_default=True):
        """Return the visitor callable registered for `type(obj)`.

        If no exact match is found, it will look for a visitor
        registered on a base-type in `type(obj).__mro__`.  If that
        fails and the VisitorMap has a `parent_map`,
        `parent_map.get_visitor(obj, use_default=False)` will be
        called.

        If all of the above fails, it returns the `DEFAULT` visitor or
        `None`.
        """
        py_type = type(obj)
        result = self.get(py_type) or self._get_parent_type_visitor(
            obj, py_type
        )
        if result:
            return result
        elif self.parent_map is not None:
            result = self.parent_map.get_visitor(obj, False)
        if not result and use_default:
            result = self.get(DEFAULT)
            if not result and self.parent_map is not None:
                result = self.parent_map.get(DEFAULT)
        return result

    def _get_parent_type_visitor(self, obj, py_type):
        for base in py_type.__mro__:
            if base in self:
                return self[base]

    def copy(self):
        return self.__class__(super(VisitorMap, self).copy())

    def as_context(self, walker, set_parent_map=True):
        """Returns a context manager for use in 'with' statements
        inside visitor functions.

        It allows you to define a set of visitor mappings that only
        apply within the current visitor's context and have all other
        mappings looked up in the exising visitor_map.  See
        `visit_xml_cdata` for an example.
        """
        return _VisitorMapContextManager(self, walker, set_parent_map)

    def register(self, py_type, visitor=None):
        """If both args are passed, this does `self[py_type] = visitor`.
        If only `py_type` is passed, it assumes you are decorating a
        visitor function definition:
          @vmap.register(some_type)
          def visit_some_type(o, w):
              ...
        """
        if visitor:
            self[py_type] = visitor
        else:

            def decorator(f):
                self[py_type] = f
                return f

            return decorator


class _VisitorMapContextManager(object):
    """The `with` statement context manager returned by
    VisitorMap.as_context()"""

    def __init__(self, vmap, walker, set_parent_map=True):
        self.vmap = vmap
        self.original_map = None
        self.walker = walker
        self.set_parent_map = set_parent_map

    def __enter__(self):
        self.original_map = self.walker.visitor_map
        if self.set_parent_map:
            assert is_.none(self.vmap.parent_map)
            self.vmap.parent_map = self.original_map
        self.walker.visitor_map = self.vmap

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.walker.visitor_map = self.original_map
        if self.set_parent_map:
            self.vmap.parent_map = None


class DEFAULT(object):
    ">>> visitor_map[DEFAULT] = visitor # sets default fallback visitor"


"""DisabledContent
"""

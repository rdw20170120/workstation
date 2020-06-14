#!/usr/bin/env false
"""
"""
from .section_1 import default_encoding
from .section_4 import visitor_map as default_visitor_map

################################################################################
# 2: Serializer


class Serializer(object):
    """A tree walker that serializes what it walks into Unicode.

    Uses the Visitor design pattern to manage the walk.
    """
    def __init__(self, visitor_map=None):
        if visitor_map is None:
            visitor_map = default_visitor_map.copy()
        self.visitor_map = visitor_map
        self._buffer = []

    def serialize(self, obj):
        """Serialize an object, and its children, into Unicode."""
        self._buffer = []
        self.walk(obj)
        return ''.join(self._buffer)

    def walk(self, obj):
        """This method is called by visitors for anything they
        encounter which they don't explicitly handle.
        """
        visitor = self.visitor_map.get_visitor(obj)
        if visitor:
#           print("Visitor '{}' is walking object '{}'".format(visitor, obj))
            visitor(obj, self) # ignore return value
        else:
            raise TypeError('No visitor found for {}'.format(repr(obj)))

    def emit(self, escaped_unicode_output):
        """This is called by visitors when they have direct output."""
#       print("Emitting: {}".format(escaped_unicode_output))
        self._buffer.append(escaped_unicode_output)

'''DisabledContent
'''


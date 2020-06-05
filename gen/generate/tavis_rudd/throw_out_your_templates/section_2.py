# -*- coding: utf-8 -*-

from .section_1 import default_encoding
# from .section_1 import safe_unicode
from .section_4 import default_visitor_map

################################################################################
# 2: Serializer


class Serializer(object):
    """A tree walker that uses the visitor pattern to serialize what
    it walks into properly escaped unicode.
    """
    def __init__(self, visitor_map=None, input_encoding=None):
        if visitor_map is None:
            visitor_map = default_visitor_map.copy()
        self.visitor_map = visitor_map
        self.input_encoding = (input_encoding or default_encoding)
        self._safe_buffer = []

    def serialize(self, obj):
        """Serialize an object, and its children, into sanitized unicode."""
        self._safe_buffer = []
        self.walk(obj)
        return ''.join(self._safe_buffer)

    def walk(self, obj):
        """This method is called by visitors for anything they
        encounter which they don't explicitly handle.
        """
        visitor = self.visitor_map.get_visitor(obj)
        if visitor:
            print("Visitor '{}' is walking object '{}'".format(visitor, obj))
            visitor(obj, self) # ignore return value
        else:
            raise TypeError('No visitor found for %s'%repr(obj))

    def emit(self, escaped_unicode_output):
        """This is called by visitors when they have escaped unicode
        to output.
        """
        print("Emitting: {}".format(escaped_unicode_output))
        self._safe_buffer.append(escaped_unicode_output)

    def emit_many(self, output_seq):
        self._safe_buffer.extend(output_seq)

''' Disabled content
'''


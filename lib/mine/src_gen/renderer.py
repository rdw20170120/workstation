#!/usr/bin/env false
"""
"""
from logzero import logger as log

from throw_out_your_templates.section_1 import default_encoding
from throw_out_your_templates.section_2 import Serializer
from throw_out_your_templates.section_4 import visitor_map as default_visitor_map


class Renderer(object):
    def __init__(
        self, visitor_map=default_visitor_map, encoding=default_encoding
        ):
        object.__init__(self)
        self._encoding = encoding
        self._visitor_map = visitor_map

    def _get_serializer(self):
        return Serializer(self._visitor_map)

    def _serialize(self, content):
        return self._get_serializer().serialize(content)

    def render(self, content, file_path=None):
        if file_path is None:
            log.info("Printing rendered content to stdout")
            print(self._serialize(content))
        else:
            log.info("Writing rendered content to file '%s'", file_path)
            with open(file_path, mode='wt',
                newline=None
                ) as f:
                f.write(self._serialize(content))

'''DisabledContent
'''


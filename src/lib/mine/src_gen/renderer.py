#!/usr/bin/env false
"""TODO: Write

TODO: REVIEW: how best to integrate logging into a library
"""
# Internal packages (absolute references, distributed with Python)
from logging import getLogger

# External packages (absolute references, NOT distributed with Python)
# Library modules   (absolute references, NOT packaged, in project)
from throw_out_your_templates.section_1 import default_encoding
from throw_out_your_templates.section_2 import Serializer
from throw_out_your_templates.section_4 import (
    visitor_map as default_visitor_map,
)
from utility.my_logging import log_exception

# Project modules   (relative references, NOT packaged, in project)


class Renderer(object):
    def __init__(self, visitor_map=default_visitor_map, encoding=default_encoding):
        self._encoding = encoding
        self._log = getLogger(self.__class__.__name__)
        self._visitor_map = visitor_map
        super().__init__()

    def _get_serializer(self):
        return Serializer(self._visitor_map)

    def _serialize(self, content):
        return self._get_serializer().serialize(content)

    def render(self, content, file_path=None):
        try:
            if file_path is None:
                self._log.info("Printing rendered content to stdout")
                print((self._serialize(content)))
            else:
                self._log.info("Writing rendered content to file '%s'", file_path)
                with open(file_path, mode="wt", newline=None) as f:
                    f.write(self._serialize(content))
        except TypeError as e:
            log_exception(self._log, e)
            raise
        except Exception as e:
            log_exception(self._log, e)
            raise


"""DisabledContent
"""

from logzero import logger as log

from ..tavis_rudd.throw_out_your_templates.section_1 import default_encoding
from ..tavis_rudd.throw_out_your_templates.section_2 import Serializer
from ..tavis_rudd.throw_out_your_templates.section_4 import default_visitor_map


class Renderer(object):
    def __init__(
        self, visitor_map=default_visitor_map, encoding=default_encoding
        ):
        object.__init__(self)
        self._encoding = encoding
        # TODO: RESEARCH: Does this address newline problem?
        self._visitor_map = visitor_map

    def _get_serializer(self):
        return Serializer(
            self._visitor_map
            # TODO: , self._encoding
            )

    def _serialize(self, content):
        return self._get_serializer().serialize(content)

    def render(self, content, file_path=None):
        if file_path is None:
            log.info("Printing rendered content to stdout")
            print(
                self._serialize(content) # TODO: .encode(self._encoding)
                )
        else:
            log.info("Writing rendered content to file '%s'", file_path)
            with open(file_path, mode='wt',
                # TODO: encoding=self._encoding,
                newline=None
                ) as f:
                f.write(
                    self._serialize(content) # TODO: .encode(self._encoding)
                    )


''' Disabled content
from ..tavis_rudd.throw_out_your_templates.section_2 import Serializer
from ..tavis_rudd.throw_out_your_templates.section_4 import default_visitor_map


class Renderer(object):
    def __init__(self, visitor_map=default_visitor_map):
        super().__init__()
        self._visitor_map = visitor_map

    def _get_serializer(self):
        return Serializer(self._visitor_map)

    def _serialize(self, string):
        return self._get_serializer().serialize(string)

    def render(self, content, filepath=None):
        if filepath is None:
            print(self._serialize(content))
        else:
            with open(filepath, mode='wt', encoding='utf-8') as f:
                f.write(self._serialize(content))
'''


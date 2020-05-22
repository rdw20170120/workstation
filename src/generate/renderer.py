from tavis_rudd.throw_out_your_templates.section_1 import get_default_encoding
from tavis_rudd.throw_out_your_templates.section_2 import Serializer
from tavis_rudd.throw_out_your_templates.section_4 import default_visitors_map


class Renderer(object):
    def __init__(self, visitor_map=default_visitors_map, encoding=get_default_encoding()):
        super().__init__()
        self._encoding = encoding
        self._visitor_map = visitor_map

    def _get_output(self, content):
        return self._get_serializer().serialize(content)

    def _get_serializer(self):
        return Serializer(self._visitor_map, self._encoding)

    def _print_output(self, output):
        print((output.encode(self._encoding)))

    def render(self, content, filepath=None):
        # TODO: Does this attempt to encode twice?
        if filepath is None:
            self._print_output(self._get_output(content))
        else:
            with open(filepath, 'w') as f:
                f.write(self._get_output(content).encode(self._encoding))


""" Disabled content
"""


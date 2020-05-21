from throw_out_your_templates_1_core_wrappers import get_default_encoding
from throw_out_your_templates_2_core_serializer import Serializer
from throw_out_your_templates_4_core_default_visitors import default_visitors_map


class Renderer(object):
    def __init__(self, visitor_map=default_visitors_map, encoding=get_default_encoding()):
        object.__init__(self)
        self._encoding = encoding
        self._visitor_map = visitor_map

    def _get_output(self, content):
        return self._get_serializer().serialize(content)

    def _get_serializer(self):
        return Serializer(self._visitor_map, self._encoding)

    def _print_output(self, output):
        print((output.encode(self._encoding)))

    def render(self, content, file_name=None):
        if file_name is None:
            self._print_output(self._get_output(content))
        else:
            with open(file_name, 'w') as f:
                f.write(self._get_output(content).encode(self._encoding))


""" Disabled content
"""


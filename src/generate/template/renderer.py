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
            with open(filepath, 'w') as f:
                f.write(self._serialize(content))


''' Disabled content
'''


from pathlib import Path

from ..tavis_rudd.throw_out_your_templates.section_3 import VisitorMap
from ..tavis_rudd.throw_out_your_templates.section_4 import default_visitor_map

from ..utility.my_system import maybe_create_directory
from .renderer           import Renderer


visitor_map = VisitorMap(parent_map=default_visitor_map)


class Content(object):
    def __init__(self, content, relative_directory, filename):
        super().__init__()
        assert isinstance(content, list)
        assert isinstance(filename, str)
        assert isinstance(relative_directory, Path)
        assert not relative_directory.is_absolute()
        self._content = content
        self._filename = filename
        self._relative_directory = relative_directory

    def add(self, content):
        self._content.append(content)
        return self

    def generate(self, target_directory):
        assert isinstance(target_directory, Path)
        directory = target_directory / self._relative_directory
        maybe_create_directory(directory)
        Renderer(visitor_map).render(self._content, directory / self._filename)

    def print(self):
        Renderer(visitor_map).render(self._content)


@visitor_map.register(Content)
def _visit_content(content, walker):
    walker.walk(content._content)


''' Disabled content
'''


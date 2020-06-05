from ..tavis_rudd.throw_out_your_templates.section_3 import VisitorMap

from .script           import Script
from .script           import visitor_map as parent_visitor_map
from .script_structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)


class PythonSource(Script):
    def __init__(self, content, relative_directory, filename):
        super().__init__(content, relative_directory, filename)


''' Disabled content
'''


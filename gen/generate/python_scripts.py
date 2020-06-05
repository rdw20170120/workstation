from .tavis_rudd.throw_out_your_templates.section_3 import VisitorMap

from .template.python_source    import PythonSource
from .template.python_source    import visitor_map as parent_visitor_map
from .template.python_structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _generate(target_directory, subdirectories, file_name):
    content = PythonSource(
        visitor_map,
        subdirectories, file_name,
        build()
        )
    content.generate(target_directory)

def build():
    return [
        python_script_header(),
    ]

def generate(target_directory):
    sub = Path('BriteOnyx/bin')
    _generate(target_directory, sub, 'avro-print')
    _generate(target_directory, sub, 'extensions')
    _generate(target_directory, sub, 'list')


''' Disabled content
'''


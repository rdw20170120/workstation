from pathlib import Path

from throw_out_your_templates.section_3 import VisitorMap

from src_gen.script.python.source    import PythonSource
from src_gen.script.python.source    import visitor_map as parent_visitor_map
from src_gen.script.python.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _generate(content, target_directory, subdirectories, file_name):
    source = PythonSource(
        visitor_map,
        subdirectories, file_name,
        content
        )
    source.generate(target_directory)

def _to_be_executed():
    return [
        python_script_header(),
        disabled_content_footer(),
    ]

def generate(target_directory):
    sub = Path('BriteOnyx/bin')
    _generate(_to_be_executed(), target_directory, sub, 'avro-print')
    _generate(_to_be_executed(), target_directory, sub, 'extensions')
    _generate(_to_be_executed(), target_directory, sub, 'list')


''' Disabled content
    sub = Path('')
    _generate(_to_be_executed(), target_directory, sub, '')
'''


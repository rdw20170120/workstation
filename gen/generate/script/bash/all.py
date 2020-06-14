from throw_out_your_templates.section_3 import VisitorMap

from src_gen.script.bash.source    import BashScript
from src_gen.script.bash.source    import visitor_map as parent_visitor_map
from src_gen.script.bash.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _generate(target_directory, subdirectories, file_name):
    content = BashScript(
        visitor_map,
        subdirectories, file_name,
        build()
        )
    content.generate(target_directory)

def build():
    return [
        bash_script_header(),
    ]

def generate(target_directory):
    sub = Path('BriteOnyx/bin')


''' Disabled content
'''


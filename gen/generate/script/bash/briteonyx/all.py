from throw_out_your_templates.section_3 import VisitorMap

from src_gen.script.bash.briteonyx.source    import BriteOnyxScript
from src_gen.script.bash.briteonyx.source    import visitor_map as parent_visitor_map
from src_gen.script.bash.briteonyx.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _generate(target_directory, subdirectories, file_name):
    content = BriteOnyxScript(
        visitor_map,
        subdirectories, file_name,
        build()
        )
    content.generate(target_directory)

def build():
    return [
    ]

def generate(target_directory):
    sub = Path('BriteOnyx/bin')


''' Disabled content
'''


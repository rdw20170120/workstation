from throw_out_your_templates.section_3 import VisitorMap

from src_gen.document.markdown.source    import Markdown
from src_gen.document.markdown.source    import visitor_map as parent_visitor_map
from src_gen.document.markdown.structure import *


visitor_map = VisitorMap(parent_map=parent_visitor_map)

def _generate(target_directory, subdirectories, file_name):
    content = Markdown(
        visitor_map,
        subdirectories, file_name,
        build()
        )
    content.generate(target_directory)

def build():
    return [
    ]

def generate(target_directory):
    pass


''' Disabled content
'''


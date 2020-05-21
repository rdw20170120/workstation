# -*- coding: utf-8 -*-

from throw_out_your_templates_1_core_wrappers import safe_unicode
from throw_out_your_templates_4_core_default_visitors import default_visitors_map
from throw_out_your_templates_5_frosting_dom_classes import Comment
from throw_out_your_templates_7_example_helpers import body
from throw_out_your_templates_7_example_helpers import div
from throw_out_your_templates_7_example_helpers import Example
from throw_out_your_templates_7_example_helpers import examples_vmap
from throw_out_your_templates_7_example_helpers import head
from throw_out_your_templates_7_example_helpers import html
from throw_out_your_templates_7_example_helpers import htmltags
from throw_out_your_templates_7_example_helpers import meta
from throw_out_your_templates_7_example_helpers import script
from throw_out_your_templates_7_example_helpers import span
from throw_out_your_templates_7_example_helpers import title

################################################################################
# 8: Basic examples

Example(
    'Standard python types, no html',
    [1, 2, 3
     , 4.0
     , 'a', 'b'
     , ('c', ('d', 'e')
        , {'f', 'f'}) # nested
     , (i*2 for i in range(10))
     ])
# output = '1234.0abcdef024681012141618'

Example(
    'Standard python types, no html *or* html escaping',
    [1, '<', 2, '<', 3],
    visitor_map=default_visitors_map)
# output = '1<2<3'

# To see output from the rest of the examples exec this module
Example(
    'Full html5 doc, no wrapper',
    [safe_unicode('<!DOCTYPE html>'),
     html(lang='en')[
         head[title['An example'], meta(charset='UTF-8')],
         body['Some content']
         ]
     ])

class HTML5Doc(object):
    def __init__(self, body, head=None):
        self.body = body
        self.head = (
            head if head
            else htmltags.head[title['An example'],
                               meta(charset='UTF-8')])

@examples_vmap.register(HTML5Doc)
def visit_html5_doc(doc, walker):
    walker.walk([safe_unicode('<!DOCTYPE html>'),
                 html(lang='en')[
                     doc.head,
                     doc.body]])

Example(
    'Full html5 doc, with wrapper',
    HTML5Doc(body('a_css_class')[div['content']]))

Example(
    'Full html5 doc, with wrapper and overriden head',
    HTML5Doc(body('wrapped')[div['content']],
             head=title['Overriden']))

Example(
    """Context-aware HTML escaping
    (does any template lang other than Genshi do this?)""",
    HTML5Doc(
        body(onload='func_with_esc_args(1, "bar")')[
            div['Escaped chars: ', '< ', '>', '&'],
            script(type='text/javascript')[
                 'var lt_not_escaped = (1 < 2);',
                 '\nvar escaped_cdata_close = "]]>";',
                 '\nvar unescaped_ampersand = "&";'
                ],
            Comment('''
            not escaped "< & >"
            escaped: "-->"
            '''),
            div['some encoded bytes and the equivalent unicode:',
                '你好', str('你好', 'utf-8')],
            safe_unicode('<b>My surrounding b tags are not escaped</b>'),
            ]))

Example(
    'a snippet using a list comprehension',
    div[[span(id=('id', i))[i, ' is > ', i-1]
         for i in range(5)]])


# -*- coding: utf-8 -*-

from throw_out_your_templates_1_core_wrappers import get_default_encoding
from throw_out_your_templates_2_core_serializer import Serializer
from throw_out_your_templates_5_frosting_dom_classes import htmltags
from throw_out_your_templates_5_frosting_dom_classes import XmlElement
from throw_out_your_templates_6_frosting_dom_visitors import visit_xml_element
from throw_out_your_templates_6_frosting_dom_visitors import xml_default_visitors_map

################################################################################
# 7: Helpers for examples:

examples_vmap = xml_default_visitors_map.copy()

@examples_vmap.register(XmlElement)
def pprint_visit_xml_element(elem, walker):
    visit_xml_element(elem, walker)
    walker.emit('\n') # easier to read example output

class Example(object):
    all_examples = [] #class attr
    def __init__(self, name, content,
                 visitor_map=examples_vmap,
                 input_encoding='utf-8'):
        self.name = name
        self.content = content
        self.visitor_map = visitor_map
        self.input_encoding = input_encoding
        Example.all_examples.append(self)

    def show(self):
        print '-'*80
        print '## Output from example:', self.name
        print
        output = Serializer(
            self.visitor_map,
            self.input_encoding).serialize(self.content)
        print output.encode(get_default_encoding())


## put some html tags in the module scope to make the examples less
## verbose:
class _GetAttrDict(dict):
    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(k)
htmltags = _GetAttrDict(htmltags)
meta   = htmltags.meta
html   = htmltags.html
head   = htmltags.head
script = htmltags.script
title  = htmltags.title
body   = htmltags.body
div    = htmltags.div
span   = htmltags.span
h1     = htmltags.h1
h2     = htmltags.h2
ul     = htmltags.ul
li     = htmltags.li
## could also say:
#for k, v in htmltags.iteritems():
#    exec '%s = htmltags["%s"]'%(k, k)
## but then my pyflakes/flymake setup complains about undefined vars ...


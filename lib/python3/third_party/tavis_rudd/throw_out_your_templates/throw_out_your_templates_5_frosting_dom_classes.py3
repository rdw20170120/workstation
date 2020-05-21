# -*- coding: utf-8 -*-

from throw_out_your_templates_1_core_wrappers import safe_unicode

################################################################################
# 5: Declarative classes for creating a dom-like tree of xml/html elements:

# If you don't like this particular tag building syntax, please
# remember my main argument and use your imagination to dream up
# a better syntax.  The code above (sections 1-4) is what counts.
# Everything that follows can be swapped out.

class XmlName(safe_unicode):
    """An XML element or attribute name"""

class XmlAttributes(list): pass
class XmlAttribute(object):
    def __init__(self, value, name=None):
        self.value = value
        self.name = name

class XmlElement(object):
    attrs = None
    children = None

    def __init__(self, name):
        self.name = name

    def __call__(self, class_=None, **attrs):
        assert not self.attrs
        if class_ is not None:
            attrs['class'] = class_
        self.attrs = self._normalize_attrs(attrs)
        return self

    def _normalize_attrs(self, attrs):
        out = XmlAttributes()
        for n, v in list(attrs.items()):
            if n.endswith('_'):
                n = n[:-1]
            if '_' in n:
                if '__' in n:
                    n = n.replace('__', ':')
                elif 'http_' in n:
                    n = n.replace('http_', 'http-')
            # may eventually run into encoding issues with name:
            out.append(XmlAttribute(value=v, name=XmlName(n)))
        return out

    def _add_children(self, children):
        assert not self.children
        self.children = []
        if isinstance(children, (tuple, list)):
            self.children.extend(children)
        else:
            self.children.append(children)

    def __getitem__(self, children):
        self._add_children(children)
        return self

class XmlElementProto(object):
    def __init__(self, name, can_be_empty=False, element_class=XmlElement):
        self.name = XmlName(name)
        self.can_be_empty = can_be_empty
        self.element_class = element_class

    def __call__(self, class_=None, **attrs):
        if class_ is not None:
            attrs['class'] = class_
        return self.element_class(self.name)(**attrs)

    def __getitem__(self, children):
        return self.element_class(self.name)[children]

class XmlEntityRef(object):
    def __init__(self, alpha, num, description):
        self.alpha, self.num, self.description = (alpha, num, description)

class XmlCData(object):
    def __init__(self, content):
        self.content = content

class Comment(object):
    def __init__(self, content):
        self.content = content

class Script(XmlElement):
    pass

# This list of html tags isn't exhaustive.  It's just an example.
# The definitive list of tags and whether they can be empty is html
# version specific.  If you care about that, you could create a
# separate list for each html version.
_non_empty_html_tags = '''
  a abbr acronym address applet b bdo big blockquote body button
  caption center cite code colgroup dd dfn div dl dt em fieldset font
  form frameset h1 h2 h3 h4 h5 h6 head html i iframe ins kbd label
  legend li menu noframes noscript ol optgroup option pre q s samp
  select small span strike strong style sub sup table tbody td
  textarea tfoot th thead title tr tt u ul var'''.split()

_maybe_empty_html_tags = '''
    area base br col frame hr img input link meta p param script'''.split()

htmltags = dict(
    [(n, XmlElementProto(n, False)) for n in _non_empty_html_tags]
    + [(n, XmlElementProto(n, True)) for n in _maybe_empty_html_tags]
    + [('script', XmlElementProto('script', element_class=Script))])

# I have a separate module that defines the html entity refs.  Email
# me if you would like a copy.


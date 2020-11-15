# -*- coding: utf-8 -*-

from cgi import escape as xml_escape

from .section_3 import VisitorMap
from .section_4 import default_visitors_map
from .section_5 import Comment
from .section_5 import Script
from .section_5 import XmlAttribute
from .section_5 import XmlAttributes
from .section_5 import XmlCData
from .section_5 import XmlElement
from .section_5 import XmlElementProto
from .section_5 import XmlEntityRef
from .section_5 import XmlName

################################################################################
# 6: Visitors for the xml/html elements, etc.

xml_default_visitors_map = default_visitors_map.copy()

# o = obj_to_be_walked, w = walker (aka serializer)
xml_default_visitors_map.update(
    {
        str: (lambda o, w: w.emit(xml_escape(o))),
        XmlName: (lambda o, w: w.emit(str(o))),
        XmlAttributes: (lambda o, w: [w.walk(i) for i in o]),
        XmlElementProto: (
            lambda o, w: (
                w.emit(
                    safe_unicode("<%s />" % o.name)
                    if o.can_be_empty
                    else safe_unicode("<%s></%s>" % (o.name, o.name))
                )
            )
        ),
        XmlEntityRef: (lambda o, w: w.emit(safe_unicode("&%s;" % o.alpha))),
    }
)


@xml_default_visitors_map.register(XmlElement)
def visit_xml_element(elem, walker):
    walker.emit_many(("<", elem.name))
    walker.walk(elem.attrs)
    walker.emit(">")
    walker.walk(elem.children)
    walker.emit("</%s>" % elem.name)


def _substring_replace_ctx(walker, s, r, ofilter=lambda x: x):
    return VisitorMap(
        {str: lambda o, w: w.emit(ofilter(o.replace(s, r, -1)))}
    ).as_context(walker)


@xml_default_visitors_map.register(XmlAttribute)
def visit_xml_attribute(attr, walker):
    walker.emit_many((" ", attr.name, '="'))  # attr.name isinstance of XmlName
    with _substring_replace_ctx(walker, '"', r"\"", xml_escape):
        walker.walk(attr.value)
    walker.emit('"')


@xml_default_visitors_map.register(Comment)
def visit_xml_comment(obj, walker):
    walker.emit("<!--")
    with _substring_replace_ctx(walker, "--", "-/-"):
        walker.walk(obj.content)
    walker.emit("-->")


@xml_default_visitors_map.register(XmlCData)
def visit_xml_cdata(obj, walker):
    walker.emit("<![CDATA[")
    with _substring_replace_ctx(walker, "]]>", "]-]->"):
        walker.walk(obj.content)
    walker.emit("]]>")


@xml_default_visitors_map.register(Script)
def visit_script_tag(elem, walker):
    walker.emit_many(("<", elem.name))
    walker.walk(elem.attrs)
    walker.emit(">")
    if elem.children:
        walker.emit("\n//")
        walker.walk(XmlCData(("\n", elem.children, "\n//")))
        walker.emit("\n")
    walker.emit("</%s>" % elem.name)

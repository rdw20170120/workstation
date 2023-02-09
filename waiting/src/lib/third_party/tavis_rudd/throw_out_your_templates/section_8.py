# -*- coding: utf-8 -*-

from .section_1 import safe_unicode
from .section_4 import default_visitors_map
from .section_5 import Comment
from .section_7 import Example
from .section_7 import body
from .section_7 import div
from .section_7 import examples_vmap
from .section_7 import head
from .section_7 import html
from .section_7 import htmltags
from .section_7 import meta
from .section_7 import script
from .section_7 import span
from .section_7 import title

################################################################################
# 8: Basic examples

Example(
    "Standard python types, no html",
    [
        1,
        2,
        3,
        4.0,
        "a",
        "b",
        ("c", ("d", "e"), {"f", "f"}),  # nested
        (i * 2 for i in range(10)),
    ],
)
# output = '1234.0abcdef024681012141618'

Example(
    "Standard python types, no html *or* html escaping",
    [1, "<", 2, "<", 3],
    visitor_map=default_visitors_map,
)
# output = '1<2<3'

# To see output from the rest of the examples exec this module
Example(
    "Full html5 doc, no wrapper",
    [
        safe_unicode("<!DOCTYPE html>"),
        html(lang="en")[
            head[title["An example"], meta(charset="UTF-8")],
            body["Some content"],
        ],
    ],
)


class HTML5Doc(object):
    def __init__(self, body, head=None):
        self.body = body
        self.head = (
            head if head else htmltags.head[title["An example"], meta(charset="UTF-8")]
        )


@examples_vmap.register(HTML5Doc)
def visit_html5_doc(doc, walker):
    walker.walk([safe_unicode("<!DOCTYPE html>"), html(lang="en")[doc.head, doc.body]])


Example(
    "Full html5 doc, with wrapper",
    HTML5Doc(body("a_css_class")[div["content"]]),
)

Example(
    "Full html5 doc, with wrapper and overriden head",
    HTML5Doc(body("wrapped")[div["content"]], head=title["Overriden"]),
)

Example(
    """Context-aware HTML escaping
    (does any template lang other than Genshi do this?)""",
    HTML5Doc(
        body(onload='func_with_esc_args(1, "bar")')[
            div["Escaped chars: ", "< ", ">", "&"],
            script(type="text/javascript")[
                "var lt_not_escaped = (1 < 2);",
                '\nvar escaped_cdata_close = "]]>";',
                '\nvar unescaped_ampersand = "&";',
            ],
            Comment(
                """
            not escaped "< & >"
            escaped: "-->"
            """
            ),
            div[
                "some encoded bytes and the equivalent unicode:",
                "你好",
                str("你好", "utf-8"),
            ],
            safe_unicode("<b>My surrounding b tags are not escaped</b>"),
        ]
    ),
)

Example(
    "a snippet using a list comprehension",
    div[[span(id=("id", i))[i, " is > ", i - 1] for i in range(5)]],
)

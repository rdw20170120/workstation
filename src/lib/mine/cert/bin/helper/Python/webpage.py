import os
import sys
import throw_out_your_templates

from my_instruction import get_output
from my_instruction import htmltags
from my_instruction import print_output


class Html5(object):
    DIRECTORY = os.environ["TMPDIR"]

    def __init__(self, css_class, title):
        super(Html5, self).__init__()
        self._body = []
        self._css_class = css_class
        self._title_text = title
        self.add(self._title_header())

    def _as_document(self):
        return throw_out_your_templates.HTML5Doc(
            htmltags.body[
                self._body,
            ],
            head=self._head(),
        )

    def _get_default_encoding(self):
        return throw_out_your_templates.get_default_encoding()

    def _head(self):
        return htmltags.head[self._meta(), self._style(), self._title()]

    def _meta(self):
        return htmltags.meta(charset=self._get_default_encoding())

    def _style(self):
        return htmltags.style()[
            "body {font-family: serif; font-size: 100%;}\n",
            "h1 {color: red;}\n",
            "h2 {color: red;}\n",
            "p {color: black; font-size: 1.00em;}\n",
            "span {color: red;}\n",
            "h1.task {color: green; font-family: sans-serif; font-size: 2.00em;}\n",
            "h1.support {color: green; font-family: sans-serif; font-size: 2.00em;}\n",
            "h2.step {color: orange; font-family: sans-serif; font-size: 1.50em;}\n",
            "h3.support {color: orange; font-family: sans-serif; font-size: 1.50em;}\n",
            "span.literal {color: blue; font-family: monospace; font-weight: bold; font-size: 1.25em;}\n",
            "span.emphasis {color: purple; font-style: italic;}\n",
        ]

    def _title(self):
        return htmltags.title(self._css_class)[self._title_text]

    def _title_header(self):
        return htmltags.h1(self._css_class)[self._title_text]

    def add(self, content):
        self._body.append(content)
        return self

    def render(self, relative_file_path=None):
        if relative_file_path is None:
            print_output(get_output(self._as_document()))
        else:
            filename = os.path.join(self.DIRECTORY, relative_file_path)
            with open(filename, "w") as f:
                f.write(
                    get_output(self._as_document()).encode(
                        self._get_default_encoding()
                    )
                )


""" Disabled content
"""

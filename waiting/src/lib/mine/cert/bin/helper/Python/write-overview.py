#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    css_class = "support"
    page = Html5(css_class, "Exam overview")
    page.add(
        htmltags.p[
            "TODO:  Describe the exam and its environment, with links to all the other pages.",
        ]
    )
    page.add(htmltags.h3(css_class)["Essential content"])
    page.add(
        htmltags.p[
            """These pages provide essential content that you will need.  They will help you to
understand the exam and the machines that constitute the exam environment.  You """,
            emphasis("SHOULD"),
            " read these pages ",
            emphasis("BEFORE"),
            " you begin the exam tasks.",
        ]
    )
    page.add(
        htmltags.ul(css_class)[
            htmltags.li[link(css_class, PAGE_MACHINE, "machine naming conventions")],
            htmltags.li[
                link(css_class, PAGE_SSH, "HowTo:  access other exam machines")
            ],
            htmltags.li[
                link(css_class, PAGE_SUDO, "HowTo:  gain superuser privileges")
            ],
            htmltags.li[
                link(
                    css_class,
                    PAGE_DOC_4_6,
                    "Documentation for Couchbase Server 4.6",
                )
            ],
        ]
    )
    page.add(htmltags.h3(css_class)["Main tasks"])
    page.add(
        htmltags.p[
            link(css_class, "./main/index.html", "Main tasks"),
            " for you to perform as part of your exam.  You ",
            emphasis("MUST"),
            """ complete these tasks.  You will be scored based on your success at completing each of
these tasks.""",
        ]
    )
    page.add(htmltags.h3(css_class)["Initial tasks"])
    page.add(
        htmltags.p[
            link(css_class, "./init/index.html", "Initial tasks"),
            " already performed to setup the exam environment.  You do ",
            emphasis("NOT"),
            """ complete these tasks.  These tasks were performed automatically before you arrived to
take this exam.""",
        ]
    )
    page.add(htmltags.h3(css_class)["Supporting content"])
    page.add(
        htmltags.ul[
            htmltags.li[
                link(
                    css_class,
                    PAGE_UI,
                    "HowTo:  understand the exam user interface (UI)",
                )
            ],
            htmltags.li[
                link(
                    css_class,
                    PAGE_SESSION,
                    "HowTo:  begin/end your exam session",
                )
            ],
            htmltags.li[link(css_class, PAGE_FOCUS, "HowTo:  manage keyboard focus")],
            htmltags.li[link(css_class, PAGE_CUT_AND_PASTE, "HowTo:  cut and paste")],
            htmltags.li[link(css_class, PAGE_Bash, "HowTo:  leverage Bash")],
            htmltags.li[link(css_class, PAGE_UNDO, "Why:  do and then undo tasks")],
        ]
    )
    page.render(PAGE_OVERVIEW)


if __name__ == "__main__":
    sys.exit(main())


""" Disabled content
"""

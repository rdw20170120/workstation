#!/usr/bin/env python

import sys

from my_configuration import *
from my_instruction import *
from webpage import Html5


def main():
    host_client = get_host_client()
    try:
        hosts_server = get_hosts_server()
    except:
        hosts_server = None

    css_class = 'support'
    page = Html5(css_class, 'Machine naming conventions')
    if hosts_server is None:
        page.add(htmltags.p[
            'The machines of the exam environment are named according to ',
            link(css_class, PAGE_EXAMPLE_COM, 'Internet standards'),
            ' for such systems.  Specifically, the client machine is named ',
            literal(host_client),
            """.  This is the machine's Fully-Qualified Domain Names (FQDNs).  It can also be
referenced locally by its simple name prefix.""",
        ],)
    else:
        page.add(htmltags.p[
            'The machines of the exam environment are named according to ',
            link(css_class, PAGE_EXAMPLE_COM, 'Internet standards'),
            ' for such systems.  Specifically, the client machine is named ',
            literal(host_client),
            ' and the servers are named ',
            literal_list(hosts_server),
            """.  These are the machines' Fully-Qualified Domain Names (FQDNs).  They can also be
referenced locally by their simple name prefixes.""",
        ],)
    page.add(htmltags.p[
        'You can ',
        link(css_class, PAGE_SSH, 'use SSH'),
        ' to access the servers within your exam environment.',
    ],)
    page.add(htmltags.p[
        '''When adding the servers as nodes in a Couchbase cluster, please remember that they must
be referenced using their Fully-Qualified Domain Names (FQDNs) within the Couchbase software.''',
    ],)
    page.render(PAGE_MACHINE)


if __name__ == '__main__':
    sys.exit(main())

""" Disabled content
"""


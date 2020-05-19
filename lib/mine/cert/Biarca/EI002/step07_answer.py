#!/usr/bin/env python

"""
step07_answer.py will do the following task:

1. Configures superuser credentials.
"""

import os
import requests
import sys
from certtools import args_parse, debug
from certtools.couchbase.utils import common


class Q():
    args = args_parse(args=sys.argv)
    server_host = args.seg1
    port = os.environ['CB_Cluster_PortWebUi']
    cluster_user = os.environ['CB_Cluster_UserSuper']
    cluster_pass = os.environ['CB_Cluster_PassSuper']


def configure(extra_path, data):
    """Configuring couchbase server node.
    """
    url = 'http://{0}:{1}/{2}'.format(Q.server_host, Q.port, extra_path)
    common.make_request(requests.post, url, data=data)


def main():
    common.check_host(Q.server_host)
    debug('{0} - Couchbase installation : OK'.format(Q.server_host))

    # Cofiguring super user credentials
    data = {'username': Q.cluster_user,
            'password': Q.cluster_pass,
            'port': 'SAME'}
    configure('settings/web', data)
    debug('{0} - Super credentials are cofigured'.format(Q.server_host))


if __name__ == '__main__':
    sys.exit(main())

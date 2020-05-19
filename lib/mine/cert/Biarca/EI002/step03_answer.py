#!/usr/bin/env python

"""
step03_answer.py will do the following task:

1.Configures separate data and index directories.
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
    data_path = os.environ['CB_Cluster_DirData']
    index_path = os.environ['CB_Cluster_DirIndex']


def configure(extra_path, data):
    """Configuring couchbase server node.
    """
    url = 'http://{0}:{1}/{2}'.format(Q.server_host, Q.port, extra_path)
    common.make_request(requests.post, url, data=data)


def main():
    common.check_host(Q.server_host)
    debug('{0} - Couchbase installation : OK'.format(Q.server_host))

    # Configuring data and index directories
    data = {'data_path': Q.data_path,
            'index_path': Q.index_path}
    configure('nodes/self/controller/settings', data)
    debug('{0} - Data and index directories are configured'
          .format(Q.server_host))


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python

"""
step03_grading.py will do the following tasks:

1. Verifying data directory configuration
2. Verifying index directory configuration
"""

import os
import sys
from certtools import args_parse
from certtools.couchbase.utils import common, checks


class Q():
    args = args_parse(args=sys.argv)
    server_host = args.seg1
    data_path = os.environ['CB_Cluster_DirData']
    index_path = os.environ['CB_Cluster_DirIndex']
    port = os.environ['CB_Cluster_PortWebUi']
    cluster_user = os.environ['CB_Cluster_UserSuper']
    cluster_pass = os.environ['CB_Cluster_PassSuper']


def main():
    # Checking for installation of couchbase server
    score = 0
    msg = "{0}:{1} - Host not reachable".format(Q.server_host, Q.port)
    if common.grading_host_check(Q.server_host):
        auth = (Q.cluster_user, Q.cluster_pass)

        # Getting the nodes data from pools
        response = common.get_details(Q.server_host, 'pools/nodes', auth=auth)
        msg = "{0}: Unable to get cluster information".format(Q.server_host)
        if response:
            nodes = response.json().get('nodes')
            msg = "{0}: Node is not in the cluster".format(Q.server_host)
            for node in nodes:
                server = common.get_fqdn(Q.server_host)
                if server in node.get('hostname'):
                    extra_path = 'nodes/{0}'.format(node.get('otpNode'))
                    node_response = common.get_details(
                        Q.server_host, extra_path, auth=auth
                    )
                    msg = (
                        "{0}: Unable to get node information"
                        .format(Q.server_host)
                    )
                    if node_response:
                        score, msg = checks.ck011(
                            Q.server_host, node_response.json(),
                            Q.data_path, Q.index_path
                        )
                    break
    common.score_check(score, 'CK011', msg)


if __name__ == '__main__':
    sys.exit(main())

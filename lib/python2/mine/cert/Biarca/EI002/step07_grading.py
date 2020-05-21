#!/usr/bin/env python

"""
step07_grading.py will do the following task:

1. Connects to Couchbase Server using superuser credentials.
"""

import os
import sys
from certtools import args_parse
from certtools.couchbase.utils import common, checks


class Q():
    args = args_parse(args=sys.argv)
    server_host = args.seg1
    port = os.environ['CB_Cluster_PortWebUi']
    cluster_user = os.environ['CB_Cluster_UserSuper']
    cluster_pass = os.environ['CB_Cluster_PassSuper']


def main():
    # Checking for the couchbase server installation
    score = 0
    msg = "{0}:{1} - CB Host not reachable".format(Q.server_host, Q.port)
    if common.grading_host_check(Q.server_host):
        auth = (Q.cluster_user, Q.cluster_pass)

        # Getting the nodes details from the pool
        response = common.get_details(Q.server_host, 'pools/nodes', auth=auth)

        # Checking the configuration of super user credentials and services
        score, msg = checks.ck012(Q.server_host, response)
    common.score_check(score, "CK012", msg)


if __name__ == '__main__':
    sys.exit(main())

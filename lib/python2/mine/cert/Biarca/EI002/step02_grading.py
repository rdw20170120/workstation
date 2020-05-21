#!/usr/bin/env python

"""
step02_grading.py will do the following tasks:

1. Verifying RAM allocations.
2. Verifying available services.
3. Verifying Full-Text Search (FTS) Service is not available.
"""

import os
import sys
from certtools import args_parse
from certtools.couchbase.utils import common, checks


class Q():
    args = args_parse(args=sys.argv)
    server_host = args.seg1
    services = args.seg2
    data_ram = args.seg3
    index_ram = args.seg4
    port = os.environ['CB_Cluster_PortWebUi']
    cluster_user = os.environ['CB_Cluster_UserSuper']
    cluster_pass = os.environ['CB_Cluster_PassSuper']


def main():
    # Checking for the couchbase server installation
    services = [service.strip() for service in Q.services.split(',')]
    if common.grading_host_check(Q.server_host):
        auth = (Q.cluster_user, Q.cluster_pass)

        # Getting the nodes details from the pool
        response = common.get_details(Q.server_host, 'pools/nodes', auth=auth)
        if response:

            # Checking the RAM allocations
            exp_quotas = {'memoryQuota': Q.data_ram}
            if int(Q.index_ram) != 0:
                exp_quotas['indexMemoryQuota'] = Q.index_ram
            score, msg = checks.ck008(
                Q.server_host, exp_quotas, response.json()
            )
            common.score_check(score, "CK008", msg)

            for node in response.json().get('nodes'):
                server = common.get_fqdn(Q.server_host)
                if server in node.get('hostname'):

                    # Checking services to be configured
                    if int(Q.index_ram) == 0:
                        try:
                            rem_index = services.index("index")
                            del services[rem_index]
                        except:
                            pass
                    node_services = node.get('services')
                    score, msg = checks.ck009(
                        Q.server_host, node_services, services
                    )
                    common.score_check(score, "CK009", msg)

                    # Checking for fts service is not configured
                    score, msg = checks.ck010(Q.server_host, node_services)
                    common.score_check(score, "CK010", msg)
                    break
        else:
            common.score_check(
                0, "CK008",
                "{0}: Unable to get node details".format(Q.server_host)
            )
    else:
        common.score_check(
            0, "CK008",
            "{0}:{1} - Host not reachable".format(Q.server_host, Q.port)
        )


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python

"""
step02_answer.py will do the following tasks:

1. Deploys Data,index and query services.
2. Allocates RAM for data and index servcice.
"""

import os
import requests
import sys
from certtools import args_parse, debug
from certtools.couchbase.utils import common


class Q():
    args = args_parse(args=sys.argv)
    server_host = args.seg1
    data_ram = args.seg3
    index_ram = args.seg4
    cluster_name = args.seg5
    port = os.environ['CB_Cluster_PortWebUi']
    services = args.seg2


def configure(extra_path, data):
    """Configuring couchbase server node.
    """
    url = 'http://{0}:{1}/{2}'.format(Q.server_host, Q.port, extra_path)
    common.make_request(requests.post, url, data=data)


def main():
    common.check_host(Q.server_host)
    debug('{0} - Couchbase installation : OK'.format(Q.server_host))

    # Setting the DNS name
    dns_name = common.get_fqdn(Q.server_host)
    data = {'hostname': dns_name}
    configure('node/controller/rename', data)
    debug('{0} - Configured DNS name'.format(Q.server_host))

    # provisioning services in the cluster
    services = [service.strip() for service in Q.services.split(',')]
    if Q.index_ram == 0:
        try:
            rem_index = Q.services.index("index")
            del Q.services[rem_index]
        except:
            pass
    data = {'services': ",".join(services)}
    configure('node/controller/setupServices', data)
    debug('{0} - Services are deployed'.format(Q.server_host))

    # Allocating RAM for data and index services
    # setting cluster name
    data = {'memoryQuota': Q.data_ram,
            'indexMemoryQuota': Q.index_ram,
            'clusterName': Q.cluster_name}
    if Q.index_ram == 0:
        data = {'memoryQuota': Q.data_ram,
                'clusterName': Q.cluster_name}
    configure('pools/default', data)
    debug('{0} - RAM for data and index services are allocated'
          .format(Q.server_host))

    # Setting index storage
    data = {'storageMode': 'forestdb'}
    configure('settings/indexes', data)
    debug('{0} - configured index storage setting'
          .format(Q.server_host))


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python

import os
import sys
import requests

from exam import *

from certtools import args_parse
from certtools.couchbase.utils import common


class Q():
    args = args_parse(args=sys.argv)

    cluster_pass = get_cluster_user_pass()
    cluster_user = get_cluster_user_name()
    port_web_ui = get_port_web_ui()
    hosts_server = get_hosts_server()


def single_node_info():
    for host_server in [host.strip() for host in Q.hosts_server.split(',')]:
        auth = (Q.cluster_user, Q.cluster_pass)
        try:
            common.check_host(host_server)
        except Exception as e:
            if 'Host not reachable' in str(e):
                print("***************", host_server, "***************")
                print("CB server is not installed or not running")
                print()
                continue
        else:
            url = 'http://{0}:{1}/pools/nodes'.format(host_server, Q.port_web_ui)
            response = requests.get(url, auth=auth)
            if response.status_code == 200:
                nodes = response.json().get('nodes')
                for node in nodes:
                    if host_server in node.get('hostname').split(':')[0]:
                        node_address = node.get('hostname').split(':')[0]
                        node_status = node.get('status')
                        services = node.get('services')
                        print("***************", node_address, "**************")
                        print("Node Status     :", node_status)
                        data_ram = response.json().get('memoryQuota')
                        index_ram = response.json().get('indexMemoryQuota')
                        print("Data RAM Quota  :", data_ram)
                        print("Index RAM Quota :", index_ram)
                        print("Services        :", ','.join(services))
                        print()
            else:
                print("***************", host_server, "***************")
                print("CB server is installed but not configured")
                print()


def cluster_info():
    nodes_list = []
    final_list = []
    for host_server in [host.strip() for host in Q.hosts_server.split(',')]:
        auth = (Q.cluster_user, Q.cluster_pass)
        server_fqdn = common.get_fqdn(host_server)
        node_count = 0
        if server_fqdn.strip() in final_list:
            continue
        nodes_list = []
        cluster_name = ""
        response = common.get_details(
            server_fqdn, 'pools/default?etag=111&waitChange=1', auth=auth
        )
        if response:
            cluster_name = response.json().get('clusterName')
            nodes = response.json().get('nodes')
            for node in nodes:
                node_count += 1
        if node_count >= 1:
            for host in nodes:
                nodes_list.append(host.get('hostname').split(':')[0])
                final_list.append(host.get('hostname').split(':')[0])
            print("Nodes in the cluster:", cluster_name)
            print("*****************************************")
            print('\n'.join(nodes_list))
            print()
            # Rack awareness
            response = common.get_details(
                nodes_list[0], 'pools/default/serverGroups',
                auth=(Q.cluster_user, Q.cluster_pass)
            )
            if response:
                print("Server Groups in the cluster:", cluster_name)
                print("*****************************************")
                for group in response.json().get('groups'):
                    nodes = []
                    for node in group.get('nodes'):
                        nodes.append(node.get('hostname').split(':')[0])
                    if nodes != []:
                        group_name = group.get('name')
                        print(group_name, "\n**********")
                        print('\n'.join(nodes))
                        print()

            # Bucket Details
            url = (
                'http://{0}:{1}/pools/default/buckets/'
                .format(nodes_list[0], Q.port_web_ui)
            )
            response = common.make_request(
                requests.get, url, auth=(Q.cluster_user, Q.cluster_pass)
            )
            if response and response.status_code == 200:
                buckets = []
                for bucket in response.json():
                    buckets.append(bucket.get('name'))
                if buckets != []:
                    print("Bucket(s) in the cluster:", cluster_name)
                    print("*********************************")
                    print('\n'.join(buckets))
                    print()
                else:
                    print("****No Buckets in the cluster:", cluster_name, "***")
                    print()


def main():
    single_node_info()
    cluster_info()


if __name__ == '__main__':
    sys.exit(main())


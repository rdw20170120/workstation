#!/usr/bin/env python

import os
import requests
from certtools.couchbase.utils import common


def ck000(file_name):
    score = 0
    msg = "{0}: File not created".format(file_name)
    if os.path.exists(file_name):
        score = 1
        msg = "{0}: File created".format(file_name)
    return score, msg


def ck001(ssh, server):
    score = 0
    msg = '{0}: NTP is not running'.format(server)
    ntp_status = common.get_cmd_status(
        ssh, 'sudo systemctl status ntpd | grep Active', 'active (running)'
    )
    if ntp_status:
        score = 1
        msg = '{0}: NTP is running'.format(server)
    return score, msg


def ck002(ssh, server):
    score = 0
    msg = '{0}: CB server is not disabled'.format(server)
    exit_status, stdout, stderr = common.execute_command(
        ssh, 'sudo /opt/couchbase/etc/couchbase_init.d status'
    )
    if exit_status == 3:
        output = stdout.read().replace('\n', '')
        if 'is not running' in output:
            score = 1
            msg = '{0}: CB server is disabled'.format(server)
    return score, msg


def ck003(ssh, server):
    score = 0
    msg = '{0}: ntpstat is not synchronized with server'.format(server)
    ntpstat_status = common.get_cmd_status(
        ssh, 'ntpstat', 'synchronised to NTP server'
    )
    if ntpstat_status:
        score = 1
        msg = '{0}: ntpstat is synchronized with server'.format(server)
    return score, msg


def ck004(ssh, server):
    score = 0
    msg = '{0}: Swappiness is not configured'.format(server)
    swap_value = common.get_cmd_status(ssh, 'cat /proc/sys/vm/swappiness')
    try:
        swap_int = 30
        if swap_value is not False:
            swap_int = int(swap_value)
    except (ValueError, SyntaxError) as e:
        msg = '{0}: {1}'.format(server, e)
    else:
        if swap_int == 0:
            score = 1
            msg = '{0}: Swappiness is configured'.format(server)
    return score, msg


def ck005(ssh, server):
    score = 0
    msg = '{0}: THP is not disabled'.format(server)
    expected_output = 'always madvise [never]'
    thp_enable = common.get_cmd_status(
        ssh, 'cat /sys/kernel/mm/transparent_hugepage/enabled',
        expected_output
    )
    thp_defrag = common.get_cmd_status(
        ssh, 'cat /sys/kernel/mm/transparent_hugepage/defrag',
        expected_output
    )
    if thp_enable and thp_defrag:
        score = 1
        msg = '{0}: THP is disabled'.format(server)
    return score, msg


def ck006(ssh, server):
    score = 0
    msg = "{0}: Couchbase is not running".format(server)
    cb_status = common.get_cmd_status(
        ssh, 'sudo /opt/couchbase/etc/couchbase_init.d status',
        'is running'
    )
    if cb_status:
        score = 1
        msg = "{0}: Couchbase is running".format(server)
    return score, msg


def ck007(server):
    score = 0
    msg = "{0}: Not reachable at 8091".format(server)
    if common.grading_host_check(server):
        score = 1
        msg = "{0}: Reachable at 8091".format(server)
    return score, msg


def ck008(server, exp_quotas, response):
    score = 1
    msg = "{0}: RAM quotas are allocated for the services".format(server)
    for service, quota in exp_quotas.items():
        if int(quota) != response.get(service):
            score = 0
            msg = (
                "{0}: RAM quotas are not allocated for the services"
                .format(server)
            )
            break
    return score, msg


def ck009(server, node_services, services):
    score = 0
    msg = "{0}: Required services are not configured".format(server)
    if all(serv.strip() in node_services for serv in services):
        score = 1
        msg = "{0}: Required services are configured".format(server)
    return score, msg


def ck010(server, node_services):
    score = 0
    msg = "{0}: FTS service is configured".format(server)
    if 'fts' not in node_services:
        score = 1
        msg = "{0}: FTS service is not configured".format(server)
    return score, msg


def ck011(server, node_data, directory_data, directory_index):
    hdd_data = node_data.get('storage').get('hdd')
    score = 0
    msg = "{0}: Data and index directories not configured".format(server)
    if(hdd_data and hdd_data[0].get('path') == directory_data and
       hdd_data[0].get('index_path') == directory_index):
        score = 1
        msg = (
            "{0}: Data and index directories are configured"
            .format(server)
        )
    return score, msg


def ck012(server, response):
    score = 0
    msg = "{0}: Unable to read the cluster information".format(server)
    if response:
        score = 1
        msg = "{0}: Superuser credentials configured".format(server)
    return score, msg


def ck013(node, server):
    msg = "{0}: Added to the cluster".format(server)
    return 1, msg


def ck014(server, group, groups):
    score = 0
    msg = '{0} is not allocated to the group: {1}'.format(server, group)
    if server in groups.get(group, {}):
        score = 1
        msg = '{0} is allocated to the group: {1}'.format(server, group)
    return score, msg


def ck015(client, response, bucketname):
    score = 0
    msg = '{0}: Unable to read buckets information'.format(client)
    if response and response.status_code == 200:
        msg = '{0}: {1} - Bucket not exists'.format(client, bucketname)
        for bucket in response.json():
            # Checking for bucket with the given name
            if(bucketname == bucket.get('name') and
               bucket.get('bucketType') == 'membase'):
                score = 1
                msg = (
                    '{0}: {1} - Bucket exists in cluster'
                    .format(client, bucketname)
                )
                break
    return score, msg


def ck016(client, response, bucketname, doc_count=280322):
    for bucket in response.json():
        # Checking bucket with correct documents count
        if(bucketname == bucket.get('name') and
           bucket.get('basicStats', {}).get('itemCount') == doc_count):
            return 1
    return 0


def ck017(results, file):
    score = 0
    msg = '{0}: File does not contian correct document count'.format(file)
    for result in results:
        # Checks for result count
        if result.get('$1') == 280322:
            score = 1
            msg = (
                '{0}: File contains correct document count {1}'
                .format(file, result.get('$1'))
            )
            break
    return score, msg


def ck018(response, host_cluster, bucket_name, index_name):
    """Checking the index created with correct definition on the
       specified bucket."""
    score = 0
    msg = "{0}: Failed to get index status".format(host_cluster)
    if response:
        for index in response.json().get('indexes'):
            if(index.get('bucket') == bucket_name and
               index.get('index') == index_name and
               index.get('definition').lower().startswith('create index')):
                score = 1
                msg = (
                    '{0}: Index is created on the {1} bucket'
                    .format(host_cluster, bucket_name)
                )
                break
        else:
            msg = (
                '{0}: Index is not created on the {1} bucket'
                .format(host_cluster, bucket_name)
            )
    return score, msg


def ck019(results, client, file):
    # Checks the content having correct results and no errors
    score = 0
    msg = (
        '{0}: {1} File contains errors/incorrect results'
        .format(client, file)
    )
    if results:
        doc_types = ['country', 'playlist', 'sub-region',
                     'track', 'userprofile']
        file_doc_types = []
        for result in results:
            file_doc_types.append(result.get('type'))
        if sorted(doc_types) == sorted(file_doc_types):
            score = 1
            msg = (
                '{0}: {1} File exists, contain correct results and'
                ' no errors'.format(client, file)
            )
    return score, msg


def ck020(results, client, file):
    """Checks for the file content having correct result and no errors."""
    score = 0
    msg = (
        '{0}: {1} File contains errors/incorrect results'
        .format(client, file)
    )
    if results:
        doc_types = {
            'country': 258, 'playlist': 132844, 'sub-region': 23,
            'track': 97216, 'userprofile': 49981
        }
        file_doc_types = []
        for result in results:
            if not doc_types.get(result.get('type')) == result.get('$1'):
                return score, msg
            file_doc_types.append(result.get('type'))
        if sorted(list(doc_types.keys())) == sorted(file_doc_types):
            score = 1
            msg = (
                '{0}: {1} File exists, contains correct results '
                'and no errors'.format(client, file)
            )
    return score, msg


def ck021(results, client, file):
    # Checks the content having correct result count  and no errors
    score = 0
    msg = (
        '{0}: {1} file contains errors/incorrect result count'
        .format(client, file)
    )
    if results:
        if len(results) == 10:
            score = 1
            msg = (
                '{0}: {1} File exists, contains correct '
                'result count and no errors'
                .format(client, file)
            )
    return score, msg


def ck022(results, host_cluster, client, bucket_name, file, auth, key):
    score = 0
    msg = (
        '{0}: {1} file contains errors/incorrect result count'
        .format(client, file)
    )
    if results and len(results) == 1:
        filedata = results[0].get(bucket_name, {})
        """Checks the content of the result"""
        step06_query = (
            'SELECT * FROM {0} USE KEYS "{1}"'
            .format(bucket_name, key)
        )
        try:
            response = common.execute_query(
                host_cluster, step06_query, auth
            )
            json_response = response.json()
        except Exception as e:
            msg = '{0}: {1}'.format(client, e)
        else:
            msg = '{0}: Output contains wrong result'.format(client)
            if(json_response.get('status') == 'success' and
               len(json_response.get('results')) == 1):
                bucket = json_response.get('results')[0].get(bucket_name, {})
                for key in bucket:
                    if bucket[key] != filedata.get(key):
                        break
                else:
                    score = 1
                    msg = (
                        '{0}: Output contains correct result'
                        .format(client)
                    )
    return score, msg


def ck023(results, client, bucket_name, file, key):
    score = 0
    msg = (
        '{0}: {1} - Output not contains metadata'
        .format(client, file)
    )
    if results and results[0].get('$1', {}).get('id') == key:
        score = 1
        msg = (
            '{0}: {1} - Output contains metadata'
            .format(client, file)
                )
    return score, msg


def ck024(size_status, client, stdo):
    score = 0
    msg = "{0}: Unable to read fileSize".format(client)
    if size_status == 0:
        try:
            file_size = int(stdo.read().strip())
        except ValueError:
            file_size = 0
        if file_size >= 323 and file_size <= 333:
            score = 1
            msg = (
                "{0}: Backup file exist with size {1}M"
                .format(client, file_size)
            )
        else:
            msg = (
                "{0}: Backup file size must be in between 323M"
                " and 333M".format(client)
            )
    return score, msg


def ck025(response, host_source, bucket_source, bucket_target, uuid):
    score = 0
    msg = "{0}: Unable to read the tasks information".format(host_source)
    if response.status_code == 200:
        for task in response.json():
            if task.get('type') == 'xdcr' and \
               task.get('status') == 'running' and \
               task.get('source') == bucket_source and \
               task.get('target').endswith(bucket_target) and \
               uuid in task.get('target'):
                score = 1
                msg = "{0}: XDCR replication created".format(host_source)
                break
        else:
            msg = (
                "{0}: XDCR replication not created/not running"
                .format(host_source)
            )
    return score, msg


def ck026(bucket_name, response):
    score = 1
    msg = '{0}: Bucket deleted'.format(bucket_name)
    for bucket in response:
        if bucket_name == bucket.get('name'):
            score = 0
            msg = '{0}: Bucket not deleted'.format(bucket_name)
            break
    return score, msg


def ck027(size_sts, stdo, client, server):
    score = 0
    msg = (
        '{0}: Unable to read log file size for {1}'
        .format(client, server)
    )
    if size_sts == 0:
        file_size = int(stdo.read().strip())
        msg = '{0} : cbcollect_info not generated'.format(server)
        if file_size > 0:
            score = 1
            msg = '{0} : cbcollect_info generated'.format(server)
    return score, msg


def ck028(nodes, fqdn_list, host_cluster):
    score = 0
    msg = "{0}: Nodes not removed from cluster".format(host_cluster)
    nodes_deleted = True
    for node in nodes:
        node_address = node.get('hostname').split(':')[0]
        if node_address in fqdn_list:
            nodes_deleted = False
            break
    # Checking that the nodes are removed from the cluster or not
    if nodes_deleted and fqdn_list:
        score = 1
        msg = "{0}: Nodes removed from cluster".format(host_cluster)
    return score, msg


def ck029(ssh, server):
    score = 0
    msg = "{0}: CB server is not uninstalled".format(server)
    status, stdout, stderr = common.execute_command(
        ssh, 'sudo /etc/init.d/couchbase-server status'
    )
    if(status == 1):
        score = 1
        msg = "{0}: CB server is uninstalled".format(server)
    return score, msg


def ck030(response, host_cluster):
    score = 0
    msg = "{0}: {1}".format(host_cluster, response.reason)
    if response.status_code == 200:
        nodes = response.json().get('nodes')
        for node in nodes:
            if node.get('clusterMembership') == "inactiveAdded":
                msg = (
                    "{0}: Cluster rebalance is in pending state"
                    .format(host_cluster)
                )
                break
        else:
            score = 1
            msg = "{0}: Cluster is rebalanced".format(host_cluster)
    return score, msg


def ck031(response, auth, host_target, src_host, port, src_bucket, bucket_target):
    score = 0
    msg = 'Cluster reference not deleted'
    for cluster_reference in response.json():
        remote_server = cluster_reference.get('hostname').split(':')[0]
        if remote_server == host_target:
            tasks_url = (
                'http://{0}:{1}/pools/default/tasks'
                .format(src_host, port)
            )
            res = requests.get(tasks_url, auth=auth)
            if res.status_code == 200:
                for task in res.json():
                    if task.get('type') == 'xdcr' and \
                       task.get('source') == src_bucket and \
                       bucket_target in task.get('target') and \
                       cluster_reference.get('uuid') in task.get('target'):
                        score = 0
                        msg = 'XDCR replication is not deleted'
                        break
                else:
                    score = 1
                    msg = 'XDCR replication is deleted'
                break
    else:
        score = 1
        msg = 'Cluster reference and XDCR are deleted'
    return score, msg


def ck032(result, bucket_name, old_key):
    score = 0
    msg = 'Output contains no correct results'
    for bucket in result:
        if bucket_name in list(bucket.keys()):
            msg = 'Userprofile not selected with key - {0}'.format(old_key)
            if bucket.get(bucket_name).get('username') in old_key:
                score = 1
                msg = 'Userprofile selected with key - {0}'.format(old_key)
                break
    return score, msg


def ck033(json_response, bucket_name, some_key):
    return common.check_count(
        json_response, bucket_name, some_key, "All playlists are"
    )


def ck034(json_response, bucket_name, some_key):
    return common.check_count(
        json_response, bucket_name, some_key, "Userprofile is"
    )


def ck035(result):
    return common.check_result_count(result)


def ck036(errors, file):
    """Return score 1 if output contains error with code 4000
       and message with No index available on keyspace
       """
    msg = "File Does not contain correct result: {0}".format(file)
    score = 0
    for error in errors:
        if error.get('code') == 4000 and\
           'No index available on keyspace' in error.get('msg', ''):
            msg = "File contains correct result: {0}".format(file)
            score = 1
            break
    return score, msg


def ck037(response, new_key, old_key, bucket_name):
    score = 0
    if response.json().get('status') == 'success':
        msg = 'Userprofile not inserted with new key - {0}'.format(new_key)
        for bucket in response.json().get('results'):
            if bucket_name in list(bucket.keys()):
                if bucket.get(bucket_name).get('username') in old_key:
                    score = 1
                    msg = (
                        'Userprofile inserted with new key - {0}'
                        .format(new_key)
                    )
                    break
    else:
        msg = response.json().get('errors', {})
    return score, msg


def ck038(response, old_key):
    score = 0
    if response.json().get('status') == 'success':
        msg = 'Userprofile not deleted with key {0}'.format(old_key)
        if response.json().get('metrics').get('resultSize') == 0:
            score = 1
            msg = 'Userprofile deleted with key {0}'.format(old_key)
    else:
        msg = response.json().get('errors', {})
    return score, msg


def ck039(old_res, new_res, new_key):
    score = 0
    msg = 'Playlists not updated with {0}'.format(new_key)
    if(old_res.json().get('metrics').get('resultCount') == 0 and
       new_res.json().get('metrics').get('resultCount') > 1):
        score = 1
        msg = 'Playlists updated with {0}'.format(new_key)
    return score, msg


def ck040(result):
    return common.check_result_count(result)


def ck041(result):
    return common.check_result_count(result, count=49850)


def ck042(result):
    return common.check_result_count(result, count=66618)


def ck043(result, bucket_name, doc_type, doc_username):
    return common.check_results(result, bucket_name, doc_type, doc_username)


def ck044(result, bucket_name, doc_type, doc_username):
    return common.check_results(result, bucket_name, doc_type, doc_username)


def ck045(bucket_name, primary_index, response):
    score = 0
    msg = (
        "{0}: Primary index not created on : {1}"
        .format(primary_index, bucket_name)
    )
    for index in response:
        if index.get('bucket') == bucket_name and \
           index.get('index') == primary_index and \
           index.get('definition').lower() \
           .startswith('create primary index'):
            score = 1
            msg = (
                "{0}: Primary index created on : {1}"
                .format(primary_index, bucket_name)
            )
            break
    return score, msg


def ck046(target_file, results, bucket_name, primary_index):
    score = 0
    msg = "{0}: contains Incorrect results".format(target_file)
    for result in results:
        check_status = common.check_operator(
            result.get('plan'), bucket_name, primary_index
        )
        if check_status is True:
            score = 1
            msg = "{0}: contains correct results".format(target_file)
    return score, msg


def ck047(target_file, results):
    score = 0
    msg = "{0}: contains Incorrect results".format(target_file)
    if not results:
        return score, msg
    documents = {
        "country": 258, "playlist": 132844, "sub-region": 23,
        "track": 97216, "userprofile": 49981
    }
    for result in results:
        if result.get('countDocuments') != documents.get(result.get('type')):
            break
    else:
        score = 1
        msg = (
            "{0}: contains correct document count of each type"
            .format(target_file)
        )
    return score, msg


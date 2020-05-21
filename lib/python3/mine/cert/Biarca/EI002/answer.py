#!/usr/bin/env python

"""
answer.py will call the answers of each step:
"""

import os
import sys
from certtools import args_parse


class Q():
    args = args_parse(args=sys.argv)
    server_host = args.seg1
    services = args.seg2
    data_ram = args.seg3
    index_ram = args.seg4
    cluster_name = args.seg5
    port = os.environ['CB_Cluster_PortWebUi']
    cluster_user = os.environ['CB_Cluster_UserSuper']
    cluster_pass = os.environ['CB_Cluster_PassSuper']
    data_path = os.environ['CB_Cluster_DirData']
    index_path = os.environ['CB_Cluster_DirIndex']
    debug = args.debug if hasattr(args, 'debug') else 0


def main():
    os.system('python step01_answer.py')
    os.system(
        'python step02_answer.py --seg1="{0}" --seg2="{1}" --seg3="{2}"'
        ' --seg4="{3}" --seg5="{4}" --debug={5}'
        .format(Q.server_host, Q.services, Q.data_ram, Q.index_ram,
                Q.cluster_name, Q.debug)
    )
    os.system(
        'python step03_answer.py --seg1="{0}" --debug={1}'
        .format(Q.server_host, Q.debug)
    )
    os.system(
        'python step04_answer.py'
    )
    os.system(
        'python step05_answer.py'
    )
    os.system(
        'python step06_answer.py'
    )
    os.system(
        'python step07_answer.py --seg1="{0}" --debug={1}'
        .format(Q.server_host, Q.debug)
    )


if __name__ == '__main__':
    sys.exit(main())

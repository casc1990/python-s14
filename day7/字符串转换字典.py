#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/5 22:42'
import socket,os,json

str1 = '''
zk_version      3.4.8--1, built on 02/06/2016 03:18 GMT
zk_avg_latency  0
zk_max_latency  11
zk_min_latency  0
zk_packets_received     3854089
zk_packets_sent 3947945
zk_num_alive_connections        32
zk_outstanding_requests 0
zk_server_state follower
zk_znode_count  6637
zk_watch_count  141
zk_ephemerals_count     23
zk_approximate_data_size        524291
zk_open_file_descriptor_count   62
zk_max_file_descriptor_count    204800
'''
c = {}
print (type(str1))
for i in str1.split('\n'):
    i = i.strip()
    if not i:continue
    j = i.strip().split()
    #print (j[0],j[1])
    c[j[0]] = j[1]
    print (c)

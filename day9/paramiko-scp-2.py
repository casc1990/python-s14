#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/31 14:05'

import paramiko
#创建连接实例
transport = paramiko.Transport(('192.168.128.128', 22))
transport.connect(username='root', password='123456')
#创建sftp实例，并把服务器连接实例传进去
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
#sftp.put('D:\python-project\s14\day9\paramiko-scp-2.py', '/tmp/paramiko-scp-2.py')  #指定路径上传
#sftp.put('paramiko-scp-2.py', '/tmp/paramiko-scp-2.py')
# 将remove_path 下载到本地 local_path
sftp.get('/root/linux_scp_get.txt', 'form_linux')

transport.close()
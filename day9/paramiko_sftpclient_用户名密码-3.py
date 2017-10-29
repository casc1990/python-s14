#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/31 14:05'

import paramiko
#创建连接通道
transport = paramiko.Transport(('192.168.128.128', 22))
transport.connect(username='root', password='123456')
#创建sftp实例，并把服务器连接实例传进去
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('D:\python-project\s14\day9\paramiko_sftpclient_用户名密码-3.py', '/tmp/paramiko_sftpclient_用户名密码-3.py')  #指定路径上传
#sftp.put('paramiko_sftpclient_用户名密码-3.py', '/tmp/paramiko_sftpclient_用户名密码-3.py')
# 将remove_path 下载到本地 local_path
sftp.get('/root/linux_scp_get.txt', 'form_linux')

#在sftp服务器创建目录
sftp.mkdir('/home/soft',mode=755)
#删除sftp服务器指定目录
sftp.remove('/home/soft')
#改名
sftp.rename('/home/soft/test.sh','/home/soft/testfile.sh')
#获取文件列表
sftp.listdir('/home/soft')


transport.close()
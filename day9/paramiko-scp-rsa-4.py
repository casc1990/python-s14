#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/31 18:21'
import paramiko
#基于公匙认证(前提：服务器之间配置好了密匙认证，即a服务器的公匙要存在b服务的authorized_keys中，然后a可以直接登陆b)
#private_key = paramiko.RSAKey.from_private_key_file(r'C:\Users\pengbo\.ssh\id_rsa')
private_key = paramiko.RSAKey.from_private_key_file('id_rsa')  #指定客户端的私匙文件
#建立连接通道
transport = paramiko.Transport(('192.168.128.128', 22))
transport.connect(username='root', pkey=private_key)  #指定私匙
#创建sftp实例，并把服务器连接通道传进去
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('id_rsa', '/tmp/id_rsa')
# 将remove_path 下载到本地 local_path
sftp.get('/root/linux_scp_get.txt', r'D:\backup\abc.txt')

transport.close()
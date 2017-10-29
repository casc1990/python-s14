#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/31 18:41'
print ('sshclinet使用transport建立连接')
import paramiko
#基于密码认证
#建立连接通道
transport = paramiko.Transport(('192.168.128.128', 22))
transport.connect(username='root', password='123456')
#实例化ssh客户端，并把建立的连接通道对象传递进去
ssh = paramiko.SSHClient()
ssh._transport = transport  #相当于ssh.connect
#执行命令
stdin, stdout, stderr = ssh.exec_command('df')
print (stdout.read().decode())
#关闭连接
transport.close()


#基于密匙认证
private_key = paramiko.RSAKey.from_private_key_file('id_rsa')
#建立连接通道
transport = paramiko.Transport(('192.168.128.128', 22))
transport.connect(username='root', pkey=private_key)
#实例化ssh客户端，并把建立的连接通道对象传递进去
ssh = paramiko.SSHClient()
ssh._transport = transport  #相当于ssh.connect
#执行命令
stdin, stdout, stderr = ssh.exec_command('df')
print (stdout.read().decode())
#关闭连接
transport.close()
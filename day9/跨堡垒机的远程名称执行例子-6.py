#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/10/29 23:17'

import paramiko
import os,sys,time

blip='172.19.22.240'
bluser='pengbo14'
blpasswd='Pb1105041@'

prot = 22
hostname = '172.27.53.40'
username = 'root'
private_key = paramiko.RSAKey.from_private_key_file('id_rsa')
paramiko.util.log_to_file('paramiko.log')  #记录日志

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpasswd,port=prot)

channel = ssh.invoke_shell() #创建回话，开启命令调用
channel.settimeout(10)  #会话命令执行的超时时间

channel


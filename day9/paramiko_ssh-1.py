#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/31 14:05'
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.128.128', port=22, username='root', password='123456')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('free -m')
# 获取命令结果
stdout_result = stdout.read()
stderr_result = stderr.read()
if stdout_result:
    print('command result:', stdout_result.decode())
else:
    print ('Error:',stderr_result)

# 关闭连接
ssh.close()
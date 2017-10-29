#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/31 17:15'
import paramiko
#基于公匙认证(前提：服务器之间配置好了密匙认证，即a服务器的公匙要存在b服务的authorized_keys中，然后a可以直接登陆b)
#private_key = paramiko.RSAKey.from_private_key_file(r'C:\Users\pengbo\.ssh\id_rsa')
private_key = paramiko.RSAKey.from_private_key_file('id_rsa')  #指定客户端的私匙文件

# 创建SSH对象
ssh = paramiko.SSHClient()
# 加载本地公匙效验文件，默认为 ~/.ssh/know_hosts，非默认路径需手工指定。（不在know_host文件里的，不允许登陆）
ssh.load_system_host_keys()
# 允许连接不在know_hosts文件中的主机。AutoAddPolicy()表示自动添加主机名和密匙到know_hosts文件
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.128.128', port=22, username='root',pkey=private_key) #连接时使用私匙

# 执行命令
stdin, stdout, stderr = ssh.exec_command('free -g',timeout=5)
# 获取命令结果
result = stdout.read()
print (result.decode())

# 关闭连接
ssh.close()
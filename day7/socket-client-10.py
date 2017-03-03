#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

import socket
client = socket.socket() #建立socket链接，默认地址簇为ipv4，协议为tcp
#client1 = socket.socket(family=AF_INET6, type=SOCK_DGRAM)  指定ipv6，udp协议
client.connect(('localhost',6969))  #发起连接
client.send(b'hello world!')  #发送数据（bytes类型只能接收ascci数据）
# client.send('我要下载'.encode('utf-8'))  #发送中文
data = client.recv(1024)  #接收对方发过来的数据
print ('recv:', data)  #打印数据
#print ('recv:', data.decode())  #打印中文数据
client.close()  #关闭连接
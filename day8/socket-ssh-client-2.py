#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/7 21:14'
import socket,os
client = socket.socket()
client.connect(('localhost',6677))
while True:
    cmd = input('please input command: ').strip()
    if len(cmd) == 0:continue #如果输入的为空，继续输
    client.send(cmd.encode('utf-8'))  #发送命令
    cmd_res_size = client.recv(1024)  #接受命令的长度
    print ('命令的总大小为:',cmd_res_size)
    client.send('命令结果的长度我已经收到了,开始发送命令结果吧.'.encode('utf-8'))  #回应确认包
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()): #判断接收的数据长度，一直循环接收，直到接收完
        data = client.recv(1024) #获取每次接收到的数据
        received_data += data  #追加到received_data
        received_size += len(data) #累加每次接收的长度
    else:
        print ('cmd res received done!')
        print (received_data.decode())  #接收完了，打印所有数据

client.close()
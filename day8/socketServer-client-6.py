#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import socket
client = socket.socket()
client.connect(('localhost',9999))  #连接服务端
while True:
    msg = input('>>:').strip() #接受用户端输入
    if len(msg) ==0:continue  #socket不能发送空
    client.sendall(msg.encode('utf-8')) #sendall表示发送所有的数据
    #send每次只能发送一定量的数据（32K），数据过大，要使用sendall，相当于循环send
    data = client.recv(102400)  #接收数据，可以指定每次接收多少
    print (data)

client.close()  #关闭连接
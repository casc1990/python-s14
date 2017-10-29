#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import socket,os
server = socket.socket() #建立socket连接
server.bind(('localhost',6969)) #绑定端口
server.listen(5)  #监听。5表示最多可以有5个排队的请求
while True:  #不断的接受请求
    #同一时间只能处理同一客户端连接
    conn,addr = server.accept()  #相应请求（有请求就响应，无请求就一直等待）
    while True: #客户端退出，会发送空数据，这个while循环是为了跳到server.accept
        data = conn.recv(102400) #接收请求
        if not data:  #客户端不发送数据，或者断开，就返回到server.accept(),响应下一个请求
            print ('client has lost...')
            break
        res = os.popen(data.decode()).read()  #执行用户发过来的指令，并保存结果
        conn.send(res.encode('utf-8'))  #将结果发送给客户端
server.close()  #关闭连接
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import socket
server = socket.socket()  #实例化socket连接
server.bind(('localhost',6969))  #绑定服务地址和端口，注意ip和端口要以元祖的形式
server.listen()  #监听（开启端口）
conn,addr = server.accept()  #server.accept会返回两个值。（等待客户端连接）
#conn是客户端连接过来而在服务器上为其生成的一个连接实例，addr：表示连接过来的客户端端的ip和端口
print (conn,addr)  #打印连接实例和连接的ip和端口
data = conn.recv(1024)  #接收客户端发送过来的数据
print ('recv:',data)  #打印数据
conn.send(data.upper())  #向连接的客户端实例发送数据（发送的数据必须是bytes类型）

server.close()
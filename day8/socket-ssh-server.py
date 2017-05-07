#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/7 21:15'
import socket,os
server = socket.socket()
server.bind(('localhost',6677))
server.listen(5)
while True:
    conn,addr = server.accept()
    print ('新的连接：',addr)
    while True:
        print ('receiveding command：')
        data = conn.recv(1024)
        if len(data) == 0:
            print ('客户端可以已经断开了...')
            break
        print ('开始执行命令',data)
        cmd_res = os.popen(data.decode()).read() #接受字符串，执行结果也是字符串.
        print ('命令总长度：',len(cmd_res)) #socket每次发送的字节数不一致
        if len(cmd_res) == 0: #popen执行失败，返回值就为0
            cmd_res = 'command is not found....'
        #发送命令结果分两步，先发送命名结果的长度，在发结果；因为客户端每次接收命令大小是有限的
        conn.send(str(len(cmd_res.encode())).encode('utf-8')) #发送命令结果的长度给客户端（因为可能有中文，所有先转换为bytes类型
            #在统计长度（len(cmd_res.encode()），然后在将数字转换为字符串，在将字符串转换为bytes类型 ）
        conn.send(cmd_res.encode('utf-8'))  #发送命令执行结果
        print ('send done!')

server.close()

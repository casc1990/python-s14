#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/13 20:23'
import socket,os,hashlib
server = socket.socket()
server.bind(('localhost',6767))
server.listen(5)
while True:
    print ('新的连接来了..')
    conn,addr =server.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            print ('连接断开了..')
            break
        cmd,filename = data.decode().split()  #获取文件名（假设用户只能使用 get filename）
        print (filename)
        if os.path.isfile(filename): #判断文件是否存在
            f = open(filename,'rb')  #打开文件
            m = hashlib.md5()   #生成MD5对象
            file_size = os.stat(filename).st_size   #获取文件大小
            conn.send(str(file_size).encode('utf-8')) #发送文件大小
            conn.recv(1024) #等待客户端确认收到文件大小数据
            for i in f:
                print ('开始发送数据：',i.decode())
                m.update(i) #MD5数据（相当于累加求MD5），
                conn.send(i)
            print('文件的MD5:', m.hexdigest())
            conn.send(m.hexdigest().encode('utf-8')) #发送文件MD5值（可能最后一次文件发送和发送MD5会粘包，粘包在客户端处理）
            f.close()
        print ('发送完毕.')
server.close()


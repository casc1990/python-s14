#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/13 20:24'
import socket,os,hashlib
client = socket.socket()
client.connect(('localhost',6767))
while True:
    cmd = input('please input get file >> ').strip()
    if len(cmd) ==0:continue
    if cmd.startswith('get'):
        client.send(cmd.encode('utf-8'))  # get 123.txt
        server_response = client.recv(1024) #接收服务端发送的文件大小（file_size）
        client.send(b'ready to recv file:') #确认已经收到文件大小
        file_total_size = int(server_response.decode()) #文件总大小
        received_size = 0
        filename = cmd.split()[1]  #获取文件名
        f = open(filename + '.new','wb') #新建文件，因为在同一个文件夹下操作，以.new区分
        m = hashlib.md5()
        while received_size < file_total_size: #循环接收数据
            ''' 为了防止粘包，我们先发送大小，然后只接收指定大小的数据  '''
            if file_total_size - received_size > 1024: #收取前N次
                size = 1024
            else:size = file_total_size -received_size #收取最后一次（因为最后一次又可能不到1024）
            data = client.recv(size) #接收指定大小的数据
            m.update(data) #md5数据
            print ('len()获取的字符串长度其实就是等于字符串的大小')
            received_size += len(data) #累加接收到的文件大小。(len获取的字符串总和等于文件总大小)
            f.write(data)
            #print (file_total_size,received_size)
        else:
            new_file_md5 = m.hexdigest()  #计算的新文件的MD5
            print ('file recv done!',file_total_size,received_size)
            f.close()
        server_file_md5 = client.recv(1024) #接收到的服务端的MD5
        print ('server file md5: ',server_file_md5.decode())
        print ('client file md5: ',new_file_md5)
client.close()




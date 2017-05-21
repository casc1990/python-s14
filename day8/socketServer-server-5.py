#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/5/14 18:43'
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler): #第一步：自己定义类，继承BaseRequestHandler
    '''
    必须自己创建一个请求处理类，并且这个类要继承BaseRequestHandler，
    并且还要重写父类里的handle()方法
    '''
    def handle(self):  #重写handle()方法（客户端的请求逻辑在这里定义）
        '''
        socketserver.BaseRequestHandler里的__init__(self, request, client_address, server):
        request:客户端对象,client_address:客户端的ip+端口（元祖形式）,server：服务器信息
        '''
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print ('request from: ' ,self.client_address[0])
                print ('recv data:',self.data)
                #if not self.data:
                #    print ('客户端断开了..')
                #    break
                #print ('python3中socketServer断开会抛出异常，我们不用自己判断了，捕获异常就可以了')
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print ('error:',e)
                print ('client %s:%s close connection....' %(self.client_address[0],self.client_address[1]))
                break

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # 实例化一个socketServer，并传递服务器的ip和你上面写的请求处理类给这个socketServer
    #server = socketserver.TCPServer((HOST,PORT),MyTCPHandler) #第二步：TCPServer是单线程。（实例化socketServer）
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler) #第二步：使用多线程socketServer（实例化socketServer）
    #循环的处理客户端请求
    server.serve_forever() # 第三步（循环的处理客户端请求）

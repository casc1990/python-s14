#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/11/1 22:57'

#gil：全局解释器锁 （确保任何时候都只有一个Python线程执行）

#gil虽然可以保证同一时刻只能有一个python线程执行.
# 因为线程共享内存地址，如果多个线程修改了同一数据，cpu处理每个线程的时间是一定的，
# 比如：假设你有A,B两个线程，此时都 要对num 进行减1操作， 由于2个线程是并发同时运行的，
# 所以2个线程很有可能同时拿走了num=100这个初始变量交给cpu去运算，当A线程去处完的结果是99，
# 但此时B线程运算完的结果也是99，两个线程同时CPU运算的结果再赋值给num变量后，结果就都是99。

#在python2.7上执行可能会结果不一样
import time
import threading


def addNum():
    global num  # 在每个线程中都获取这个全局变量
    print('--get num:', num)
    time.sleep(1)
    num -= 1  # 对此公共变量进行-1操作


num = 100  # 设定一个共享变量
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()

print('final num:', num)

print ('python3解决了全局锁的问题，为程序自动加锁了，保证了数据的一致性')

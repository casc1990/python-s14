#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#Time ： 2017/11/11 18:26
import threading,time
import random


'''
def light():
    print ('\033[42;1m--green light on---\033[0m')
    print ('\033[43;1m--yellow light on---\033[0m')
    print('\033[41;1m--red light on---\033[0m')
'''
event = threading.Event()
def light():
    count = 0
    while True:
        if count < 10:  #绿灯(0-10秒)
            event.clear()   #清除标志位
            print ('\033[42;1m--green light on---\033[0m')
        elif count < 13: #黄灯（10-13秒）
            print('\033[43;1m--yellow light on---\033[0m')
        elif count < 20: #变红灯（13-20秒）
            event.set()  # 设置标志位
            print  ('\033[41;1m--red light on---\033[0m')
        else:   #大于20秒
            count = 0
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():   #如果标志位被设置
            print('red light, [%s] waiting...' % name)
            event.wait()
        else:
            print('[%s] runing..' % name)
        time.sleep(1)

light = threading.Thread(target=light,)
light.start()

car1  = threading.Thread(target=car,args=('tesla',))
car1.start()



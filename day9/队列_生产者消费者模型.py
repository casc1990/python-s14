#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/11/19 20:47'

import threading
import queue,time


q = queue.Queue()
def producer():
    i = 1
    while True:
        q.put('包子%s' %i)
        print ('包子%s做好了!' %i)
        i += 1
        time.sleep(0.1)


def consumer(name):
    while True:
        print ('[%s] 取到了[%s],并且吃了它..' %(name,q.get()))
        time.sleep(0.5)

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer,args=('alex',))
c1 = threading.Thread(target=consumer,args=('zhangsan',))

p.start()
c.start()
c1.start()

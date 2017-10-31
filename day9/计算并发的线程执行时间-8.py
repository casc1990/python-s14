#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/10/31 23:44'

import threading
import time

def run(n):
    print ('run task: ',n)
    time.sleep(3)
start_time = time.time()
result_list = []
for i in range(50):  #并发开启50个线程
    t = threading.Thread(target=run,args=('t-%d' %i,))
    t.start()
    result_list.append(t)

for i in result_list:  #判断每个线程是否执行完
    i.join()
else:
    print ('all threads has finished...'.center(80,'-'))
    print ('cost:',time.time() - start_time)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/10/31 23:44'

import threading
import time

def run(n):
    print ('run task: ',n)
    time.sleep(3)
    print (threading.current_thread()) #输出：<Thread(Thread-5, started 13932)> 子线程
start_time = time.time()
result_list = []
for i in range(50):  #并发开启50个线程
    t = threading.Thread(target=run,args=('t-%d' %i,))
    #主线程退出时不管守护线程是否退出，设置成守护线程后，线程就不重要了。必须在启动线程之前设置，之后就不能设置了
    t.setDaemon(True)  #将当前线程设置成守护线程（主线程不会等守护线程执行完在退出。）
    t.start()
    result_list.append(t)

print (threading.active_count()) #输出：51  统计当前活跃的线程数（1个主线程和50个子线程）
for i in result_list:  #判断每个线程是否执行完
    i.join()

print ('all threads has finished...'.center(80,'-'))
print (threading.current_thread())  #输出：<_MainThread(MainThread, started 1728)> 打印当前线程，MainThread表示主线程
print ('cost:',time.time() - start_time)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#Time ： 2017/11/11 17:03
print ('threading.BoundedSemaphore(5):指定同时可以有几个线程同时运行。'
       '作用：维护线程池，控制访问量')
import threading, time


def run(n):
    semaphore.acquire()
    time.sleep(2)
    print("run the thread: %s\n" % n)
    semaphore.release()


if __name__ == '__main__':

    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(30):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')
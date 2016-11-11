#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
#高阶函数实现装饰器
def timer(func):
    start_time = time.time()
    stop_time = time.time()
    print ('the func run %s' %(stop_time-start_time))
    return func

def test1():
    time.sleep(3)
    print ('in the test1')

def test2():
    time.sleep(3)
    print ('in the test2')

#timer(test1)
test1=timer(test1)
test1()   #没有改变调用方式，没有修改源代码。（高阶函数）
#print (time.time())

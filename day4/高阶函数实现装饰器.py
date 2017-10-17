#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
#高阶函数实现装饰器
def timer(func):
    print ('添加功能一')
    print ('添加功能二')
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

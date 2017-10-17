#!/usr/bin/env python
#-*- coding:utf-8 -*-
#高阶函数+嵌套函数 实现装饰器
import time
def timer(func):  #timer(test1)  func=test1
    def deco():
        start_time = time.time()
        func()   #run test1()
        stop_time = time.time()
        print ('the func run %s' %(stop_time-start_time))  #增加功能
    return deco   # return test1(返回test1的内存地址)

@timer    #test1=timer(test1)  给谁加，装饰谁
def test1():
    time.sleep(3)
    print ('in the test1')

@timer
def test2():
    time.sleep(3)
    print ('in the test2')

#timer(test1)
#test1=timer(test1)
test1()   #run deco() 没有改变调用方式，没有修改源代码。（高阶函数 + 嵌套函数）
test2()   #run deco() 没有改变调用方式，没有修改源代码。（高阶函数 + 嵌套函数）
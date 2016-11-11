#!/usr/bin/env python
#-*- coding:utf-8 -*-
#实现带参数的装饰器
import time
def timer(func):
    def deco(*args,**kwargs):  #让deco函数可以接受参数 (可以接受任意参数或者空)
        start_time = time.time()
        func(*args,**kwargs)    #将deco接受的参数传给func函数；test(*args,**kwargs)    可以接受任意参数或者空
        stop_time = time.time()
        print ('the func run %s' %(stop_time - start_time))
    return deco

@timer   #test1=timer(test1)
def test1(name,age):
    print ('name : ', name,age)

@timer   #test1=timer(test1)
def test2():
    print ('test2')
test1('alex',22)    #将参数传入函数
test2()




#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import os,time
#装饰器（装饰函数）
# 定义：本质是函数，用来装饰其他函数。（为其他函数附件功能）
#原则：1.不能修改被装饰的函数的源代码
#     2.不能修改被装饰的函数的调用方式（对函数是透明的，被装饰函数无感知）

#实现装饰器知识储备： 高阶函数 + 嵌套函数
#    1. 函数即变量
#    2. 高阶函数
#        a. 把一个函数名作为实参传给另外一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
#        b. 返回值中包含函数名。（在不修改函数的调用方式的情况下为其添加功能）
#    3. 嵌套函数
        #在一个函数的函数体内用def去申明一个函数
'''
#函数即变量
def bar():
    print ('in the bar')
print (bar)  #直接打印bar，只会返回bar函数的内存地址
bar_new = bar
bar_new()  # bar_new()=bar() (函数即变量)
'''
'''
#python执行过程
#setup_1
def bar():  #相当于定义了“变量”bar，函数体为变量值
    print('in the bar')
    test()
def test():
    print ('in the test')
bar()  #这样可以执行（因为python是解释性语言，从上往下执行，先将bar的函数体存入内存,接着解释 \
                    #test函数，所有调用bar函数时，bar函数里的test是可以执行的）
#etup_2
def bar():  #相当于定义了“变量”bar，函数体为变量值
    print('in the bar')
    test()
bar()    #这样调用会报错（因为定义完bar后，就执行了bar函数，此时test函数还未解释到）
def test():
    print ('in the test')
'''
#高阶函数
'''
    #把一个函数名作为实参传给另外一个函数
def bar(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print ('the test run %s' %(stop_time-start_time))
def test():
    print ('in the test')
    time.sleep(3)
bar(test)   #在不修改被装饰函数源代码的情况下为其添加功能（高阶函数特性一）
    #返回值中包含函数名
def bar():
    print ('in the bar')
    time.sleep(3)
def test(func):
    print (func)   #增加的新功能
    return func
#test(bar)  #打印bar函数的内存地址，不会打印返回值（print (func)）
#print (test(bar))  #打印bar函数的内存地址和打印返回值（print (func)和 return func）
#test(bar())  #把函数的返回值传给函数；test(bar)将内存地址传给函数
bar = test(bar)
bar()   #不修改函数的调用方式，为函数添加了功能。(bar=test(bar)的返回值，调用
        #返回值相当于调用了上面定义的bar()函数，这里的bar()不等于上面的bar函数，
        #名字一样，只是想演示“不修改函数的调用方式，为函数添加了功能”  )
'''
#函数嵌套
def bar():
    print ('in the bar')
    def test():  #在函数体内定义函数
        print ('in the test')
    test()
bar()




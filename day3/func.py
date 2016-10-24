#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#定义: 函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可
#特性: 代码复用性、可扩展性、可维护性
#函数就是面向过程的程序设计的基本单元。

def func1():   #定义func1函数，没有参数
    '''Function description document '''   #函数说明文档
    print ('in the func1')               #函数主体（逻辑部分）
    return 0                             #函数的返回值，默认返回none

def func2():
    '''Function description document '''
    print('in the func2')
func1()     #执行函数
x = func1()
y = func2()

print ('func1 return is %s!' %x)    #返回定义的返回值
print ('func2 return is %s!' %y)    #返回默认值none
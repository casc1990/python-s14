#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#函数返回值的作用：根据返回值可以定位到函数是否被成功执行，调用者可以根据返回值判断自己的代码该如何操作


def test1():
    print ('in the test1!')     #默认返回none

def test2():
    print ('in the test2!')
    return 1                  #返回指定的对象
    print ('func end')        #return之后的不会被执行（函数结束并退出）

def test3():
    print ('in the test3!')
    return 1,'hello',['aa','BB'],{'name':'alex'}    #函数返回值以元祖的方式返回所有需要返回的

x = test1()
y = test2()
z = test3()
print (x)
print (y)
print (z)
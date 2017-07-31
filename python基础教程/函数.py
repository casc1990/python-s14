#!/usr/bin/env python
# -*- coding:utf-8 -*-

#函数文档
def square(x):
    'Calculates the square of the number x.'
    return  x*x
a = square(5)
print (a)  #25
print (square.__doc__)  #Calculates the square of the number x.
print (help(square))  #help函数也可以看到帮助信息

def test():
    print ('this is printed')
    return
    print ('this is not')
b = test() #this is printed
print (b)  #None
#return语句后面的不会被执行,return默认返回None




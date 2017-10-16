#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import os

#可迭代对象：（可以被for循环的对象）
#    1.拥有__iter__方法的数据类型都是可迭代的。
#    2.生成器和带yield的函数
a = '12'
a1 = a.__iter__()
b = [1,2]
b1 = b.__iter__()
c = {1:'a',2:'b'}
c1 = c.__iter__()
d =(1,2)
d1 = d.__iter__()
e = set((1,2))
e1= e.__iter__()
with open('test.txt','w') as f:
    f.write('123,test')
    f.write('\n456.hello')
f = open('test.txt','r')
f1 = f.__iter__()
print (type(a),type(b),type(c),type(d),type(e))
print (next(a1),next(b1),next(c1),next(d1),next(e1),next(f1))  #next = __next__
print (a1.__next__(),b1.__next__(),c1.__next__(),d1.__next__(),e1.__next__(),f1.__next__())
#   总结：list、tuple、dict、set、str、file都是可迭代的
from collections import Iterable
#使用isinstance()可以判断一个对象是否是Iterable（可迭代）对象，返回Ture或者False
print (isinstance(a,Iterable))
print (isinstance(b,Iterable))
print (isinstance(123,Iterable))  #int(数字)不是可迭代对象

from collections import Iterator
#*可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
print ('-----华丽的分界线-----')
print (isinstance((x for x in range(10)),Iterator))  #True 生成器(列表和生成器的区别就在于[]和())
print (isinstance([],Iterator))  #False
print (isinstance({},Iterator))    #False
print (isinstance('abc',Iterator))  #False
#生成器都是可迭代对象，但list、dict、str虽然是Iterable(可迭代的)，却不是Iterator(迭代器)。


#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
#生成器都是迭代器对象
print ('iter()函数可以把对象变成Iterator(迭代器)')
print (isinstance((x for x in range(10)),Iterator))  #Ture 生成器都是迭代器
print (isinstance(iter([]),Iterator))  #使用iter()函数可以把列表转换成迭代器
print (isinstance([],Iterator))  #列表虽然是可迭代的，但是不是迭代器
print (isinstance(iter({}),Iterator))
print (isinstance({},Iterator))

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#迭代器包含生成器
#Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，\
#    直到没有数据时抛出StopIteration错误。Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
print ('''
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
应用场景：
    1.xrange(),xreadlines() python2.7
    2.for循环都是通过迭代器实现的  python2.7和python3.0
事例：
for x in [1, 2, 3, 4, 5]:
    print (x)
等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
''')
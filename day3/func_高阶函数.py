#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#"函数式编程"是一种"编程范式"，python对函数式编程提供部分支持，python更强大的是面向对象编程
#函数式编程和函数是两回事。不是同一个概念
#一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x,y,f):  #f=abs函数。
    return f(x) + f(y)   #abs函数是求绝对值得，求x和y的绝对值
res = add(2,-3,abs)   #传递了abs函数作为实际参数
print (res)
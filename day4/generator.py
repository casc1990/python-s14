#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#列表生成式：是Python内置的非常简单却强大的可以用来创建list的生成式。
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环。
a = [i+1 for i in range(9)]   #列表生成式
b = [x * x for x in range(1, 11) if x % 2 == 0]  #列表生成式可以加判断
c = [i+j for i in 'abc' for j in 'ABC']  #还可以使用双重循环
dict = {'A':'a','B':'b','C':'c','D':'d'}
d = [i + '=' + j for i,j in dict.items()]  #使用变量生成
print (a)
print (b)
print (c)
print (d)

#生成器 --- 延迟生成
# 特性：1.生成器必须是可迭代的。和迭代器有着一定的渊源关系，可以理解为自定义迭代器
#      2.延迟生成。只有在调用的时候才会生成相应的数据
#      3.只记录当前位置
#      4.有__next__方法  2.7版本next()
my_generator = (x**x for x in range(4))  #定义了生成器
my_list = [x**x for x in range(4)]  #列表和生成器的区别就在于[]和()
print (my_generator)
print (my_list)
#for i in my_generator:print (i)   #生成器是可迭代的
s = my_generator.__next__()  #生成器的__next__方法,下次访问或者循环就会从这个位置往后读取数据了
print (s)









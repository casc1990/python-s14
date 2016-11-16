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
s2 = next(my_generator)    #通过next函数也可以迭代生成器对象
print (s2)
#斐波拉契数列:除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):   #普通函数
    n,a,b = 0,0,1  #n代表取几个值  a代表第一个元素   b代表第二个元素
    while n < max:  #n定义了取几个值
        print (b)
        a,b=b,a+b   #a,b=b,a+b相当于t=(b,a+b) 则 a = t[0] ，b= t[1]
        n+=1
print ('华丽的分界线')
fib(6)
#生成器格式的斐波拉契数列
#generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#  而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib2(max):
    n,a,b=0,0,1
    while n < max:
        yield b   #如果一个函数定义中包含yield关键字,就是生成器
        a,b=b,a+b
        n = n + 1
    return 'done'  #定义返回值，使用__nex__方法和next()函数可以拿到返回值，如果使用for不能得到返回值
e = fib2(3)
print (e.__next__())  #使用__next__方法
print (e)

#yield 例子
def old():   #依次打印1,3,5
    print('step 1')
    yield 1  #报存命令的执行位置
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = old()
print (o.__next__())
print (o.__next__())
print (o.__next__())
#last =o.__next__()
#print (last)   #第四次已经没有了，所有报错了

#生成器函数：使用__nex__方法和next()函数可以拿到返回值，如果使用for不能得到返回值
g = fib2(6)
while True:  #生成器对象使用循环是拿不到返回值的，无效循环，捕获异常
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:  #是这种类型的报错
        print('Generator return value:', e.value)   #打印返回值
        break










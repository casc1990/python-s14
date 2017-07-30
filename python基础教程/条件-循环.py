#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/7/4 22:24'
print ('Age:',42)  #输出 Age: 42
print ('Hello',',','Mr','Gumby' ) #输出 Hello , Mr Gumby
#print时 ',' 会被替换成空格

import os
import sys,time
from math import sqrt
from math import isclose,isinf
from math import *
import math as foobar
from math import ceil as cl

#序列解包
x,y,z = 1,2,3
print (x,y,z) #输出 1 2 3
x,y = y,x
print (x,y,z) #输出 2 1 3 （交换变量的值）
scoundrel = {'name':'Robin','girlfriend':'Marion'}
key,values = scoundrel.popitem()
print (key,values) #输出 name Robin  （函数至少返回一个以上的值并且打包成元祖）
#x,y,z = 1,2,3,4  报错 （赋值的数位要一一向对）

print (True == 1) #输出 True
print (1+1 == 3) #输出 False
print (False+True+1 == 2) #输出 True （True和False可以参加运算）
print (bool('False')) #输出 True
print (bool(0))  #输出 False
print (bool(''))  #输出 False
print (bool(' '))  ##输出 True （注意：空格为真）
#False、None、0、'' 、() 、[] 、{} :空和False、None为假，其余为真
#bool函数判断函数真假

#if语句
'''
name = input('what is your name? ')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print ('Hello! Mr Gumby')
    elif name.startswith('Mrs'):
        print ('Hello! Mrs. Gumby')
    else:
        print ("hello! stranger")
'''
#比较运算符：
print ('== 、< 、> 、>= 、<= 、!= 、is 、is not 、in 、 not in')
x = y = [1,2,3]
z = [1,2,3]
print (x ==y) #输出 True
print (x == z) #输出 True
print (x is z) #输出 False
#总结：使用==运算符来判定两个对象是否相等，使用is判断两者是否是同一个对象

'''
name = input('what is your name? ')
if 's' in name:
    print ('your name contains the letter "s" ')
else:
    print ('your name does not contains the letter "s" ')
'''
#判断对象中是否有指定的字符

#字符串比较
print ('alpha' < "beta") #输出 True
print ('FnOrD'.lower() == 'Fnord'.lower()) #输出 True
print ([1,2] < [1,3])  #输出 True
print ([2,[1,4]] < [2,[1,5]])  #输出 True
print (chr(97))  #输出a （查询asll码为97的字符）
print (ord('a')) #输出97 （查询a的asll码）
#元素比较，依次按顺序比较

#断言
result = 2 if 1+1==3 else 3
print (result) #输出3 （如果1+1==3成立，result=2，否则result=3）
age = 1
assert 0<age<100  #输出True
age =-1
#assert 0<age<100 #报错
#assert 0<age<100,'the age must be realistic'  #报错，报错里会打出指定的字符串。（解释断言）
#断言就是判断一句话的是否为真


#while循环（当while条件为真，一致循环）
q = 1
while q < 100:
    print (q)
    q += 1
#假如q小于100，执行循环体里的内容

name = ''
while not name:
    name = input('Please enter your name? ').strip()  #strip去除输入左右两边的空格
print ('Hello！%s' % name)
#使用while循环确保用户输入了用户名

#for循环（在指定的范围内循环）
words = ['this','is','an','ex','parrot']
for i in words:
    print (i)
#使用for循环，可以循环可迭代对象

#range（范围函数）
range(5,10) #5-9
range(20) #0-19
range(0,20,2) #0-19之间的偶数（步进为2）
#xrange和range使用方法一致，区别在于xrange是生成器对象（延时生成），range一次性创建整个序列。xrange适合大序列

d = {'x':1,'y':2,'z':3}
#字典循环方法一
for i in d:
    print ('%s value is %s' %(i,d[i]))
#字典循环方法二
for key,value in d.items():
    print ('%s value is %s' %(key,value))

#迭代工具
names = ['anne','beth','george','damon']
age = [12,45,32,102]
for i in range(len(names)):
    print (names[i],'is',age[i],'years old')
#并行迭代案例（并行迭代对象的长度要相等）

www = zip(names,age)
print (www) #输出 [('anne',12),('beth',45),('george',32),('damon',102)]
zip(range(5),range(8)) #[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]   以长度最短的序列为准
#zip(序列1，序列2,序列N..)变量解包,将给定的序列组成元祖的列表，以长度最短的序列为准

for name,age in zip(names,age):
    print (name,'is',age,'years old!')
#用zip函数迭代序列

names = ['anne','beth','george','damon']
for index,key in enumerate(names):
    print (key,'is index',int(index)-1)
#enumerate(seq) 打印序列的编号和值

names = ['anne','beth','george','damon']
names.sort() #原地修改，无返回值（排序）
names.reverse() #原地修改，无返回值（反转）
print (sorted(names)) #排序，不修改原数据
print (list(reversed(names))) #反转，不修改原数据
#sort、reverse 修改原数据  sorted、reversed 不修改原数据

#break、continue
import math
print (math.sqrt(99))
for i in range(99,0,-1): #步进为-1
    root = math.sqrt(i)
    if root == int(root):
        print (i)
        break   #计算100以内的算术平方根
#break:跳出最内层循环
#continue: 跳到下一轮循环的开头继续循环

#while True
while True:
    words = input('please enter a word: ')
    if  not words: break
    print ('the words was'+ words)
    break
#while True语句一定要有退出条件

#循环中的else子句
from math import sqrt
for i in range(99,80,-1):
    root = sqrt(i)
    if root == int(root):
        print (i)
        break  #如果循环是因为break退出的，else不会执行
else: #循环正常执行完，做些善后的工作
    print ("Didn't find it!")
#for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
s = ["a111", "b222", "c333", "d444", "e555"]
found = False
for c in s:
    if c.startswith("c"):
        found = True
        print ("发现以字母c开头的项")
        break
if not found:
    print ("没有发现以字母c开头的项")
#给变量打标签。结合if实现对不同条件的处理

#列表推导式
print ([x*x for x in range(10)])  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print ([x*x for x in range(10) if x % 2 ==0]) #[0, 4, 16, 36, 64]

print ([(x,y) for x in range(2) for y in range(2)]) #[(0, 0), (0, 1), (1, 0), (1, 1)]
#等价于
result = []
for x in range(2):
    for y in range(2):
        result.append((x,y))
print (result)  #[(0, 0), (0, 1), (1, 0), (1, 1)]

girls = ['alice','bernice','clarice']
boys = ['chris','arnold','bob']
print ([b for b in boys for g in girls if b[0] == g[0]]) #['chris', 'arnold', 'bob']
#列表推导式：[ 循环体 循环条件1 循环条件2..逻辑判断..], 注意是[],不是(),结果生成的是列表

print ('pass在循环里什么都不会做的，起代码占位符作用')
x = 1
del x
print ('del函数删除对象的变量名称')

#exec、eval函数
exec('b=4+5')
print (b) #输出：9
abc = 45
exec('abc+=1')
print (abc) #输出：46
#exec（'string'）:执行字符串代码块

print (eval(input('enter an expression: '))) #输入：4+5  输出：9
print (eval('3**3')) #输出：27
#eval（'string'）:表达式求值

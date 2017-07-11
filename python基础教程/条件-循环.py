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
assert 0<age<100 #输出True
age =-1
assert 0<age<100 #报错
assert 0<age<100,'the age must be realistic'  #报错，报错里会打出指定的字符串。（解释断言）
#断言就是判断一句话的是否为真


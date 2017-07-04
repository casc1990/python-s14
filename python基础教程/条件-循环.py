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


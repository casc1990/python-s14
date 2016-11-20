#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#思路：随机生成一个数字，判断这个数字是否等于指定的值，如果符合就讲数字追加到空列表中，
#      如果不符合，使用chr函数将大写字符追加到列表中，最后拼接字符串
import random,os
print (ord('A'))  #A-z的ascii表中的编号是65-90
print (chr(90))
print ('0到1的随机数：',random.random())   #random.random()会打印0到1的随机数
print (random.randint(1,5))   #random.randint()打印指定范围的随机数
print ('-------华丽的分界线---------')
a = ['a','b','c','d']
list_str = ''.join(a)  #list_str='abcd'  字符串拼接
lst = []  #定义空列表，存放随机生成的元素
for i in range(6):  #验证码为6位
    r = random.randint(0,5)   #随机生成一个0-5的数字
    if r == 2 or r == 4:  #判断产生的随机数字是2或者4，将数字追加到随机字符串列表中
        n = str(random.randint(0,9))
        lst.append(n)
    else:          #将大写字符追加到随机字符串列表中
        n = random.randint(65, 90)
        lst.append(chr(n))
result = "".join(lst)   #字符串拼接
print (result)   #打印随机字符串列表
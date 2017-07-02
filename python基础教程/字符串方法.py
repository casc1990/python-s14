#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/7/1 20:58'

str1 = "Monty Python's Flying Circus"
#find(sub, start=None, end=None)
print (str1.find('Monty')) #输出为 0 (在字符串中查找子串，返回最左侧索引，没找到返回-1)
print (str1.find('abc')) #输出为 -1
print (str1.find('Python',0,16)) #输出为 6 （指定起始位置和结束位置）

dirs = ['','usr','bin','env']
#join(iterable)
print ('/'.join(dirs))  #输出为：/usr/bin/env （以指定分隔符，将列表转换为字符串）
print ('C:' + '\\'.join(dirs)) #输出为 C:\usr\bin\env
print ('Python is very lange'.split()) #输出为['Python', 'is', 'very', 'lange'] （split和join正好相反）

print ('Trondheim Hammer Dance'.lower()) #输出为：trondheim hammer dance （转换为小写）
print ('Trondheim Hammer Dance'.upper()) #输出为 TRONDHEIM HAMMER DANCE
print ('trondheim hammer dance'.capitalize())  #首字符大写(同于 title())
print ('trondheim hammer dance'.center(50)) #宽度为50，居中显示

print ('trondheim hammer dance'.count('m'))  #统计

print ('This is a test'.replace('is','eez',4))  #替换，可以指定次数

print ('1+2+3+4'.split('+')) # 输出 ['1', '2', '3', '4']
print ('/usr/bin/env'.split('/')) #输出 ['', 'usr', 'bin', 'env']
#split是将字符串以指定的分隔符转换为列表，join是以指定的分隔符将序列转换为字符串

print ('      internal whitespace is kept      '.strip()) #输出internal whitespace is kept
print ('*** SPAM * for * everyone!!! ***'.strip('*')) #输出为 SPAM * for * everyone!!!
#strip是脱去两侧的指定的字符

from string import maketrans #导入模块
tables = maketrans('cs','kz') #生成转换表（将c替换为k；将s替换为z）
print ('this is an incredible test'.translate(tables)) # 输出 thiz iz an inkredible tezt
print ('this is an incredible test'.translate(tables,' ')) #输出 thizizaninkredibletezt
#translate用于替换单个字符，translate第二个参数是指定要删除的字符






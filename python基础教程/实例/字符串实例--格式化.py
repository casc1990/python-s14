#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/7/1 18:14'
from math import pi
'''
print ('%s plus %s equals %s ' %(1,1,2))  #输出 1 plus 1 equals 2
print ('price of eggs $%.3f' % (2.5)) #输出 price of eggs $2.500
print ('%.5s' % 'hello world') #输出为 hello
print ('%.*s' % (5,'hello world')) #输出为 hello (通过元祖传递宽度和精度)
print ('%010.3f' %pi)  #输出为 000003.142 （用0填充，宽度为10，精度为3的浮点类型）
print ('%-10.2f' %pi) #输出为 '3.14      ' (-表示左对齐)
print ('%+5d' % 10 + '\n' + '%+5d' % -10) #输出为 +10 -10 （+表示显示正负数）
'''
#example
#使用给定的宽度打印格式化后的价格列表
width = input('please enter width: ')
#价格那列字段的宽度
price_width = 10
#item那列的宽度等于总宽度(width)-价格的宽度(price_width)
item_width = width - price_width

header_format = '%-*s%*s'
text_format = '%-*s%*.2f'

print ('=' * width)
print (header_format % (item_width,'Item',price_width,'Price'))
print ('-' * width)
print (text_format % (item_width,'Apples',price_width,0.4))
print (text_format % (item_width,'Pears',price_width,0.5))
print (text_format % (item_width,'Dried',price_width,1.92))
print (text_format % (item_width,'Prunes',price_width,12))
print ('=' * width)



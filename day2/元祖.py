#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#元祖可以认为是只读列表，不能修改.使用小括号表示
name = ('zhangsan','lisi','wangwu','lisi')
name2 = (1,2,3,4)
name3 = name + name2   #元祖拼接
name4 = ()   #空元祖
del name4    #删除name4元祖
tup1 = (50)    # int类型
tup2 = (50,)   #只有1个元素时要加,否则不是元祖
tup3 = tup2 * 3  #元祖相乘
print (type(tup1),type(tup2))
print (name[0:3])    #元祖支撑切片
print (len(name))   #获取长度
print (name3,tup3)
print (name.count('lisi'))
print (name.index('lisi'))
'''
#元祖内置函数
len()
max()
min()
tuple()    #转换为元祖
'str' in (tuple)   #成员关系判断
for i in (tuple):print (i)   #元祖遍历
'''
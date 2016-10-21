#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
with open('yesterday','r',encoding='utf-8') as f:  #with...as（文件访问完了，会自动关闭）
    for line in f:
        print (line.strip())

with open('yesterday','r',encoding='utf-8') as f, \
     open('yesterday3', 'r', encoding='utf-8') as f2:   #python2.7以上可以2个文件（一行代码不易超过80字符）
    for line in f:
        print (line.strip())
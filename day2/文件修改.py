#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
f = open('yesterday','r',encoding='utf-8')
f_new = open('yesterday_new','w',encoding='utf-8')
for line in f:
    #print (line.strip())
    if '肆意的快乐等我享受' in line:
        line = line.replace('肆意的快乐等我享受','肆意的快乐等Alex享受')
    f_new.write(line)
f.close()
f_new.close()
f2 = open('abc.txt','w',encoding='utf-8')
f2.write('this is a test file')
f2.close()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

#2.7打开文件可以用open、file，但是在3.0中只能用open
f = open('yesterday',encoding='utf-8')  #因为默认window使用gbk字符编码，所有要使用utf-8，否则会报错
                                        #文件打开在内存中，将打开的文件复制给一个变量，记录文件句柄。
#print (f.readline())
data1 = f.read()    #文件读到行尾，指针就留在哪儿，在读就为空了
data2 = f.read()    #已经到行尾了，所有data2就等于空了
print (data1)
print ('---------'.center(50),data2)  # 打印为空
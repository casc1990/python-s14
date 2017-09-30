#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import sys,os
#old = sys.argv[1]   #第一个位置参数
#new = sys.argv[2]
print (len(sys.argv))   #获取命令行参数个数
print (sys.argv[0])    #打印脚本名
if len(sys.argv) != 3:        #所以参数个数从1开始算（不等于3都不对）
    print ('''请按如下格式替换内容：
         {0} 替换谁 替换成什么'''.format(sys.argv[0])) #参数不够给出提示（sys.argv[0]打印脚本名）
    sys.exit()
else:
    with open('yesterday','r',encoding='utf-8') as f,\
         open('yesterday_new','w',encoding='utf-8') as f2:
        for line in f:
            if sys.argv[1] in line:
                line = line.replace(sys.argv[1],sys.argv[2])   #替换（将传进来的一个参数换成第二个）
            f2.write(line)      #写到新文件里





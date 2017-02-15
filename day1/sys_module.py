#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import sys,os
#print (sys.path)
print (sys.argv)  #['sys_module', 'hehe', 'ls',-l] 打印文件的相对路径和传递的参数（列表形式）
print (sys.argv[0])  #['sys_module'] 打印文件的相对路径
print (os.system(sys.argv[2])) #执行shell的ls命令（os.system接收命令行参数，运行参数指令）
print (os.system(str(sys.argv[2])+' ' +str(sys.argv[3]))) # 执行 ls -l

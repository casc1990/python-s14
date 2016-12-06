#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import sys
#python sys模块-5.py 1 2 3 4 5 运行这个文件，加上参数
print (sys.argv)  #打印所有命令行参数列表。第一个元素是程序本身路径。['sys模块-5.py', '1', '2', '3', '4', '5']
print (sys.argv[0]) #打印程序本身路径。 输出为：sys模块-5.py
print (sys.argv[1]) #打印第一个参数。输出为：1
#sys.exit()        #退出程序，正常退出时exit(0)
print (sys.version)        #获取Python解释程序的版本信息
print (sys.maxsize)   #最大的Int值
print (sys.path)      #模块搜索路径
print (sys.platform)  #返回操作系统平台名称

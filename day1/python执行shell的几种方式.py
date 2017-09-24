#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/9/24 14:25'
import os,sys
import subprocess   #pyhon2中使用的是commands模块

#os.system会把执行的shell命令的结果输出到屏幕上，返回的是命令执行的状态码（0表示成功执行，非0执行不成功）
result = os.system('ls -lh')
#os.popen会将命令执行的结果报存到文件里，生成的是一个文件对象，可以对文件对象做各种操作
result2 = os.popen('ls -lh').readline()
#subprocess模块执行shell命令,返回值是元祖形式（0,'/usr/lib64/python2.7'）,包括命令执行状态码，命令的结果
result3 = subprocess.getstatusoutput('pwd')
result4 = subprocess.getoutput('pwd')  #输出 '/usr/lib64/python2.7'(返回命令结果)
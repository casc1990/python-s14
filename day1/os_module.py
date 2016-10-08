#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import os
os.system('dir')  #os.system不保存命令执行结果，只是打印到屏幕上
cmd_result = os.system('dir')  #保存的是命令的执行状态（0或者非0:0表示成功执行，非0表示不成功，同linux）
os.popen('dir').read()
cmd_result2 = os.popen('dir').read()  #os.popen可以保存命令执行的结果；os.system保存的是命令执行的状态
print ('--->',cmd_result,cmd_result2)  #打印命令执行状态和执行结果
os.mkdir('new_dir')  #新建目录

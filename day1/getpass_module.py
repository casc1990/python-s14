#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import getpass   #getpass模块在pycharm不能运行，在python解释器或者程序都是可以的
user = input('user: ')
passwd = getpass.getpass('passwd: ')
print (user,passwd)

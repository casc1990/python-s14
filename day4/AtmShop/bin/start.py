#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import os,sys
print (sys.path)
print (__file__)   #查看当前文件的相对路径。
print (os.path.abspath(__file__))   #os.path.abspath() 查看文件的绝对路径
abspath = os.path.abspath(__file__)
print (os.path.dirname(abspath))   #os.path.dirname() 查看文件的上级父目录名（/a/b 返回/a）
absdir = os.path.dirname(abspath)
print (os.path.dirname(absdir))  #查看文件的上上级父目录名
print (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   #获取到项目的根目录
root_absdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_absdir)
print (sys.path)
from core import main   #导入core目录里的main文件（因为把项目的根目录加入到环境变量中了，所有可以导入）
main.login()      #执行main文件里的login函数

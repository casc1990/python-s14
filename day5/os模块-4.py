#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
print (os.getcwd())  #pwd 查看当前工作目录
os.chdir('d:\\backup')  # cd d:\\backup  去到指定目录（windoss中路径要加\\）
os.chdir(r'd:\backup') # cd d:\\backup  去到指定目录 （r表示原始字符串，加\就可以）
print (os.getcwd())
print (os.curdir)  #返回当前目录: ('.') --不常用
print (os.pardir)  #获取当前目录的父目录字符串名：('..') --不常用
os.makedirs('d:\\backup\\a\\b\\c')  # mkdir -p 递归创建多级目录 (目录存在会报错)
os.removedirs(r'd:\backup\a\b\c')  #删除空目录。先检查c目录是否为空，空就删除，\
#                         接着判断b目录是否为空，为空，删除b。以此类推。因为backup目录不为空，所以删除了a\b\c目录
os.mkdir(r'd:\backup\a') # 创建单级目录
os.rmdir(r'd:\backup\a') #删除单级目录
print (os.listdir('.'))  # ls -la 列出指定目录下的所有文件和子目录，包括隐藏文件
print (os.listdir('..')) #列出上级目录所有文件或者目录，包括隐藏的
with open(r'd:\backup\w','w') as f:
    pass
#os.remove(r'd:\backup\w')   #删除文件
#os.rename(r'd:\backup\w','www')  #os.rename('oldname','newname')  重命名文件、目录
print (os.stat(r'd:\backup'))  #获取文件/目录信息
#  输出： os.stat_result(st_mode=16895, st_ino=1125899906920964,st_dev=1848412937, st_nlink=1, st_uid=0, st_gid=0, st_size=4096, st_atime=1481019057, st_mtime=1481019057, st_ctime=1470710532)
print (os.sep)    #输出操作系统的路径分割符
print (os.linesep) #行终止符
print (os.name)  #输出当前使用平台（nt：windows，linux：posix）

os.system('bash command')  #运行shell命令，直接显示。（不保存命令结果）
os.system('dir')
print (os.environ)   #获取系统环境变量

#path--路径相关
print (os.path.abspath(__file__))  #返回当前路径的绝对路径
print (os.path.abspath(r'd:\backup'))  #返回指定路径的绝对路径
print (os.path.split(__file__))  #将路径分割成目录和文件名二元组返回。('D:/python-project/python-s14/day5', 'os模块-4.py')
print (os.path.dirname(__file__)) #返回路径的目录名
print (os.path.basename(__file__)) #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。输出：os模块-4.py
print (os.path.exists(__file__))  #如果path存在，返回True；如果path不存在，返回False
print (os.path.isabs(__file__))     #如果path是绝对路径，返回True
print (os.path.isfile(__file__))   #如果path是不是文件，返回True。否则返回False
print (os.path.isdir(__file__))    #如果path是不是目录，则返回True。否则返回False






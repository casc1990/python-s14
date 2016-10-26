#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
需求 = '''
1、查
    输入：www.oldboy.org
    获取当前backend下的所有记录

2、新建
    输入：
        arg = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }

3、删除
    输入：
        arg = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }

需求
'''
import os,sys,json
result = []
flag = False
f = open('haproxy.conf','r',encoding='utf-8')

choice = input('你想对配置文件做什么操作：\n'
               '1)查询\n'
               '2)修改\n'
               '3)删除 \n'
               '4)其他任意字符退出 \n'
               '请输入你的选择的序号:')
if choice == '1':
    chocie2 = input('输入：')
    for line in f:
        #print (line)
        if "backend %{0}".format(chocie2).strip() in line :
        #if str.startswith('backend')+' '+chocie2 in line:
            flag = True
            print (flag)
            continue
        if flag == True:
            print (line)

elif choice == '2':
    print (2)
elif choice == '3':
    print (3)
else:
    sys.exit()
#for line in f:


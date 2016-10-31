#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import os,json,sys

def fetch(backend):               #定义查询的函数
    '''
    查询backend函数
    思路：1.读文件，找打backend + 用户输入的域名的行。
         2.将backend + 用户输入的域名的下一行到下一个backend开头的行的server记录找出来，追加到新列表中
         3.返回追加的列表和打印列表中的内容
    :param backend:
    :return:
    '''
    result = []      #空列表用来存查到的backend sever记录
    with open('haproxy.conf', 'r', encoding='utf-8') as f:   #打开文件
        flag = False      #设置标志位（当flag值改变，说明backend的记录找完了）
        for line in f:  #循环文件
            if line.strip() == 'backend ' + backend:  #查询用户输入的backend信息
                flag = True  #找到用户输入的值，修改标志位
                continue   #回到backend那行，打印server记录
            if line.startswith('backend'): #到第二个backend开始处，说明server记录已经找完了
                flag = False  #修改标志位
            if flag and line.strip():
               result.append(line)   #将找到的记录追加到列表
        return result   #返回列表
s = '{"bakend": "www.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}'
a = "{'key':'value'}"
print (type(s),s)
s1 = json.loads(s)  #json.loads 可以将字典或者列表形式的字符串转换成字典、列表(注意：字符串里的元素使用双引号"")
s2 = eval(s)     #eval 也可以将字典或者列表形式的字符串转换成字典、列表（字符串里的元素使用单双引号都可以）
s3 = eval(a)
print (type(s3),a)
print (type(s1),s1)
print (type(s2),s2)
def add(dict_info):
    dict_info = json.loads(dict_info)
    backend = dict_info['backend']
    server = dict_info['record']['server']
    weight = dict_info['record']['weight']
    maxconn = dict_info['record']['maxconn']
    add_backend_format = 'backend '+ dict_info['backend']
    add_context_format = 'server %s %s weight %d maxconn %d' %(server,server,weight,maxconn)
    result_list = fetch(dict_info['backend'])
    backend_and_server_list = []
    with open('haproxy.conf','r',encoding='utf-8') as old,\
         open('ha.conf','w',encoding='utf-8') as new:
        if result_list:
            if add_context_format in result_list:
                    print ('该域名的server记录已经存在了！')
                    sys.exit()
            else:
                backend_and_server_list.append(backend)
                backend_and_server_list.append(add_context_format)
        else:
            backend_and_server_list.append(backend)
            backend_and_server_list.append(add_context_format)
        for line in old:
            new.write(line)
        for line1 in backend_and_server_list:
            new.write(line1)
    os.rename('haproxy.conf','haproxy.conf.bak')
    os.rename('ha.conf','haproxy.conf')

#add(s)









'''
choice = input('你想对配置文件做什么操作：\n'
               '1)查询\n'
               '2)修改\n'
               '3)删除 \n'
               '4)其他任意字符退出 \n'
               '请输入你的选择的序号:')

while True:
    if choice == '1':
        choice2 = input('请输入要查询的域名：')
        res = fetch(choice2)
        for i in range(1):
            if res:
                for i in res:
                    print(str(i).strip())
            else:
                print ('你输入的 %s 域名不存在' % choice2)
                break
    if choice == '2':
        choice3 = input('请输入要添加的内容：')
        add(choice3)
'''

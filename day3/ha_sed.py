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
s = '{"backend": "eee.mage.edu","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}'
a = "{'key':'value'}"
print (type(s),s)
s1 = json.loads(s)  #json.loads 可以将字典或者列表形式的字符串转换成字典、列表(注意：字符串里的元素使用双引号"")
s2 = eval(s)     #eval 也可以将字典或者列表形式的字符串转换成字典、列表（字符串里的元素使用单双引号都可以）
s3 = eval(a)
print (s1['backend'])
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
    print (backend,server,weight,maxconn,add_backend_format,add_context_format)
    result_list = fetch(dict_info['backend'])  #调用fetch函数（查询用户的backend是否存在，把查询结果保存在result_list列表中）
    #逻辑：如果backend不存在文件中，说明要新增，把旧文件的内容都读入到新文件，然后在最后面写入用户传入的backend和server
    if not result_list:   #backend不存在
        with open('haproxy.conf', 'r', encoding='utf-8') as old, \
              open('ha.conf','w',encoding='utf-8') as new:  #打开旧文件，新建新文件
            for line in old:
                new.write(line)  #把旧文件全部写到新文件
            new.write('\n')  #加一个空行（每个backend之间有一个空行）
            new.write('\n' + add_backend_format + '\n')  #最后在把用户传入的backend和server写入到新文件的最后面
            new.write(" "* 8 + add_context_format + '\n')
    #逻辑：backend存在：
           #1.server也存在：源文件不用作任何操作。
           #2.server不存在：将用户传入的server记录追加到result_list（result_list中存在着backend查到的server结果 + 要新加的结果）。
           #                循环旧文件，追加新文件（一行一行的写，到用户输入的backend的地方，设置标志位，并把result_list写入到backend
           #                 的server段 ）
    else:  #backend存在
        result_list.append(add_context_format)   #将用户传入的server记录追加到result_list
        if add_context_format in result_list:   #backend和server都存在
            pass
        else:     #backend存在，server不存在
            with open('haproxy.conf', 'r', encoding='utf-8') as old, \
              open('ha.conf','w',encoding='utf-8') as new:
                flag = False    #设置标志位
                for line in old:
                    if line.startswith('backend') and line == add_backend_format:    #
                        flag = True
                        new.write(line)
                        for line in result_list:
                            new.write(" " * 8 +line + '\n')
                    if flag and line.startswith('backend'):
                        flag = False
                        new.write(line)
                        continue
                    if line.strip() and not flag:
                        new.write(line)




add(s)









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

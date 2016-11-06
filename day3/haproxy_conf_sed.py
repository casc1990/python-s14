#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import os,json,sys,time
date = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
print (date)
a = '''{
            'backend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }'''
s = '{"backend": "abc.mage.edu","record":{"server": "100.1.7.17","weight": 20,"maxconn": 30}}'
print (type(s),s)
s1 = json.loads(s)  #json.loads 可以将字典或者列表形式的字符串转换成字典、列表(注意：字符串里的元素使用双引号"")
s2 = eval(s)     #eval 也可以将字典或者列表形式的字符串转换成字典、列表（字符串里的元素使用单双引号都可以）
s3 = eval(a)
print (s1['backend'])
print (type(s3),a)

def fetch(backend):  #查询函数
    '''
    查询backend函数
    思路：1.读文件，找打backend + 用户输入的域名的行。
         2.将backend + 用户输入的域名的下一行到下一个backend开头的行的server记录找出来，追加到新列表中
         3.返回追加的列表和打印列表中的内容
    :param backend:
    :return:
    '''
    result = []   #定义空列表，空列表用来存查到的backend sever记录
    with open('haproxy.conf', 'r') as f:  #d打开文件
        flag = False   #设置标志位（当flag值改变，说明backend的记录找完了）
        for line in f:  #循环文件
            if line.strip().startswith('backend') and line.strip() == "backend " + backend:  #查询用户输入的backend信息
                flag = True  #找到用户输入的值，修改标志位
                continue  #回到backend那行，打印server记录
            if flag and line.strip().startswith('backend'):  #下一个backend段，说明server记录已经找完了
                break  #退出循环
            if flag and line.strip():  #寻找匹配的记录
                result.append(line.strip())  #追加到列表中
        f.close()
    return result  #返回列表

def add(backend, record):  #添加函数
    '''
    逻辑：如果backend不存在:
              说明要新增，把旧文件的内容都读入到新文件，然后在最后面写入用户传入的backend和server
         如果backend存在：
           #1.server也存在：源文件不用作任何操作。
           #2.server不存在：将用户传入的server记录追加到result（result中存在着backend查到的server结果 + 要新加的结果）。
           #                循环旧文件，追加新文件（一行一行的写，到用户输入的backend的地方，设置标志位，并把result写入到backend
           #                 的server段 ）
    :param backend:
    :param record:
    :return:
    '''
    result = fetch(backend)  #调用fetch函数（查询用户的backend是否存在，把查询结果保存在result列表中）
    if not result:  # 无backend，无server
        with open('haproxy.conf', 'r', encoding='utf-8') as old, \
              open('ha.conf','w',encoding='utf-8') as new:  #打开旧文件，新建新文件
            for line in old:
                new.write(line)  #把旧文件全部写到新文件
            new.write('\n')  # 加一个空行（每个backend之间有一个空行）
            new.write('backend ' + backend + '\n')  #写backend
            new.write(' ' * 8 + record + '\n')  #写server
        old.close()

    else:  # backend存在
        if record in result:   #server也存在
            pass
        else: #server不存在
            result.append(record)  #将不存在的那条server追加到列表中（列表中有全部的server）
            with open('haproxy.conf', 'r') as old, open('ha.conf', 'w') as new:  #同时打开2个文件
                continue_flag = False  #设置标志位
                for line in old:  #循环源文件
                    if line.strip().startswith('backend') and line.strip() == "backend " + backend:
                        #找到用户所输入的backend
                        continue_flag = True  #修改标示位
                        new.write(line)  #将找到的哪行追加到文件（此时的新文件记录的是从第一行到用户输入的backend行）
                        for temp in result:  #循环保存server记录的列表文件
                            new.write(" " * 8 + temp + "\n")   #将列表中的server写入到文件中
                        continue  #跳到文件下次循环位置（此时新文件写到下一个backend行）
                    if continue_flag and line.strip().startswith('backend'): #找到下一个backend行
                        continue_flag = False  #修改标志位（此时要添加的内容全部添加完成）
                    if continue_flag:  #标志位为真，什么都不做（这个判断是为了下一个判断条件）
                        pass
                    else:
                        new.write(line)  #标志位为假，将源文件一行一行写到新文件

def add2(backend, record):   #添加函数2
    '''
    思路：一行一行读并写入到新文件，遇到用户输入的内容，打标签，并判断。
    逻辑：1.找到用户输入的backend那行，打标签
         2.找到下一个backend哪行，打标签
         3.处理要添加的backend的server记录
         4.除以上情况，一行一行的写入
    :param backend:
    :param record:
    :return:
    '''
    with open('haproxy.conf', 'r') as old, open('ha.conf', 'w') as new:  #打开新文件
        in_backend = False  #是否遇到backend段
        has_backend = False  #backend不存在
        has_record = False  #server记录是否存在
        for line in old:  #循环源文件
            #写入匹配到的backend那一行数据
            if line.strip().startswith('backend') and line.strip() == "backend " + backend:
                #判断用户输入的backend在源文件的那一行
                has_backend = True  #找到后，修改标志位
                in_backend = True  #标示backend存在
                new.write(line)  #把匹配的哪行写入到文件（写匹配的backend那行）
                continue  #回到文件上次循环位置

            #写不存在server那条记录（写到下一个backend的前一行）
            #写入下一个backend开头的那条记录
            if in_backend and line.strip().startswith('backend'): #找到下一个backend段
                if not has_record:   #如果server记录不存在
                    new.write(" " * 8 + record + '\n')
                    # 将用户输入的server记录写入到文件（也就是写入到匹配到的backend的最后面，下一个backend的前面）
                new.write(line)  #写入下一个backend那条记录
                in_backend = False  #修改标签（要处理的backend已经完成了）
                continue  #回到文件上次循环位置

            #写存在的server记录
            # 判断匹配到的backend段的server记录
            if in_backend and line.strip() == record: #如果用户输入的server已经存在了
                has_record = True  #标示server已经存在
                new.write(line)  #将存在的那行写入到文件
                continue  #回到文件上次循环位置

            #以上条件都不成立时写入所有记录
            if line.strip():  #以上条件都不成立
                new.write(line)  #将其他的行，写入到新文件

        #backend不存在
        if not has_backend:   #判断backend不存在
            new.write('backend ' + backend + '\n')  #写backend
            new.write(' ' * 8 + record + '\n')    #写server

#del():
#    pass

while True:
    choice = input('你想对配置文件做什么操作：\n'
                   '1)查询\n'
                   '2)修改\n'
                   '3)删除 \n'
                   '4)其他任意字符退出 \n'
                   '请输入你的选择的序号:')
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
        backend = input('请输入要添加的backend：')
        record = input('请输入要添加的server：')
        add(backend,record)
    if choice == '4':
        break

#修改文件

os.rename("haproxy.conf" ,"haproxy.conf.bak")  # 将源文件改名
os.rename('ha.conf', 'haproxy.conf')  # 将新文件改名为源文件
#ret = fetch("www.oldboy.org")
#print(ret)

#add('abc.mage.edu', "server 100.1.7.18 100.1.7.18 weight 20 maxconn 3000")
#add2('abc.mage.edu', "server 100.1.7.11 100.1.7.11 weight 20 maxconn 3000")

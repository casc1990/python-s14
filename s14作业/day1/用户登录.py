#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/9/24 15:14'
'''
需求：用户登录系统。提示用户输入用户名，如何用户名不输入，一直提示输入；输入有误，提示重写输入；最多
      可输入3次。三次都错误，锁定用户；锁定的用户不允许登陆
思路：2层循环，4种情况（不输入，用户已锁定，用户名不存在，用户名正确）。用户名正确，验证密码，使用标志位退出
      最外层循环。for.....else来处理循环正常执行完的操作
'''
with open('username.list','w') as f:
    f.write('zhangsan\t123\n')
    f.write('lisi\t456\n')
    f.write('wangwu\t789\n')
    f.write('zhouliu\t000\n')
    f.write('aaa\twww\n')
#with open('userdeny.list','r') as f:
#    pass
access_user = []
access_user_passwd = {}
with open('username.list') as f:
    for line in f.readlines():
        access_user.append(line.split()[0])
        access_user_passwd[line.split()[0]] = line.split()[1]
print (access_user)
print (access_user_passwd)
deny_user = open('userdeny.list').read()

while True:
    status = False
    user_name = input('please enter your username: ')
    if len(user_name) != 0 and user_name in deny_user:
        print('Locked users are not allowed to log in....')
        break
    elif len(user_name) != 0 and user_name in access_user:
        for seq in range(3):
            user_passwd = input('please enter your password: ')
            if user_passwd == access_user_passwd.get(user_name):
                print ('welcome %s login our system!' %user_name)
                status = True
                break
            else:
                print ('passwd is wrong! please try again.... ')
        else:
            print ('password enter wrong 3th,please contact your administrator')
            with open('userdeny.list','a') as f:
                f.write(user_name+'\n')
            status = True
            break
    elif len(user_name) == 0:
        continue
    else:
        print('Invalid user name,please try again:')
    if status == True:
        break



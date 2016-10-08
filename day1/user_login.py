#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
f = open('user.txt')
f2 = open('lock.txt')
deny_user = f2.read()
f2.closed
access_user = f.read()
print (type(access_user))
count = 0
#while count <3:
while True:
    username = input ('please enter your username: ')
    if username in deny_user and len(username) != 0:
        print ('Locked users are not allowed to log in....')
        break
    status = False
    if username in access_user and len(username) != 0:
        print ('ok')
        for i in range(3):
            passwd = input('please enter your passwd: ')
            if passwd in access_user and len(passwd) != 0:
                print ('welcome {name} login our system!'.format(name=username))
                status = True
                break
            else:
                print ('passwd is wrong! please try again.... ')

        else:
            status = True
            print('hehe....')
            f2 = open('lock.txt', 'a')
            f2.write('{name}\n'.format(name=username))
            f2.closed
            break
            #if passwd

    else:
            print ('no')
            print ('Invalid user name,please try again:')
            #f2 = open('lock.txt','a')
            #f2.write('{name}\n'.format(name=username))
            #f2.closed
    count += 1
    if status == True:
        break
else:
    f2 = open('lock.txt','a')
    f2.write('{name}\n'.format(name=username))
    f2.closed

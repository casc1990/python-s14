#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
_name = 'pengbo'
_passwd = '1qaz@WSX'
user = input('please enter your login name: ')
passwd = input('please enter your login passwd:  ')
if user == _name and passwd == _passwd:
    print ('Welcome {name} login our system!'.format(name=user))
else:
    print ('invalid user or passwd is wrong!')
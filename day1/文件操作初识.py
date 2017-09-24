#!/usr/bin/en'/v python
# -*- coding:utf-8 -*-
#Author:pengbo
f = open('user.txt')
access_user = f.readlines()
print (access_user)
user = input('user:')

if user in access_user:
        print ('ok')
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
oldboy_of_age = 65
while True: #只允许猜3次
    for i in range(3):
        status = False
        age = int(input('请猜猜老男孩老师的年龄: '))
        if age == oldboy_of_age:
            status = True
            print ('你真聪明，猜对了！')
            break   #猜对了，退出
        elif age > oldboy_of_age:
            print ('没那么大年纪，往小的猜...')
        else:
            print ('没那么小，往大的猜....')
    else:
        result = input('你是否还想接着猜测呢？请输入YES或者NO: ')
        if result != 'n':
            pass
        else:
            print ('程序退出...')
            break
    if status == True:
        break
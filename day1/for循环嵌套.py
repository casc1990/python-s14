#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
for i in range(0,10,2):
    print ('loop:',i)
oldboy_of_age = 65
count = 0
for i in range(3): #只允许猜3次
    age = int(input('请猜猜老男孩老师的年龄: '))
    if age == oldboy_of_age:
        print ('你真聪明，猜对了！')
        break   #猜对了，退出
    elif age > oldboy_of_age:
        print ('没那么大年纪，往小的猜...')
    else:
        print ('没那么小，往大的猜....')
    count+=1  #count+=1相当于count=count+1
    print('总共3次机会，已使用%s次机会了' %count)
#if count == 3: count==3时机会已经用完了，这时候在打印提示信息，就避免了输入正确时也打印这条信息
#在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环\
#   正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
else:  #while不成立，执行else语句，相当于if..else
    print ('3次机会已经用完了，不能猜了，程序退出..')
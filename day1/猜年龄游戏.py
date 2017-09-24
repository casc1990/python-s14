#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
oldboy_of_age = 65
age = int(input('请猜猜老男孩老师的年龄: '))
if age == oldboy_of_age:
    print ('你真聪明，猜对了！')
elif age > oldboy_of_age:
    print ('没那么大年纪，往小的猜...')
else:
    print ('没那么小，往大的猜....')

print ('hehe')
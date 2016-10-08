#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
user = input('user: ')
age = int(input('age: '))
#print (type(age))
job = input('job: ')
salary = int(input('salary: '))
sex = 'M'
info = '''------ info of {0}------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
Sex:{4}
'''.format(user,age,job,salary,sex)
print (info)
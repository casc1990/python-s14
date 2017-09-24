#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
user = input('user: ')
age = int(input('age: '))
#print (type(age))
job = input('job: ')
salary = int(input('salary: '))
info = '''------ info of {user}------
Name:{user}
Age:{age}
Job:{job}
Salary:{salary}
Sex:{sex}
''' .format(user=user,
            age=age,
            job=job,
            salary=salary,
            sex='M')
print (info)
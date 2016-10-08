#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
user = input('user: ')
age = int(input('age: '))
print (type(age))
job = input('job: ')
salary = int(input('salary: '))
info = '''------ info of %s------
Name:%s
Age:%d
Job:%s
Salary:%d
''' %(user,user,age,job,salary)
print (info)
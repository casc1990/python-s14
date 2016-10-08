#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
user = input('user: ')
age = int(input('age: '))
#print (type(age))
job = input('job: ')
salary = int(input('salary: '))
info = '''------ info of {_user}------
Name:{_user}
Age:{_age}
Job:{_job}
Salary:{_salary}
Sex:{_sex}
''' .format(_user=user,
            _age=age,
            _job=job,
            _salary=salary,
            _sex='M')
print (info)
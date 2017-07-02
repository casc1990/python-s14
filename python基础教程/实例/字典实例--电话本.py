#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/7/2 16:13'
#定义人员字典
people = {
    'Alice':{'addr':'Foo drive 23','phone':'2341'},
    'Beth':{'addr':'Bar street 42','phone':'9102'},
    'Cecil':{'addr':'Baz avenue 90','phone':'3158'}
}

people['Alice']['phone'] #访问字典的嵌套字典

#定义描述标签字典
labels = {
    'phone': 'phone number',
    'addr' : 'address'
}

#用户输入
name = input('Please Enter Your Name: ')
request = input('Do you want serach phone number(p) or address(a)? ')

#使用正确的值
key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

#使用get()提供默认值
person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not available')

#用户名是字典中的有效键才打印信息
print ("%s's %s is %s." %(name,label,result))

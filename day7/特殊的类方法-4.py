#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
from lib.test import Role
print (Role.__doc__)  #这是类的说明文档 描述信息
obj = Role()
print (obj.__module__) #lib.test  打印从那个模块导出的
print (obj.__class__) #<class 'lib.test.Role'> 打印从那个模块的那个类

class School(object):
    ''' 这个是描述学校的类'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print ('{0} is eatting'.format(self.name))
    def __call__(self, *args, **kwargs):
        print ('running call!',args,kwargs)
    def __str__(self):
        return ('<obj:%s>' %self.name)
student = School('alex',23)
student.eat() #调用一般方法
student(1,2,3,name='alex') #running call! (1, 2, 3) {'name': 'alex'}   对象后面加括号，触发执行的方法。
School('alex',23)()  #running call! () {}  类后面加括号，触发也可以执行
print (School.__dict__)  #打印类里面的所有属性，不包括实例属性
print (student.__dict__) #{'name': 'alex', 'age': 23} 打印实例中的所有属性，不包括类属性
print (student)  #<obj:alex>  打印对象时，输出__str__方法的返回值
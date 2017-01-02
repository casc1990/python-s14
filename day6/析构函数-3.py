#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

class Person(object): #创建类
    n = 100     #类变量
    name = '类中的name' #类变量
    def __init__(self, name): #构造函数
        self.name = name   #实例变量（静态属性）作用域是实例本身
    def __del__(self):  #析构函数。析构函数没有参数，程序退出、释放时执行
        print ('程序结束了。。。')
    def getName(self): #类中的方法（动态属性）
        return self.name
    def color(self, color): #类中的方法
        print ("%s is %s" % (self.name, color))

girl = Person('alex') #程序结束会自动执行__del__函数
print (girl.getName())
del girl   #   程序释放也会自动执行__del__函数
boy = Person('hehe')
print (boy.getName())
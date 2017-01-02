#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
class Person(object): #创建类
    n = 100     #类变量
    name = '类中的name' #类变量
    def __init__(self, name,age,sex,job='It',money=5000): #构造函数
        self.name = name   #实例变量（静态属性）作用域是实例本身
        self.age = age
        self.__sex = sex  #私有属性
        self.job = job
        self.__money = money  #私有属性

    def showstatus(self):
            print ('%s is job:%s' %(self.name,self.__sex))  #类内部是可以调用私有属性的
    def __admin(self):  #私有方法
        print ('form __admin里的私有方法')
    def getName(self): #类中的方法（动态属性）
        Person.__admin(self)   #类内部是可以调用私有方法的
        return self.name
    def color(self, color): #类中的方法
        print ("%s is %s" % (self.name, color))

girl = Person('alex',26,'M')
print (girl.name)
#print (girl.__sex)  #无法访问私有属性
girl.showstatus()  #alex is job:M 类内部是可以访问私有属性的

#girl.__admin()  #无法访问私有方法
girl.getName()  #输出：form __admin里的私有方法 。类内部可以访问私有方法


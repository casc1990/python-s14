#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

class Person(object): #创建类
    n = 100     #类变量
    name = '类中的name' #类变量
    lst = []
    def __init__(self, name): #构造函数
        self.name = name   #实例变量（静态属性）作用域是实例本身
    def getName(self): #类中的方法（动态属性）
        return self.name
    def color(self, color): #类中的方法
        print ("%s is %s" % (self.name, color))

girl = Person('wangguniang') #实例化
name = girl.getName() #调用类方法
print ("the person's name is: ", name)
girl.color("white") #调用类方法

print ("------")
print (girl.name) #实例的属性

#访问类变量
print (Person.n)  #100 类访问类变量
print (girl.n)  #100 实例访问类变量
print (Person.name) #类中的name
print (girl.name)  #wangguniang 实例变量的优先级高于类变量
print ('实例可以访问类变量，如果变量即在实例中又在类中，实例变量的优先级高于类变量')
print ('类变量的作用:存储共用的属性，节省开销')
#修改类变量（修改就是添加实例变量）
print (girl.n) #100
girl.n = 200 #其实并不是修改了类变量，而是给实例又添加了n这个变量。（添加实例变量）
print (girl.n) #200  新实例变量的值
print (Person.n) #100  类变量的值并没有改变
girl.lst.append('form girl') #向类变量中追加值
print (girl.lst) #因为类变量和实例变量引用的是同一个内存地址，所有都会修改
print (Person.lst)


#修改实例变量
print (girl.name)  #wangguniang 修改之前（访问实例变量 ）
girl.name = 'zhangsan'   #修改实例变量（属性）
print (girl.name)  #zhangsan 修改之后
#添加实例变量
girl.age = 26  #添加实例变量（属性）
print (girl.age)
#删除实例变量
print (girl.age)  #26
del girl.age   #删除实例变量
#print (girl.age) #再次查看，报错了，实例变量被删除了


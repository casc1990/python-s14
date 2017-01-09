#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
class StaticMethod(object):
    name = '我是类变量'   #类变量
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.id = 5
    @staticmethod    #静态方法
    def foo(self):
        print ("%s is static method foo()." % self.name)
        print (self.id)
    @staticmethod  #静态方法
    def foo2():
        print("This is static method foo().")
    def eat(self):
        print("%s is eating" % self.name)

class ClassMethod(object):
    name = '我是类变量'   #类变量
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    @classmethod   #类方法
    def bar(self):
        print ("%s is static method foo()." %self.name)
        #print (self.age)
    @classmethod   #类方法
    def foo2(self):
        print("This is static method foo().")
    def eat(self):
        print("%s is eating" % self.name)

if __name__ == "__main__":
    static_foo = StaticMethod('alex',25,'M')
    static_foo.eat()  #alex is eating 调用普通实例方法（正常访问）
    #static_foo.foo() #保错 调用静态方法（静态方法不能访问实例变量和类变量）
    static_foo.foo(static_foo)  #静态方法只是属于类，和类没什么关系，就是一个普通函数
    static_foo.foo2() #This is static method foo(). 静态方法就是一个普通函数，因为没有参数，所以可以直接调用
    print ('静态方法只是属于类，和类没什么关系，就是一个普通函数.所以静态方法不能访问实例变量和类变量')
    class_foo = ClassMethod('alex',25,'M')
    class_foo.bar() #我是类变量 is static method foo(). 类方法可以访问类变量,不能访问实例变量
    class_foo.foo2()  #This is static method foo(). 类方法要加参数（def foo2(cls):）
    class_foo.eat() #alex is eating 调用普通实例方法（正常访问）
    print ('类方法可以访问类变量,不能访问实例变量')
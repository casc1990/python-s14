#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#类是由type生成

class foo(object):
    def func(self):
        print ('hello alex')
F = foo()
print (type(foo)) #输出为：type (类的tyep为type)

def __init__(self,name,age):
    self.name = name
    self.age = age
def talk(self):
    print ('%s is talking' %self.name)
Foo = type('Foo',(object,),{'__init__':__init__,
                           'talking':talk})   #object,表示是新式类，字典里是类对应的方法
f = Foo('alex',22)  #实例化
print (type(Foo)) #类型为type，同class类型一致
print (f.name) #输出为:alex （访问类属性）
f.talking()  #alex is talking （调用类方法）--talking对应着talk函数

#总结: 类是由 type 类实例化产生

#__new__()
class MyType(type):
    def __init__(self, child_cls, bases=None, dict=None):
        print("--MyType init---", child_cls, bases, dict)
        # super(MyType, self).__init__(child_cls, bases, dict)

    # def __new__(cls, *args, **kwargs):
    #     print("in mytype new:",cls,args,kwargs)
    #     type.__new__(cls)
    def __call__(self, *args, **kwargs):
        print("in mytype call:", self, args, kwargs)
        obj = self.__new__(self, args, kwargs)

        self.__init__(obj, *args, **kwargs)


class Foo(object, metaclass=MyType):  # in python3
    # __metaclass__ = MyType #in python2

    def __init__(self, name):
        self.name = name
        print("Foo ---init__")

    def __new__(cls, *args, **kwargs):  #重构new方法（new是用来创建实例的）--可以对类实例化之前做些定制
        #__init__方法是通过__new__创建的（先执行new方法，new调用了init方法去实例化对象）
        print("Foo --new--") #为new添加额外的功能（实例化之前会被执行）
        return object.__new__(cls)  #继承父类的new方法，cls指Foo(类本身)

    def __call__(self, *args, **kwargs):
        print("Foo --call--", args, kwargs)


obj = Foo("Alex")
#总结：__new__方法是用来创建实例的，__new__方法是首先被执行的，然后__new__调用__init__进行对象的实例化
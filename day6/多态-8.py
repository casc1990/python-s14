#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
def length(x):
    print ("The length of", repr(x), "is", len(x))

length("how are you")
length([1,2,3])
length({"lang":"python","book":"itdiffer.com"})
print ('length函数就是多态的表现形式。不关心你传递的内容，都将它转换成python对应的类型和统计的长度')

#多态的例子
class Animal(object):
    def __init__(self, name=""):
        self.name = name
    def talk(self):
        pass
class Cat(Animal):
    def talk(self):
        print ("Meow!")
class Dog(Animal):
    def talk(self):
        print ("Woof!")
a = Animal()
a.talk()
c = Cat("Missy")
c.talk()
d = Dog("Rocky")
d.talk()
print ('代码中有 Cat 和 Dog 两个类，都继承了类 Animal，它们都有 talk() 方法，输入不同的动物名称，会得出相应的结果。')
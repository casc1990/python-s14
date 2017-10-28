#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
# class People: 旧式类
class People(object): #新式类
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []
        print("in the People ")
    def eat(self):
        print("%s is eating..." % self.name)
    def talk(self):
        print("%s is talking..." % self.name)
    def sleep(self):
        print("%s is sleeping..." % self.name)

class Relation(object): #社交类
    #def __init__(self,n1,n2):  #2个父类的参数必须保证一样多，不然继承就不知道要传递多少个参数
    #    print("in the Relation")
    def make_friends(self,obj): #接受一个参数(w1)
        print("%s is making friends with %s" % (self.name,obj.name)) #obj.name=w1.name,self.name=People类里的self.name
        self.friends.append(obj) #将对象追加到列表中（内存空间）
class Man(Relation,People):  #多重继承
    def piao(self):  #子类的方法
        print("%s is piaoing ..... 20s....done." % self.name)
    def sleep(self):  #重写了sleep方法
        People.sleep(self)  #执行父类的sleep方法
        print("man is sleeping ")

class Woman(People,Relation): #多重继承
    def get_birth(self):  #子类的方法
        print("%s is born a baby...." % self.name)

m1 = Man("NiuHanYang",22) #实例化
w1 = Woman("ChenRonghua",26) #实例化
m1.make_friends(w1) #输出为：NiuHanYang is making friends with ChenRonghua
#                   调用Man的make_friends方法，发现Man类并没有make_friends方法，于是找Man继承的父类，从继承的
#                   父类中，从左到右依次查找；查找Relation父类，找到了make_friends方法，并把子类Woman作为参数传入了，
#                   obj.name=w1.name,self.name=People类里的self.name
w1.name = "陈四炮"  #修改了w1的name属性
print(m1.friends[0].name) #陈四炮 查询列表中实例对象的name属性（属性已经被修改）


#####例子2 #######
class K1(object):
    def foo(self):
        print ("K1-foo")
class K2(object):
    def foo(self):
        print ("K2-foo")
    def bar(self):
        print ("K2-bar")
class J1(K1, K2):
    pass
class J2(K1, K2):
    def bar(self):
        print ("J2-bar")
class C(J1, J2):
    pass
if __name__ == "__main__":
    print (C.__mro__) #__mro__查看类继承的顺序。
    #输出为：<class '__main__.C'>, <class '__main__.J1'>, <class '__main__.J2'>, <class '__main__.K1'>, <class '__main__.K2'>, <class 'object'>
m = C()
m.foo()
m.bar()
#代码中的 print C.__mro__ 是要打印出类的继承顺序。从上面清晰看出来了。如果要执行 foo() 方法，首先看 J1，没有，看 J2，还没有，看 J1 里面的 K1，有了，
# 即 C==>J1==>J2==>K1；bar() 也是按照这个顺序，在 J2中就找到了一个。
print ('新式类多重继承属性和方法搜索的顺序称之为“广度优先”；'
       '旧式类多重继承属性和方法搜索的顺序称之为“深度优先”')
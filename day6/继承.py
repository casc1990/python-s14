#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
class People(object):  #定义类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print ('%s is eating....' %self.name)
    def sleep(self):
        print ('%s is sleeping....' %self.name)
    def work(self):
        print ('%s is working....'% self.name)

class Man(People):  #Man类继承People类
    #重构__init__方法。重构时实例化会执行子类的__init__方法，所以父类的name,age参数也必须重构的初始化函数里。
    #money参数为要新加入的参数。
    def __init__(self,name,age,money):  #name,age是父类中参数；money是新加的属性
        #People.__init__(self,name,age)  #执行父类的__init__方法，导入self.name = name和self.age = age等
        super(Man,self).__init__(name,age) #super(子类,self).父类的某方法：执行父类中的某方法。等价于People.__init__(self,name,age)
        self.money = money  #新加参数money属性
        print ('%s 初始化金额为：%d' %(self.name,self.money))
    def play_game(self):  #Man类中的方法
        print ('Man %s is playing.... ' % self.name)

class Woman(People): #Woman类继承People类
    def go_shopping(self): #Woman类中的方法
        print ('Woman %s is go shopping....')
    def sleep(self):  #重构sleep方法。子类中的方法优先于父类中的方法
        People.sleep(self)   #执行父类中的sleep方法
        print ('%s is Woman' %self.name)  #为sleep方法添加新的功能

boy = Man('alex',26,10)   #实例化子类时，需要传入父类中的初始化变量def __init__(self,name,age):
boy.eat() #调用父类中的方法
boy.play_game() #调用子类中的方法
print (boy.money)  #访问新添加的属性

girl = Woman('王美女',32)  #实例化子类
girl.work()  #调用父类中的方法
girl.sleep()  #调用子类中的方法，子类中的sleep方法会执行父类中的sleep方法



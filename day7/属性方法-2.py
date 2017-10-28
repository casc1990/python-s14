#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
print ('属性方法的作用就是通过 @property 把一个方法变成一个静态属性')
class Dog(object):
    def __init__(self,name):
        self.name = name
        self.food = None
    @property   #属性方法
    def eat(self):
        print ('%s is eating %s....' %(self.name,self.food))
    @eat.setter  #属性方法赋值
    def eat(self,foo):
        print ('set to food' ,foo)
        self.food = foo
    @eat.deleter  #属性方法删除（del XX）
    def eat(self):
        del self.food
        print ('删完了')

d2 = Dog('alex')
#d2.eat() #报错，因为@property已经把这个方法变成了一个静态的属性了，调用是不能加()
d2.eat  #alex is eating None....  正常执行
d2.eat = '饺子' #set to food 饺子。执行@eat.setter函数
#               @eat.setter给属性方法赋值（‘饺子’赋值给了food变量）
d2.eat #alex is eating 饺子....。 （food的值被修改了）
del d2.eat  #删完了 。执行@eat.deleter
#           @eat.deleter删除属性方法（foo属性被删除了）
#d2.eat #在此调用就报错了。因为food属性被删了



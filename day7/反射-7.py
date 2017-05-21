#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
'''
def jiao(self):
    print ('%s is jiao..wang..wang..'%self.name)
class Dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print ('%s is eatting %s' %(self.name,food))

d = Dog('alex')  #实例化
choice = input('你想让狗干嘛>> :').strip()  #接受用户的选择
if hasattr(d,choice): #判断用户输入的字符串的方法名是否在实例(d)中
    #delattr(d,choice) 删除对象(d)里对应的字符串(choice)名称的方法或属性
    #getattr(d,choice)('狗粮') --同下
    func = getattr(d,choice) #获取实例(d)中字符串方法(choice)的内存地址
    func('狗粮') #执行方法
else:
    setattr(d,choice,jiao) #向对象(d)中添加一个字符串(choice)方法，方法对应的函数是jiao
    d.talk(d)  #执行设置的方法（因为关联的函数有一个self参数，所有需要把实例自己传进去）

#总结：
#hasattr(obj,name_str): 判断一个对象(obj)里是否有对应的字符串(name_str)名称的方法或属性
#getattr(obj,name_str): 根据字符串(name_str)去获取对象(obj)里对应的方法或者属性
#setattr(obj,name_str,func): 向对象(obj)中添加一个字符串(name_str)方法，方法对应的函数或者属性是func
#delattr(obj,name_str): 删除对象(obj)里对应的字符串(name_str)名称的方法或属性
'''
class A(object):
    def __getattr__(self, item): #访问item这个属性或者方法，它不存在的时候，此方法被调用
        print ('you use getattr')
    def __setattr__(self, key, value): #如果要给 key 赋值，就调用这个方法
        print ('you use setattr')
        self.__dict__[key] = value #给实例设置属性
a = A()
print (a.x) #输出为：you use getattr（获取方法或者属性：调用__getattr__）
a.x = 7  #输出为：you use setattr （设置方法或者属性：调用__setattr__）
print (a.x) #输出为7

class B(object):
    def __getattribute__(self, item): #无论 item方法或者属性是否存在，都要被调用
        print ('you use getattribute')
        return object.__getattribute__(self,item)
b = B()
print (b.__dict__) # 输出为：{} --说明被实例化的对象没有属性或者方法
#b.y  #输出为：you use getattribute --调用了__getattribute__方法，但是此时对象还没有y属性的，所有还是会报错的
b.y =8 #给对象设置了y属性
b.y #再次调用__getattribute__方法
print (b.y)  #打印属性

#总结
#__setattr__(self,name,value) ：如果要给 name 赋值，就调用这个方法
#__getattr__(self,name) ：如果name被访问，同时它不存在的时候(既不是类属性或者方法，又不是实例属性或方法)，此方法被调用。
#__getattribute__(self,name) ：当 name 被访问时自动被调用（注意：这个仅能用于新式类）,无论 name 是否存在，都要被调用。
#__delattr__(self,name) ：如果要删除 name，这个方法就被调用。


#@property和property
"""study __getattr__ and __setattr__"""  #描述信息（__doc__方法调用）
class  Rectangle(object):
    '''the width and length of Rectangle'''
    def __init__(self):
        self.width = 0
        self.length = 0
    def getsize(self):
        return self.width,self.length
    def setsize(self,size):
        self.width,self.length = size
    size = property(getsize,setsize)
    #property函数可以把类的方法变成属性，并根据对象的相应操作，执行不同的属性（方法），比如执行r.size就会调用getsize
if __name__ == "__main__":
    r = Rectangle()
    r.width = 3 #修改实例化属性
    r.length = 4
    print (r.size) #输出为：(3, 4) --调用getsize方法
    r.size = 30,40  #调用setsize方法
    print (r.width,r.length) #访问实例属性
#上面的类Rectangle等同于如下
class Rectangle1(object):
    def __init__(self):
        self.width = 0
        self.length = 0
    @property
    def getsize(self):
        return self.width,self.length
    @getsize.setter
    def getsize(self,size):
        self.width, self.length = size
d = Rectangle1()
d.width = 3 #修改实例化属性
d.length = 4
print (d.getsize) #输出为：(3, 4) --调用getsize方法
d.getsize = 30,40  #调用setsize方法
print (d.width,d.length) #访问实例属性

#总结：
#property(getsize,setsize): property函数可以把类的方法变成属性，并根据对象的相应操作，执行不同的属性（方法）
#@property: 将类的方法变成属性（self.setter,self.deltter）



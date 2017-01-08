#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
print ('要了解封装，离不开“私有化”，就是将类或者函数中的某些属性限制在某个区域之内，外部无法调用。')
class ProtectMe(object):
    def __init__(self):
        self.me = "qiwsir"
        self.__name = "kivi"

    def __python(self):
        print ("I love Python.")

    def code(self):
        print ("Which language do you like?")
        self.__python()
        print (self.__name)
if __name__ == "__main__":
    p = ProtectMe()
    print (p.me)  #qiwsir
    #print (p.__name)  #私有属性，实例是不能访问的
    #p.__python()  #私有方法，实例也是不能访问的
    p.code()  #内内部是可以访问私有方法和属性的


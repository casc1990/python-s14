#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#getitem、setitem、delitem可以让类支持索引操作（增、删、改、查）。

class Foo(object):
    def __init__(self):
        self.data = {}
    def __getitem__(self, key):
        return self.data.get(key)
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        print('%s is removeing!' % self.data.get(key))
        del self.data[key]
        print ('remove over!')

k1 = Foo()
k1['name'] = 'alex'  #调用__setitem__方法
print (k1['name'])  #调用__getitem__方法
del k1['name'] #调用__delitem__方法

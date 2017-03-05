#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

#__import__()模块实现 --内置方法（不推荐）
lib = __import__('lib.test')  #导入字符串模块，导入到lib这层（import lib）
print (lib)  #输出：<module 'lib' from 'D:\\python-project\\s14\\day7\\lib\\__init__.py'>
test = lib.test  #导入test
instance = test.Role() #实例化。
#print (test.name) #输出为：alex

#importlib模块实现  --第三方模块（推荐）
import importlib
test = importlib.import_module('lib.test')  #导入字符串模块,导入到test这层（import lib.test）
print (test) #输出：<module 'lib.test' from 'D:\\python-project\\s14\\day7\\lib\\test.py'>
instance = test.Role() #实例化。
print (instance.name)  #输出为：alex
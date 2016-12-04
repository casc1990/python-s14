#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

print ('''
模块定义： 用来从逻辑上组织python代码（通过变量、函数、类），本质是.py结尾的python文件
    功能： 实现某一种功能(文件名：test.py, 模块名：test)
''')

#import module  导入sys.path环境变量路径里的.py文件
import custom_module   #导入模块
print (custom_module.name)   #打印模块变量
custom_module.say_hello('zhangsan')  #调用模块函数
print('导入模块方法：import 模块名')
print('导入多个模块方法：import 模块名1,模块名2...')
from custom_module import *  #不建议这样使用
print (name)
say_hello('lisi')
print('导入某个模块的某个方法：from 模块名 import 方法名 ')
print('导入某个模块的所有方法：from 模块名 import * ')
import os as ww
from sys import path as www
print (ww.path)
print (www)
print('导入某个模块并给方法重命名：from 模块名 import 方法名 as 方法别名 ')
#导入模块的本质是把模块里的python文件解释一遍。
# import 模块名：把模块里的python文件全部解释一遍。使用模块名.方法调用
# from 模块名 import 方法：只是把模块里的某个方法解释一遍。使用方法名直接调用

import package_test  # 执行python_test目录里的__init__.py文件
                    #   输出：python package from package_test目录
# 包(Python Package): 用来从逻辑上组织模块的。本质就是一个目录(必须带有一个__init__.py文件)
#导入包的本质就是执行该包下的__init__.py文件




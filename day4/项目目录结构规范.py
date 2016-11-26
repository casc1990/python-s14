#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
print ('''
设计一个层次清晰的目录结构的优点：
    1.可读性高: 不熟悉这个项目的代码的人，一眼就能看懂目录结构，知道程序启动脚本是哪个，
                测试目录在哪儿，配置文件在哪儿等等。从而非常快速的了解这个项目。
    2.可维护性高: 定义好组织规则后，维护者就能很明确地知道，新增的哪个文件和代码应该放在什么目录之下。
                 这个好处是，随着时间的推移，代码/配置的规模增加，项目结构不会混乱，仍然能够组织良好。
例子：
    Foo/    项目名称
    |-- bin/   项目可执行命令目录
    |   |-- foo     可执行命令
    |
    |-- core/     主程序目录
    |   |-- tests/   测试代码目录
    |   |   |-- __init__.py 测试程序文件
    |   |   |-- test_main.py
    |   |
    |   |-- __init__.py  主程序文件
    |   |-- main.py  主程序入口文件
    |
    |-- conf/   配置文件目录
    |   |-- setting.conf  配置文件
    |   |-- test.conf
    |
    |-- docs/   文档目录
    |   |-- conf.py  项目文档
    |   |-- abc.rst
    |
    |-- setup.py  安装、部署、打包的脚本
    |-- requirements.txt  存放软件依赖的外部Python包列表
    |-- README  项目说明文件



'''
)
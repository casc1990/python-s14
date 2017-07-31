#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/7/31 22:19'

def init(data):
    '初始化数据结构函数，记录用户名字的第一个字，中间的字，最后的字'
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data,label,name):
    '查询数据结构中有没有关于用户名字（姓、中间字、名）的关键字'
    return data[label].get(name)

def store(data,full_name):
    '接收用户的查询请求（在哪个数据结构中查询姓名相关信息），函数的入口，接收用户传入的值'
    names = full_name.split() #将用户的名字转换为列表（姓名分成3等分）
    if len(names) ==2: names.insert(1,'')  #如何用户的名字是2个字符，中间添加空格
    labels = 'first','middle','last'  #定于数据结构中key的值
    for label,name in zip(labels,names):  #将名字标签和名字的各个值对应上并循环
        people = lookup(data,label,name)  #调用查询函数，查询是否有匹配到的标签的名字的值
        if people:
            people.append(full_name)  #如果有，打印出这些值并附加上自己（查到的结果+自己本身）
        else:
            data[label][name] = full_name  #如果无数据，将自己的全名追加进数据结构

MyNames = {} #定义字典
init(MyNames) #初始化数据结构
store(MyNames,'Magnus LieHetland')  #存储数据
print (lookup(MyNames,'first','Magnus')) #查询数据结构，在first中匹配'Magnus'

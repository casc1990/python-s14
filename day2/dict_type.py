#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#字典是无序的，由key,value组成，不支持切片
info = {
    'stu001':'zhangsan',
    'stu002':'lisi',
    'stu003':'wangwu',
    'stu004':'alex'
}                  #新建字典（可以分行写）
info2 = {'stu001':'zhangsan','stu002':'lisi','stu003':'wangwu','stu004':'alex'}
info3={'www':'ddd','name':'aa','age':22,'name':'bb','name':'cc'}  #如果字典中key重复，以最后那个key为准，遍历时key是唯一的
print (len(info3))  #len方法只会统计不重复key的数量
print (info3)
print (info)
info['stu005'] = 'old-boy'   #增加或者修改（没有就增加，有就修改）
info['stu006'] = 'jack'
#del info['stu001']  # del函数删除
info.pop('stu002')  #pop方法删除
#info.popitem()      #随机删除
info['stu001'] = '007'   #修改
print (info['stu003'])   #查询（查到直接返回，没查到，报错）
print (info.get('stu003'))  #查询。（查到直接返回，没查到，返回None）
print (info.clear())   #清空字典
dict_list = {1:'a',2:'b',3:['hello','world']}
dict_list2 = dict_list.copy()   #浅copy （只copy一层，嵌套的数据修改会影响copy的结果。深copy请导入copy模块）
dict_list[3][1] = 'xiaoming'
print (dict_list2,dict_list)

print (info)



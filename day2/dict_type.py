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
#print (info.clear())   #清空字典
dict_list = {1:'a',2:'b',3:['hello','world']}
dict_list2 = dict_list.copy()   #浅copy （只copy一层，嵌套的数据修改会影响copy的结果。深copy请导入copy模块）
dict_list[3][1] = 'xiaoming'
print (dict_list2,dict_list)
lst = ['a','b','c']
dict_list3 = dict.fromkeys(lst,'hello')  #用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
dict_list4 = dict.fromkeys(range(3),'hello') #输入为：{0: 'hello', 1: 'hello', 2: 'hello'}
dict_list5 = dict.fromkeys(range(3)) #输出为：{0: None, 1: None, 2: None}
print (info.items())    #以元祖的形式返回字典的所有键、值数组,输出如下：
#dict_items([('stu001', '007'), ('stu005', 'old-boy'), ('stu004', 'alex'), ('stu003', 'wangwu'), ('stu006', 'jack')])
print (info.keys())   #返回所有的键
print (info.values())  #返回所有的值
print (info.setdefault('ID',5))   #查找键值，如果键不存在于字典中，将会自动插入键并将值设为默认值。
print (info.setdefault('stu001',5))  #键如果存在，不会修改。
dict6 = {'age':20,'users':'zhangsan','addr':'山东省'}
info4 = {'sex':'M'}
dict6.update(info4)   #把指定字典的键值更新到当前字典中
print (dict6.update(info4))  #更新无输出，所以将更新的结果赋值或打印都是现实None
print (dict6)

china = {
    '陕西':{
         '商洛':['丹凤','商南','山阳','柞水'],
         '安康':['白河','甸阳','镇平','平利','紫阳']
           },
    '河北':{
         '张家口':['桥西','桥东','宣化'],
         '保定':['新市','北市']
           },
    '北京':['丰台','朝阳','昌平']

    }
print (china['陕西']['商洛'][0])  #字典的多级嵌套

for i in info:   #字典循环姿势一（推荐使用）
    print (i,info[i])

for i,j in info.items():
    print (i,j)   #字典循环姿势一(效率低，不建议使用)


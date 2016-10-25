#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#在子程序中定义的变量称为局部变量；在程序的一开始定义的变量称为全局变量。
#全局变量作用域是整个程序；局部变量作用域是定义该变量的子程序。
#局部变量可以修改可变序列的值（列表、字典、集合），不能修改不可变序列的值（字符串、元祖、整数）
school = 'Oldboy'
lst1 = [1,2,3,4]
def change_name(name):
    global school    #global将school改为了全局变量（不推荐使用）
    school = 'mage'  #修改了其值（不可变序列）
    print ('before_change',name)   #这个name是用户传递的参数
    name = 'hello'     #局部变量（name这个变量只作用于这个函数）
    print ('after change',name)   #这个name是被子程序修改过了，不影响外界
    print (school)     #函数内部可以访问全局变量
    lst1[0] = 'a'  #修改全局变量列表的值（可变序列）
    print (lst1)

name = 'zhangsan'      #全局变量name的值(这个值不会受函数内的子程序影响)
change_name('zhangsan')
print (name)  #取全局变量name的值，输入为：zhangsan
print (school)    #函数中将school提升为全局变量，有被函数修改，所以值变了，输入为：mage
print (lst1)     #全局变量的值被修改，因为是可变序列，不可变序列就不会改变




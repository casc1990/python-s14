#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#集合是一个无序的、不重复的数据组合。主要作用如下：
#去重：把一个列表变成集合，就自动去重了
#关系测试：测试两组数据之前的交集、差集、并集等关系
name = set('hello')   #将字符串转换为集合，重复的元素就被过滤掉
name2 = set([1,2,3,4,5]) #将列表转换为集合，重复的元素就被过滤掉
name3 = set((1,2))     #将元祖转换为集合，重复的元素就被过滤掉
name4 = set({1:'a'})   #将字典转换为集合。转换后只有key为集合元素
name5 = {'d','d','s'}   #创建一个set集合，重复的元素就被过滤掉
name6 = set()   #新建空集合
print (name5.add('w'))  #增加集合元素
print (name5.add('s'))  #重复的元素加不进集合
print (name4.clear())   #清空集合所有元素
li = name5.copy()   #浅复制，复制name3到li


s = {33,11,22}
t = {33,44,22}
a = t | s   #求t和s的并集，结果为：33, 22, 11, 44（相加去重）
print ('并集',t.union(s))  #求t和s的并集，同t | s 结果一致
print ('并集',s.union(t))  #并集的结果是一致的
a = t & s   #求t和s的交集，结果为：33, 22（两者共同拥有的）
print ('交集',t.intersection(s)) #求t和s的交集，同t & s结果一致
a = t - s   #求t和s的差集，结果为：44 （t中有，s中没有）
print (t.difference(s))  #同a = t - s，求差集
a = t ^ s   #求t和s的对称差集，结果为：11, 44 （s没有的+t中也没有的）
print ('对称差集',t.symmetric_difference(s)) #求t和s的对称差集,同t ^ s结果一致
a1 = {'a','b','c','d'}
a2 = {'a','c'}
a3 = {'a','w'}
a4 = ('z','x')
print ('是否有交集',a2.isdisjoint(a4))  #判断没有交集，返回True,否则,返回False
print ('子集',a2.issubset(a1))   #判断a2是否是a1的子集.(子集的元素，父集中都要有，才会为真)
print (a3.issubset(a1))       #判断a3是否是a1的子集。输入为：False
print ('父集',a1.issuperset(a2))  #判断a1是否是a2的父集。输入为：True



s.discard(22)  #删除集合中的某个元素。原子操作，不能将结果复制给变量
s.discard(55)  #如果该元素不在集合中，则什么也不做
s.remove(11)   #删除集合中的某个元素.
#s.remove(55)   #如果该元素不在集合中，会报错。
t.pop()    #随机移除集合中的一个元素，并返回该元素
t.update(s)   #把指定集合更新到当前集合中
t.update([88,99])  #把指定类型数据更新到当前集合中
print (88 in t)    #判断某元素是否在集合中。not in 是否不在集合中
print (t)

print (a)

#print (name,name2,name3,name4,name5)
#print (type(name))

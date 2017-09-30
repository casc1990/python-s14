#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

name = ['zhangsan','lisi','wangwu','pb','liuhaoran','huyuedong','zhoushan']
print (name)
''''
#列表切片
print (name[0:])  #打印所有。类似 print(name)
print (name[-1])  #打印最后一个元素
print (name[2],name[4])
print (name[2:5])  #打印第3个元素到第5个元素（顾前不顾尾）
print (name[0:-1:2])  #从开头到结尾，步进为2
print (name[:])     #开头到结尾
print (name[-3:])  #打印倒数3个元素
print (name[-4:-1]) #打印倒数第四到倒数第二（反取也是从左到右，不是从后往前取值）
'''
#增
'''
name.append('taolong')    #向列表末尾追加
name.insert(4,'tangyuan')  #在指定位置插入（第5个元素前插入）
print(name)
'''
#删
''''
#name.pop()         #删除最后一个
#name.pop(2)        #删除下标为2的元素（位置删）
#name.append('lisi')
#name.remove('lisi')   #删除lisi这个元素。只删除匹配到的第一个元素（名称删）
#del name[2]       #删除第3个元素
#del name[2:5]     #删除第3到第5个元素
name.clear()      #清除列表中所以元素
print (name)
'''
#改
'''
#name[3] = 'chenzheng'   #修改第4个元素的值
#name[3:5] = ['a','b']   #修改第4个元素和第5个元素的值
#name[3:] = []           #将列表第4个元素到结尾置空
print (name)
'''
#查
'''
#print (name[3])      #查看第4个元素的值
#print (name.index('pb'))   #查找值为pb的元素位置
#print (name[name.index('pb')])
'''
#其他方法
'''
#name.append('lisi')
#print (name.count('lisi'))  #统计lisi这个元素出现过几次
name.sort()   #按assl排序 （顺序为：特殊字符、数字、大写字母、小写字母）
print (name)
name.reverse()  #列表元素从右到左翻转
print (name)
name2 = [1,2,3,4]
name.extend(name2)  #合并列表
print (name,name2)

print (ord('W'))  #查看元素所对应的assl编号
print (chr(119))   #根据编号查找assl元素
'''
#深复制和浅复制
#name2 = name    #name和name2指向了同一个id，只要其中一个改变，都会改变。
#name.append('chenzheng')

#name2 = name[:]     #切片复制id改变，name和name2修改互不影响
#print (id(name),id(name2))
#name.append('chenzheng')

#name.insert(2,['chenzheng'])
#name2 = name[:]
#name.pop()
#name[2][0] = 'CHENZHENG'    #切片复制嵌套数据类型时，只是复制了嵌套类型数据的物理源数据，源数据改变，都会影响。
#print (id(name),id(name2))
#print (name)
#print (name2)
'''
name.insert(2,['chenzheng','hehe'])
name2 = name.copy()   #copy复制，只能复制到1层，嵌套的列表改变，复制的列表也会改变
name.pop()            #id不同，相互修改不影响
name[2][0] = 'CHENZHENG'  #list里嵌套的列表改变，复制的列表也会改变
name2[2][1] = 'HEHE'
print (id(name),id(name2))
print (name)
print (name2)

import copy
name.insert(2,['chenzheng','hehe'])
name2 = copy.deepcopy(name)    #copy.deepcopy方法可以实现深复制（克隆）
#name2 = copy.copy(name)        #copy.copy方法和name.copy是等价的
name[2][0] = 'CHENZHENG'
print (name)
print (name2)        #因为是深复制，所以值不会改变

#列表循环
for i in name:
    print (i)
'''








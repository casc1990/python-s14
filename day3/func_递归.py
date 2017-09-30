#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#如果一个函数在内部调用自身，这个函数就是递归函数。
#递归特性:
#1. 必须有一个明确的结束条件
#2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
#3. 递归效率不高
def calc(n):
    print (n)   #每次打印下自己
    if int(n/2) >0:  #正整数（退出条件）
        return calc(int(n/2))  #返回calc函数的执行结果，但是calc函数还未执行完，所以一直调用自身
#    print ('----->',n)  #因为条件不成立，就不会到return，就不会再递归了。打印了最后一个元素
calc(20)

#下面的函数和上面是一致的
def calc1(n):
    print (n)  #打印每次n的值
    if int(n/2) == 0:  #如果商等于0，返回n（n小于等于1，条件成立）
        return n
    return calc1(int(n/2)) #其他情况，一直递归（重新调用自己）
print ('分割线'.center(50,'-'))
calc1(20)


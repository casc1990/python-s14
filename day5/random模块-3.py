#!/usr/bin/env python
#-*- coding:utf-8 -*-
import random
print (random.random()) #随机生成0<x>1的随机浮点数  0.9538333785778547
print (random.uniform(1,3)) #指定范围的随机浮点数（1<x>3） 1.7602452961984527
print (random.randint(1,3))  #指定范围的随机整数（1<=x>=3 顾头顾尾） 3
print (random.randrange(1,3))  #指定范围的随机整数，和range用法一致（1<=x>3 顾头不顾尾） 1
print (random.choice([1,2,3,4]))  #random.choice(序列)  从序列中随机选出一个元素   2
print (random.sample([1,2,3,4,5],3)) #random.sample(序列,随机选择的元素数) 从指定的序列中随机选出指定的元素数  [1, 5, 2]

#洗牌（将序列数据随机化）
a = ['apple', 'pear', 'peach', 'orange', 'lemon']
print (a)  #['apple', 'pear', 'peach', 'orange', 'lemon']
random.shuffle(a)   #源处修改，没有返回值
print (a) #['lemon', 'orange', 'peach', 'pear', 'apple']

#随机验证码
print (ord('A'))
print (ord('Z'))

lst = []
for i in range(6):
    i = random.randint(0,6)
    if i == 2 or i == 4:
        temp = random.randrange(0, 10)
        lst.append(str(temp))
    else:
        temp = random.randint(65, 90)
        lst.append(chr(temp))
str_random = ''.join(lst)
print (str_random)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import os
goods_list = [
    ['iphone',5388],
    ['bike',500],
    ['watch',1389],
    ['mac pro',12000]
]   #商品列表
shopping_list = []  #用户的购物车
while True:   #用户要输入正确的工资
    salary = input('请输入你的工资: ')
    if salary.isdigit():
        salary = int(salary)
        break
    else:
        print ('参数无效，请输入整数格式的工资金额。如20000：')
while True:
    for index,item in enumerate(goods_list):    #打印商品列表和下标
        print (str(index)+': ',item)
    print ('查看购物车，请输入S或者select...')
    user_choice = input('请输入你想购买的商品编号: ')   #接受用户的输入
    print (type(user_choice))
    if user_choice.isdigit():     #判断用户输入的是否是数字
        user_choice = int(user_choice)
        if user_choice < len(goods_list) and user_choice >= 0:  #判断用户输入的编号是否在商品列表下标中
            goods_item = goods_list[user_choice]   #用户选择要购买的商品
            if goods_item[1] < salary:      #买的起
                salary -= goods_item[1]     #剩余的钱
                shopping_list.append(goods_item)  #追加到购物车
                print ('商品\033[31;1m%s\033[0m已经加入购物车了,你的余额剩余\033[41;1m%s\033[0m' % (goods_item,salary))
            else:  #买不起
                print ('你剩余的钱不够买商品了，请充值后再购买。。')
        else:   #用户输入的编号不在商品列表下标中
            print('参数无效，无此编号商品。。')
    elif user_choice == 'q' or user_choice == 'quit':   #输入q 退出
        print ('''------- shopping list ----------''')  #打印商品列表
        for i in shopping_list:
            print (i)
        print ('你的余额剩余%s' % salary)
        break
    elif user_choice == 'S' or user_choice == 'select':  #查看购物车
        print('''------- shopping list ----------''')
        for i in shopping_list:
            print(i)
    else:  #用户输入的不是数字、q、S，提示参数无效
        print ('参数无效，无此编号商品。。')


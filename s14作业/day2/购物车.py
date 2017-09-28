#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/9/26 22:53'
'''
需求:
启动程序后，让用户输入工资，然后打印商品列表
允许用户根据商品编号购买商品
用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
可随时退出，退出时，打印已购买商品和余额
'''
goods_list = [
    ['apple','5000'],
    ['iphone8','7500'],
    ['watch','1300'],
    ['bike','500'],
    ['mac pro','12000']
]
shopping_list = []  #用户的购物车
salary = input('请输入你的工资：')
balance = int(salary)
while True:
    for seq,line in enumerate(goods_list):
        print (seq,":",' $'.join(line))
    print ('查看购物车，请输入S或者select...')
    choice_num = input('请选择你想买的商品编号: ')
    if choice_num.isdigit():   #判断用户选择的序号是否只由数字组成
        choice_num = int(choice_num)
        if choice_num not in list(range(len(goods_list))):
            print ('没有此编号的商品，请重新选择商品编号')
            continue
        else:
            if balance > int(goods_list[choice_num][1]):
                balance -= int(goods_list[choice_num][1])
                shopping_list.append(goods_list[choice_num])
                print ('你购买了%s,花费了%s,你的余额为:%s' %(goods_list[choice_num][0],goods_list[choice_num][1],balance))
            else:
                print('你剩余的钱不够买商品了，请充值后再购买。。')
    elif choice_num == 'q' or choice_num == 'quit':
        print('''------- shopping list ----------''')
        for i in shopping_list:
            print(i, )
        print('你的余额剩余%s' % balance)
        break
    elif choice_num == 'S' or choice_num == 'select':
        print('''------- shopping list ----------''')
        for i in shopping_list:
            print (i,)
    else:
        print ('你的输入不合法，只能输入商品的序号:')
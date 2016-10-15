#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

#sys.exit()可以退出程序。也可以在程序中设置标志位，通过标志位的值退出程序
#pass 函数是一个占位符
import sys
china = {
    '陕西':{
         '商洛':['丹凤','商南','山阳','柞水'],
         '安康':['白河','甸阳','镇平','平利','紫阳'],
           },
    '河北':{
         '张家口':['桥西','桥东','宣化'],
         '保定':['新市','北市']
           },
    '北京':{
         '丰台':['六里桥','东高地','三营门'],
         '朝阳':['国贸','亚运村','大望路','双井']
          }
    }
print (china['北京']['丰台'])

while True:
    for i in china:
        print (i)     #打印省
    choice = input('1>>>>请选择你想查询的省份: ')
    if choice in china:

        while True:
            for i2 in china[choice]:
                print (i2)    #打印市
            choice2 = input('\t2>>>>请选择你想查询的市级区域: ')
            if  choice2 in china[choice]:
                for i3 in china[choice][choice2]:
                    print (i3)
                choice3 = input('\t\t最后一层了，按b返回上层: ')
                if choice3 == 'b':
                    continue
                elif choice3 == 'q':
                    sys.exit()     #退出程序
            elif choice2 == 'b':
                break
            elif choice2 == 'q':
                sys.exit()   #退出程序


    elif choice == 'b':
        break
    elif choice == 'b':
        sys.exit()  # 退出程序





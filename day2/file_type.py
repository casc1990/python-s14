#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

#2.7打开文件可以用open、file，但是在3.0中只能用open
f = open('yesterday',encoding='utf-8')  #因为默认window使用gbk字符编码，所有要使用utf-8，否则会报错
                                        #文件打开在内存中，将打开的文件复制给一个变量，记录文件句柄。
f2 = open('yesterday','r',encoding='utf-8')  #以只读的方式打开（默认就是以只读模式）
'''
#print (f.readline())
data1 = f.read()    #文件读到行尾，指针就留在哪儿，在读就为空了
data2 = f.read()    #已经到行尾了，所有data2就等于空了
print (data1)
print ('---------'.center(50),data2)  # 打印为空
#f3 = open('yesterday2','w',encoding='utf-8')   #以写的方式打开文件（文件不存在等于新建；文件存在等于覆盖）
f4 = open('yesterday2','a',encoding='utf-8')   #以追加的方式打开文件,追加方式也不能读（文件指针跳到文件最后一行，从最后一行开始写文件）
#f5 = open('yesterday3','a',encoding='utf-8')  #以追加的方式打开文件，文件不存在也会新建文件
f4.write('\nwhen i was young i listen to the radio\n')
f4.write('加油吧！少年。')
f4.closed    #关闭文件

print (f2.readline())      #每次读一行（列表形式）
print (f2.readlines())     #读所以行（列表形式）

for i in range(5):
    print (f2.readline().strip())   #打印前5行（strip（）脱去空格和换行）

#文件的第10行打印别的内容
for index,values in enumerate(f2.readlines()):  #enumerate生成下标和数据
    if index == 9:
        print ('华丽的分界线'.center(50,'*'))   #center格式化输出
        continue
    print (values.strip())               #第10行打印别的内容
'''
for index,values in enumerate(f2.readlines()):
    if index < 4:
        pass
    elif index >= 4 and index < 10:
        print (values.strip())











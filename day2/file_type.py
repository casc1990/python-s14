#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

#r  只读模式（默认模式）
#w  写模式（不能读）
#a  追加  （从结尾开始写, 如果文件不存在，会新建）
#r+  读+追加（读写模式，写的内容会追加到行尾）
#w+  写读    （覆盖原文件，写的内容会追加到行尾） ---基本用不到
#a+  追加读  （读写模式，写的内容会追加到行尾）
#rb  二进制读模式打开  （读二进制文件时使用此模式，比如网络编程会用到）
#wb  二进制写模式打开  （写二进制文件时使用此方法）
#ab  二进制追加模式打开 （即读即写二进制文件使用此方法）
#rb+、wb+、ab+  二进制读写模式
#2.7打开文件可以用open、file，但是在3.0中只能用open

f = open('yesterday3','w',encoding='utf-8')  #因为默认window使用gbk字符编码，所有要使用utf-8，否则会报错
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
#print ('读行:',f2.readline())   #readline每次读一行
for i in range(5):
    print (f2.readline())  #读文件前5行

for i in range(10):
    if i < 5:
        f2.readline()
    else:
        print (f2.readline())  #读文件5到10行

f5 = open('yesterday',encoding='utf-8')
print (f5.readlines())   #读文件的所有行（列表形式）
count =1
for i in f.readline():
    print (i)
    count +=1
    if count == 9:
        print ('-------分界线--------')

f4.closed    #文件是否关闭

print (f2.readline())      #每次读一行（列表形式）
print (f2.readlines())     #读所以行，适合读小文件，读大文件有可能会内存溢出，大文件使用for循环读（列表形式）

for i in range(5):
    print (f2.readline().strip())   #打印前5行（strip（）脱去空格和换行）

#文件的第10行打印别的内容
for index,values in enumerate(f2.readlines()):  #enumerate生成下标和数据
    if index == 9:
        print ('华丽的分界线'.center(50,'*'))   #center格式化输出
        continue
    print (values.strip())               #第10行打印别的内容

# 打印文件5行到10行之间的内容
for index,values in enumerate(f2.readlines()):
    if index < 4:
        pass
    elif index >= 4 and index < 10:   #读5-10行内容
        print (values.strip())

for i in f2:      #文件也是序列类型，支持循环 （支持大文件读取）
    print (i)

#文件的第10行打印别的内容 --高效版
count = 0
for i in f2:
    if count == 9:
        print ('华丽的分界线'.center(50,'*'))
        count += 1
        continue
    else:
        print (i)
        count += 1

print (f2.readline())
print (f2.tell())   #查询读到文件的那个位置
print (f2.seek(0))  #将光标指针移动到指定位置
print (f2.seek(6))  #将文件指针移动到第6个字符处。
print (f2.readline())  #将会打印这行的从第7个元素到行尾内容
print (f2.read(4))   #读文件前5个字符
print (f2.encoding)   #打印文件的字符编码
print (f2.closed)    #文件是否关闭
#f2.close()       #关闭文件
'''
f.write('hello 1\n')
f.flush()    #立即刷新到硬盘（默认数据不会立即写硬盘的）
print (f2.isatty())  #是否是终端文件
print (f2.writable())   #文件是否可读
print (f2.readable())    #文件是否可写
print (f2.name)      #显示文件名
print (f2.seekable())   #文件指针是否可移动的（终端文件就不能seek操作）
f5 = open('yesterday2','r+',encoding='utf-8')
f6 = open('yesterday3','wb')  #以二进制模式打开
f6.write('hello,world'.encode('utf-8'))  #写二进制文件（直接写字符串是不允许的，encode转二进制）
#f5.truncate()    #截断文件所有内容，(文件就被置空了)
f5.truncate(8)   #截取文件8个字符，对文件截取操作时，文件打开的模式必须是r+,a等（保留前10个）














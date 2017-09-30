#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
name = 'my \tname is Mr Peng'
name2 = 'hello! {name},your age is {year}'
msg = '我爱北京天安门'
print (name.capitalize())   #第一个单词的首字母大写
print (name.title())       #所有单词的首字母大写
print (name.casefold())    #将字符串所有字符转换成小写
print (name.center(50,'*'))  #字符串总共要占50字符，不够用修饰符左右填充,无修饰符，使用空格填充
print (name.ljust(30,'*'))        #字符串总共要占30字符，不够用修饰符向后填充,无修饰符，使用空格填充
print (name.rjust(30,'*'))        #字符串总共要占30字符，不够用修饰符向前填充,无修饰符，使用空格填充
print (len(name))
print (name.count('e'))    #统计e在字符中出现多少次
print (msg.encode(encoding='utf-8'))  #把utf-8编码为bytes，encode时指定原本的字符编码。不指定python3默认以utf-8为原始编码
print (msg.encode(encoding='utf-8').decode(encoding='utf-8'))  #把bytes解码为utf-8编码
print (name.endswith('ng'))   #判断字符串是否已指定字符结尾
print (name.startswith('My')) #判断字符串是否已指定字符开头
print (name)
print (name.expandtabs(tabsize=30))  #将字符串中的tab转换成30个空格
print (name.find('m',1,7))   #查找指定字符串的下标。从左到右查找，找到就停止。可以指定查找范围
print (name.index('m'))      #同find用法一致
print ('abcdsddsd'.rfind('d'))        #同find，只是返回的是最后面匹配的下标
print ('abcdsddsd'.rindex('d'))       #同index，只是返回的是最后面匹配的下标
print (name2.format(name='xiaoming',year='26'))   #字符串格式化输出。等同于%辅助
print (name2.format_map({'name':'xiaoming','year':'26'}))  #format_map接受字典格式的赋值
print ('a你w'.isalnum())    #判断字符串是否只包含了字母或者数字，无其他特殊字符
print ('a1'.isalpha())      #判断字符串是否只由字母组成
print ('22A'.isdecimal())   #检查字符串是否只包含十进制字符
print ('23'.isdigit())     #检测字符串是否只由数字组成
print ('aB'.islower())     #检测字符串是否只由小写字母组成
print ('YYaY'.lower())     #将字符串所有字符都转换为小写字母
print ('BB'.isupper())     #检测字符串是否只由大写字母组成
print (name.swapcase())    #大小写互换
print ('yy'.upper())      #将字符串所有字符都转换为大写字母
print ('ss'.isidentifier())  #检测字符串是否是字母开头
print ('22'.isnumeric())    #检测字符串是否只由数字组成。
print ('2w\t'.isprintable())  #判断字符串中所有字符是否都属于可见字符
print (' '.isspace())    #检测字符串是否为空格,是空格，结果为真
print (''.join(['a','b','c','d']))  #将列表转换为字符串
print ('+'.join(['1','2','3']))     #将列表转换为字符串并以+为连接符
print ('  YY  ')
print ('  YY  '.lstrip())        #去除字符串左边开头的空格
print ('  YY  '.rstrip())        #去除字符串右边结尾的空格
print ('  YY  '.strip())         #去除字符串左右两边结尾的空格
passwd = str.maketrans('abcdefghijkl','1!2@3#4$5%6^') #maktrans是一个静态方法，用于生成一个对照表，以供 translate 使用。且2个参数长度相等
print ('pengbo'.translate(passwd))   #查找指定字符串的对照表，如果有，就显示，没有，显示源字符串。早期用于生产密码。
print ('pengbo p'.replace('p','P',1))  #字符串替换。默认全部替换，可以指定替换几次
print (name.split())        #字符串分割，默认是空格。分割后的字符串是列表形式。
print ('1+2+3+4'.split('+'))  #指定以+为分割符。分割后的字符串是列表形式。
print (name.zfill(30))   #用 '0' 填充字符串，并返回指定宽度的字符串。

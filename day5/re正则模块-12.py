#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import re
print('''
'.'  :默认匹配除\n之外的任意一个字符，若指定flag DOTALL, 则匹配任意字符，包括换行
'^'  :匹配字符开头，若指定flags MULTILINE, 这种也可以匹配上(r"^a", "\nabc\neee", flags=re.MULTILINE)
'$'  :匹配字符结尾，或e.search("foo$", "bfoo\nsdfsf", flags=re.MULTILINE).group()也可以
'*'  :匹配 * 号前的字符0次或多次，re.findall("ab*", "cabb3abcbbac") 结果为['abb', 'ab', 'a']
'+'  :匹配前一个字符1次或多次，re.findall("ab+", "ab+cd+abb+bba") 结果['ab', 'abb']
'?'  :匹配前一个字符1次或0次
'{m}'  :匹配前一个字符m次
'{n,m}'  :匹配前一个字符n到m次，re.findall("ab{1,3}", "abb abc abbcbbb") 结果 ['abb', 'ab', 'abb']
'|'  :匹配 | 左或 | 右的字符，re.search("abc|ABC", "ABCBabcCD").group() 结果 'ABC'
'(...)'  :分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c

'\A'  :只从字符开头匹配，re.search("\Aabc", "alexabc")是匹配不到的
'\Z'  :匹配字符结尾，同$
'\d'  :匹配数字0 - 9
'\D'  :匹配非数字
'\w'  :匹配[A - Za - z0 - 9]
'\W'  :匹配非[A - Za - z0 - 9]
's'   :匹配空白字符、\t、\n、\r, re.search("\s+", "ab\tc1\n3").group() 结果 '\t'

'(?P<name>...)'  :分组匹配
re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})", "371481199306143242").groupdict("city")
#  结果 {'province': '3714', 'city': '81', 'birthday': '1993'}

最常用的匹配语法
re.match 从头开始匹配 .group()打印匹配到的内容
re.search 匹配包含 。group()打印匹配到的内容
re.findall 把所有匹配到的字符放到以列表中的元素返回
re.splitall 以匹配到的字符当做列表分隔符
re.sub      匹配字符并替换
''')

#match(pattern, string, flags=0)  （匹配开头，匹配一次）
#从起始位置开始根据模型去字符串中匹配指定内容，匹配单个。如果匹配到，返回匹配到的对象，没有匹配到，返回None
a = re.match('\d+','123home')  #匹配1个或者多个数字开头的数字部分
print (a,a.group())  #<_sre.SRE_Match object; span=(0, 3), match='123'>如果匹配到会返回对象。 123：匹配的内容
print (re.match('\d+','4home').group())  #结果为 4 。
print (re.match('\d+','h234ome')) #没有匹配到任何内容，返回None。match是从开头开始匹配，开头不符合就不会再匹配了
print (re.match('\d.+abc','456sA ababceds').group()) #结果 (456sA ababc). .+匹配任意字符任意长度

#search(pattern, string, flags=0)  从开头往后依次匹配，匹配到了就不会再往下匹配。（匹配一次）
# 根据模型去字符串中匹配指定内容，匹配单个
print (re.search('\d+','ho23d45ss56').group())  #匹配结果 （23）
print (re.search('\d[a-z]{2}[a|A]$','345eds5dha').group()) #匹配结果 (5dha) 匹配数字小写字符出现2次a或者A结尾的连续集合
s = "123abc456"
print (re.search("[0-9]*[a-z]*[0-9]*",s).group()) #匹配结果（123abc456）匹配数字出现0次或者多次小写字符出现0次或者多次在跟着数字出现0次或者多次的连续集合
print (re.search('(abc){1,2}[0-9]?\W$','sdfSfabc1#').group())  #匹配结果（abc1#） 匹配abc出现1次到2次数字出现0次或者1次，特殊字符结尾的集合

#group() 和 groups()
#group()返回匹配到的一个或者多个子组。如果是一个参数，那么结果就是一个字符串，如果是多个参数，那么结果就是一个元组形式。
# group的默认值为0，将返回字符串格式的所有的匹配值。如果group1的值是[1…99]范围之内的,那么 将匹配对应括号组的字符串。
# 如果组号是负的或者比pattern中定义的组号大，那么将抛出IndexError异常
x = "123abc456"
print (re.search("([0-9]*)([a-z]*)([0-9]*)", x).group())  #匹配结果（123abc456） group()=group(0) 字符串形式，匹配所以
print (re.search("([0-9]*)([a-z]*)([0-9]*)", x).group(0)) #匹配结果（123abc456） group()=group(0) 字符串形式，匹配所以
print (re.search("([0-9]*)([a-z]*)([0-9]*)", x).group(1))  #匹配结果（123） group(1)匹配([0-9]*)部分
print (re.search("([0-9]*)([a-z]*)([0-9]*)", x).group(2))  #匹配结果（abc） group(2)匹配([a-z]*)部分
print (re.search("([0-9]*)([a-z]*)([0-9]*)", x).group(1,3)) #匹配结果（('123', '456')）匹配([0-9]*)和([0-9]*)部分
print (re.search('\s+','1dds \r\n  ').group())  #匹配\t、\n、\r

#返回匹配一个包含所有子组的元组。Default是用来设置没有匹配到组的默认值的。Default默认是"None”,
print (re.search("([0-9]*)([a-z]*)([0-9]*)", x).groups())  #匹配结果('123', 'abc', '456')  元祖形式，匹配所有

#findall(pattern, string, flags=0) 从开头往后依次全部匹配 匹配所有’ 无.group()方法
print (re.findall('\d+', 'fa123uu888asf')) #匹配结果（['123', '888']） 列表形式 匹配所有
print (re.findall('[a-zA-Z]\d?','a1B2c3d55e6ff7')) #匹配结果（['a1', 'B2', 'c3', 'd5', 'e6', 'f', 'f7']）

#sub(pattern, repl, string, count=0, flags=0)相当于str.replace  用于替换匹配的字符串
content = "123abc456"
print (re.sub('\d+', 'sb', content)) #匹配的结果（sbabcsb） 把匹配到的内容替换为指定的字符串（数字部分替换为sb）
new_content = re.sub('\d+', 'sb', content, 1)  #从头往后匹配，只替换1次
print (new_content)

#split(pattern, string, maxsplit=0, flags=0)相当于str.split   根据指定匹配进行切割，返回列表形式
content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
new_content = re.split('\*', content)  #指定*为分隔符
new_content1 = re.split('\*', content, 1)  #指定*为分割符，分割1次
print (new_content)   #["'1 - 2 ", ' ((60-30+1', '(9-2', '5/3+7/3', '99/4', '2998+10', '568/14))-(-4', '3)/(16-3', "2) )'"]
print (new_content1) #["'1 - 2 ", " ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"]
print (re.split("[a-zA-Z]+","0A3b9z")) #['0', '3', '9', ''] 以大小写字符为分割符。

#"(?P<name>...)" 分组匹配,返回匹配到的所有命名子组的字典。Key是name值，value是匹配到的值。
print (re.search("(?P<省>[0-9]{2})(?P<市>[0-9]{2})(?P<县>[0-9]{2})(?P<生日>[0-9]{8})","612523199005274317").groupdict("city"))
#结果{'县': '23', '生日': '19900527', '省': '61', '市': '25'}

#常用匹配汇总
'''
IP：
^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$
手机号：
^1[3|4|5|8][0-9]\d{8}$
'''
print (re.search('^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$','172.19.29.32').group())
print (re.search('^1[3|4|5|8][0-9]\d{8}$','13345678910').group())






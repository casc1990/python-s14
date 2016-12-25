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
print (re.search("[0-9]*[a-z]*[0-9]*",s).group())



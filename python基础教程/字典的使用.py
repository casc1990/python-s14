#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/7/2 15:39'
#创建
phonebook = {'Alice': '2341','Beth': '9102',\
             'Cecil': '3258','qinghua': '1234'}
items = [('name','liming'),('age',25)]
d = dict(items) # 输入： {'age': 25, 'name': 'liming'}  被转换的必须是key，value形式的
s = dict(name= 'linux',age= 23) #输出 {'age': 23, 'name': 'linux'} 通过关键字参数创建

print (len(phonebook)) #获取长度
print (phonebook['Alice']) #访问
phonebook['abc'] = '123' #修改或者创建
del phonebook['abc']  #删除
print ('Alice' in phonebook) # 成员关系判断

#格式化字典
print ("Cecil's phone number is %(Cecil)s" % phonebook) #输出 Cecil's phone number is 3258
print ("Cecil's phone number is %s" % phonebook['Cecil']) #等同于上面
#字典的格式化时，字典的键(一定要使用圆括号括起来(%(Cecil)s)，注意修饰符(s)不能少)

d = {}
d['age'] = 42
d['name'] = 'Gumby'
d.clear() # 无返回值 （清空所有的键值对）

x = {'username' : 'admin','machines': ['foo','bar','baz']}
y = x
y['username'] = 'mlh'
print (x,y) #x,y的输出都为 {'username': 'mlh', 'machines': ['foo', 'bar', 'baz']} 引用同一个变量，值相等
z = x.copy()
z['username'] = 'mlt'
print (z) #输出 {'username': 'mlt', 'machines': ['foo', 'bar', 'baz']}  副本改变，不会影响原始的值
print (x) #输出 {'username': 'mlh', 'machines': ['foo', 'bar', 'baz']}
z['machines'].remove('foo')
print (z) #输出 {'username': 'mlt', 'machines': ['bar', 'baz']} #原始字串也被改变（copy是浅复制）
print (x) #输出 {'username': 'mlh', 'machines': ['bar', 'baz']}
# a = b 表示一个变量2个标签，a改变b也改变，a重新赋值，a就不等于b；
# a = b.copy() 字典浅复制，副本第一层值(a)改变，原始字典(b) 不影响；
#如果是嵌套字典， 副本改变深层次的值，原始字典(b)也会跟着改变；

from copy import deepcopy
d = {'name':['Alfred','Bertrand']}
c = d.copy()
dc = deepcopy(d)
c['name'].append('Clive')
print (d,c)  #输出 {'name': ['Alfred', 'Bertrand', 'Clive']}
print (dc) #输出 {'name': ['Alfred', 'Bertrand']}
#deepcopy是深复制，复制了数据结构

print (dict.fromkeys(['name','age'])) #输出 {'name': None, 'age': None}
print (dict.fromkeys(['name','age'],('unknown'))) #输出 {'age': 'unknown', 'name': 'unknown'} 指定value
#fromkeys使用指定的键建立新字典，并可以指定key的value

rb = {'name':'liming','age':24}
#print (rb['www']) #如果key不存在会报错
print (rb.get('www')) #如果key不存在不会报错，返回None
print (rb.get('www','N/A')) #输出 N/A （指定找不到的返回值）
#访问key建议使用get,还可以指定找不到的返回值

d = {}
#print (d.has_key('name'))  #输出 False （注意：python3没有这个函数）

d = {'title': 'python web site','url':'http://www.python.org','spam':0}
print (d.items()) #输出：dict_items([('spam', 0), ('url', 'http://www.python.org'), ('title', 'python web site')])
#items方法将字典所有的项以列表方式返回，列表中每一项都表示为(key,value)的形式

d = {'name':'liming','age':24}
print (d.keys()) #输出 dict_keys(['age', 'name']) （所有key）
print (d.values()) #输出 dict_values([24, 'liming']) （所有values）

d = {'a':'A','b':'B','c':'C'}
d.pop('a') #删除指定的键值对，（指定key）
d['c'] = 'C'
d.popitem() #随机删除键值对
#pop(key) ：删除指定kv；popitem()：随机删除kv

d = {}
print (d.setdefault('name','N/A')) #输出 N/A
print (d) #输出 {'name': 'N/A'}
d['name'] = 'liming'
print (d.setdefault('name','N/A')) #输出 liming
#setdefault('key','values'): 如果键存在，正常返回；不存在设置；setdefault类似于get，不同点get不更新字典

d = {'name':'liming','age':23}
x = {'sex':'M','name':'lina'}
d.update(x)
print (d) # 输出 {'sex': 'M', 'name': 'lina', 'age': 23}
#update方法合并旧字典到新字典，新字典相同的key会被旧字典覆盖






#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
a = [
    {'gather_facts': False,
     'hosts': 'web',
     'tasks': [{'name': 'Copy file to client',
                'copy': 'src=/root/rs.sh dest=/root/ccc'}],
     'user': 'root',
     'remote_user': 'root',
     'name': 'create user',
     'vars': [{'user': 'xiaorui'}]}
]
import yaml
s = yaml.load(open('test.yaml'))  #load方法会把yaml文件内容格式化成列表形式。列表里面的元素被封装成字典格式
print (s[0]['hosts']) #访问host属性
print (s[0]['tasks'][0]['copy'])  #访问copy属性
s1 = yaml.load(open('test2.yaml'))
print (s1)   #{'soft': {'php': 5.3, 'mysql': 5.2, 'apache': 2.2}, 'host': {'ip00': '192.168.1.1', 'ip01': {'one': '192.168.1.2', 'two': '192.168.1.254'}}}
print (s1['soft'])
print (s1['soft']['mysql'])

#生成yaml文件
data={'host': {'ip01': {'two': '192.168.1.254', 'one': '192.168.1.2'}, 'ip00': '192.168.1.1'}, 'soft': {'apache': 2.2, 'php': 5.3, 'mysql': 5.2}}
f=open('test2.yaml','w')
yaml.dump(data,f)
f.close()

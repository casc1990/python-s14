#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#用于生成和修改常见配置文档，当前模块的名称在 python 3.x 版本中变更为 configparser
import configparser    #在python2.7中时ConfigParser
#生成如下配置文件：
'''
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no
'''
config = configparser.ConfigParser()  #先要生成一个对象
config["DEFAULT"] = {'ServerAliveInterval': '45',  #[DEFAULT]相当于key,里面的配置相当于这个key的value
                     'Compression': 'yes',    #Compression = yes
                     'CompressionLevel': '9'}  #CompressionLevel = 9

config['bitbucket.org'] = {}   #[bitbucket.org]
config['bitbucket.org']['User'] = 'hg'  #User = hg

config['topsecret.server.com'] = {}  #[topsecret.server.com]
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'  # Port = 50022
topsecret['ForwardX11'] = 'no'  # ForwardX11 = no
config['DEFAULT']['ForwardX11'] = 'yes'  #添加了[DEFAULT]标签的 ForwardX11 = yes

config['mysqld'] = {
                    'port' : 6379,
                    'ip': '127.0.0.1'}
with open('mysql.conf', 'w') as configfile:  #新建mysql.conf文件
    config.write(configfile)  #将生成的对象写入到文件

#读取配置文件数据
config2 = configparser.ConfigParser()
config2.read('mysql.conf') #读取这个文件
print (config2.sections())  #读出所有的标签项,[DEFAULT]因为是关键字，所有读不到。 [bitbucket.org]，[topsecret.server.com]，[mysqld]
print (config2.defaults()) #读出[DEFAULT]配置的所有配置信息。
print('bitbucket.org' in config2)  #判断bitbucket.org是否在对象中
print (config2['bitbucket.org']['User'])  #读取['bitbucket.org']标签下user配置项的值
print (config2['DEFAULT']['Compression'])
print (config2['topsecret.server.com']['ForwardX11'])
for key in config2['DEFAULT']:  #循环配置
    print(key)

#增删改查
config3 = configparser.ConfigParser()
config3.read('mysql.conf') #读取这个文件
options = config3.options('topsecret.server.com')   #打印出[topsecret.server.com]和[DEFAULT]标签配置的key
print ('----',options)
item_list = config3.items('topsecret.server.com')
print (item_list)  #打印出[topsecret.server.com]和[DEFAULT]标签配置的key、value对
print (config3.get('topsecret.server.com','port'))  #获取[topsecret.server.com]标签的port对应的值
# sec = config.remove_section('group1')  #删除[group1]标签的所有配置
# config.write(open('i.cfg', "w"))  #写回到文件

# sec = config.has_section('wupeiqi')
# sec = config.add_section('wupeiqi')
# config.write(open('i.cfg', "w"))


# config.set('group2','k1',11111)   #在[group2]标签里在添加一条配置
# config.write(open('i.cfg', "w"))

# config.remove_option('group2','age')  #在[group2]标签里在移除一条配置
# config.write(open('i.cfg', "w"))

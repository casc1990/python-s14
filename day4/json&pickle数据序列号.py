#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

import json,pickle
#json:所有语言都通用，只能处理简单的数据类型（例如，函数就处理不了）
#pickle：只能用于python语言中的数据类型中，处理任何数据类型
dic = {'key1':'value1','key2':'value2'}
f = open('test.txt','w')
#f.write(dic)    #文件存储的都是字符串或者二进制。其他数据类型是存储不进去的
f.write(str(dic))
f.close()
# 字符串类型的python数据类型是不能通过list,dict,set等方法转换成相应的python数据类型的。通过序列化可以实现
#序列化：将python数据类型(字符串、二进制)转换成字符串。（python数据类型----字符串）
#反序列化： 将字符串类型的数据转换成相应的python数据类型。（字符串----python数据类型）
#注意：反序列化时最好使用“”(双引号)

dic1 = str({'key1':'value1','key2':'value2'})
print (dic1,type(dic1))
#a = dict(dic1)  # 字符串类型的python数据类型是不能通过list,dict,set等方法转换成相应的python数据类型的
#print (a.get('key1')) #所以 "{'key1':'value1','key2':'value2'}" 就不能使用dict函数，只能使用序列化
a1 = eval(dic1)    #eval函数是可以（eval将字符串转换成表达式）
print (a1.get('key1'))  #可以正常输出结果

dic2 = {'key1':'value1','key2':'value2'}
#json.dumps() 序列化
dict_to_str = json.dumps(dic2)  #将dict序列化成字符串（"{'key2': 'value2', 'key1': 'value1'}"）
#json.dumps() 序列化到文件
with open('test.txt','w') as f:
    dict_to_json_file = json.dump(dic2,f)  #json.dump序列化到文件
print (dict_to_str,type(dict_to_str))
#json.loads()  反序列化
str_to_dict = json.loads(dict_to_str)  #将字符串反序列化成字典。{'key1':'value1','key2':'value2'}
#json.load()  从文件反序列化
with open('test.txt','r') as f:
    file_json_to_dict = json.load(f)  #从文件反序列化
    print ('form file:',file_json_to_dict,type(file_json_to_dict))
print (str_to_dict.get('key1'),type(str_to_dict))


#pickel() 序列化 && 反序列化
dic3 = {'key1':'value1','key2':'value2'}
#pickle.dumps() 序列化  (bytes类型)
pickle_to_srt = pickle.dumps(dic3) #pickle.dumps序列化后的数据类型是bytes类型
#pickle.dump() 反序列化到文件
with open('test.txt','wb') as f:
    dict_to_pickle_file = pickle.dump(dic2,f)  #pickle.dump序列化到文件
print (pickle_to_srt,type(pickle_to_srt))  #b'\x80\x03}q\x00(X\x04\x00\x00\x00key2q\x01X\x06\x00\x00\x00value2q\x02X\
#                    x04\x00\x00\x00key1q\x03X\x06\x00\x00\x00value1q\x04u.' <class 'bytes'>
#pickle.loads() 反序列化
str_to_pickle = pickle.loads(pickle_to_srt)  #反序列化
#pickle.load() 从文件反序列化
with open('test.txt','rb') as f:
    file_pickle_to_dict = pickle.load(f)  #从文件反序列化
    print ('form file:',file_pickle_to_dict,type(file_pickle_to_dict))
print (str_to_pickle['key2'],type(str_to_pickle))



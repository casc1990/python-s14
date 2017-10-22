#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import hashlib
#用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
m = hashlib.md5()  #生成MD5对象
m.update(b"Hello")  #输入要加密的数据(输入的数据一定要是bytes类型)
m.update(b"It's me")  #可以调用update()多次更新要加密的数据
m.hexdigest()
print(m.hexdigest())  #打印加密的md5值(16进制格式hash)
m.update(b"It's been a long time since last time we ...")
print (m.hexdigest())
print(len(m.hexdigest()))
'''
def digest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of binary data. """
    pass

def hexdigest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of hexadecimal digits. """
    pass

'''
import hashlib

# ######## md5 ########

print ('-------------')
hash = hashlib.md5()
hash.update(b"admin")
print(hash.hexdigest())

# ######## sha1 ########

hash1 = hashlib.sha1()
hash1.update(b"admin")
print(hash1.hexdigest())

# ######## sha256 ########

hash2 = hashlib.sha256()
hash2.update(b"admin")
print(hash2.hexdigest())

# ######## sha384 ########

hash3 = hashlib.sha384()
hash3.update(b"admin")
print(hash3.hexdigest())

# ######## sha512 ########

hash4 = hashlib.sha512()
hash4.update(b"admin")
print(hash4.hexdigest())

#python 还有一个 hmac 模块，它内部对我们创建 key 和 内容 再进行处理然后再加密
import hmac
h = hmac.new('wueiqi'.encode('utf-8'))
h.update('hellowo'.encode('utf-8'))
print (h.hexdigest())











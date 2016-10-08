#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
msg = '我爱北京天安门'
print (msg)
msg2 = msg.encode(encoding='utf-8')  #把utf-8编码为bytes，encode时指定原本的字符编码。不指定python3默认以utf-8未原始编码
print (msg2)
msg3 = msg2.decode(encoding='utf-8') #把bytes解码为utf-8编码
print (msg3)

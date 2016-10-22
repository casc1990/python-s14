#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

#python2.7 默认使用ascii编码 python3是unicode
#ascii是最早的编码集，不支持中文，占1字节
#gb2312是最早的中文字符集，到最后发展到gbk（支持最多的中文）
#unicode 俗称“万国码” ，包括了全世界的各地字符集，支持中文。占2个字节
#utf-8是可变长的字符编码，可以认为是unicode的扩展，支持中文。英文占1个字节，中文占3个字节
#encoding() --编码     decoding()  --解码
#因为unicode是万国码，它可以编码utf-8和gbk、gb2312等等，所有不同编码的转换都要经过unicode重新编码
import sys
str = '你好，世界！'
print (sys.getdefaultencoding())   #查看默认的系统编码，（python2.7是ascii，python3是unicode
#unicode到gbk转换
str_to_gbk = str.encode('gbk')  #因为python3中默认就是unicode，所有可以直接将unicode编码为gbk或者gb2132
print (type(str_to_gbk))        #在转换中，不仅转换了编码吗集，转换后的字符类型都会变成bytes类型
print ('gbk type:',str_to_gbk)
#unicode到utf-8的转换
str_to_utf8 = str.encode('utf-8')  #直接将unicode编码为gbk或者utf-8
print (type(str_to_utf8))    #查看转换后的类型
print ('utf-8 type:',str_to_utf8)
#utf-8到gbk的转换
utf8 = str.encode('utf-8')
utf8_to_gbk = utf8.decode('utf-8').encode('gbk')
print ('gbk type:',utf8_to_gbk)

#gbk到utf-8
gbk = str.encode('gbk')
gbk_to_utf8 = gbk.decode('gbk').encode('utf-8')
print ('utf-8 type:',gbk_to_utf8)


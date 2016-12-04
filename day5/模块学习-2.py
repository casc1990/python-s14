#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#模块分类：标准库（os,sys）
#         开源模块
#         自定义模块

#标准库：
#time、datetime模块
#Python中，通常有这几种方式来表示时间：1）时间戳 2）格式化的时间字符串 3）元组（struct_time）共九个元素。
import time,_datetime
print (time.time())  #时间戳形式(1480861904.4984093 1970年开始算)
print (time.localtime())  #元祖形式(time.struct_time(tm_year=2016, tm_mon=12, tm_mday=4,\
#          tm_hour=22, tm_min=31, tm_sec=44, tm_wday=6, tm_yday=339, tm_isdst=0))
#           解释：tm_wday=6:一周中的第几天，取值范围（0-6,0表示第一天）；tm_yday=339: 一年中的第几天
day = time.localtime()
print (day.tm_year,day.tm_mon)  #2016,12 访问元祖形式的时间序列
print (time.timezone)  #本地时间和utc时间的差值（-28800 本地时间比标准时间早8小时）
print (time.daylight)  #查看是否使用夏令时时间（0:不使用；1：使用）
time.sleep(3)  #睡眠3s
print (time.gmtime())  #把时间戳转换为utc标准时间的元祖形式（当前时间-8）
print (time.localtime())  #把时间戳转换为本地时间的元祖形式（utc+8）
print (time.gmtime(1450853161))  #time.gmtime(second) 可以指定具体的时间戳
print (time.localtime(1450853161))  #time.localtime(second)  可以指定具体的时间戳
x = time.localtime()
print (time.mktime(x))  #time.mktime(tuple)  #元祖形式转化成时间戳形式
print (time.strftime('%Y-%m-%d %H:%M:%S',x )) #将元祖形式转换成自定义的字符串格式 (2016-12-04 23:24:59)
print (time.strptime('2016-12-04 23:24:59','%Y-%m-%d %H:%M:%S')) #将格式化字符串转换成元祖形式。(time.struct_time(tm_year=2016, tm_mon=12, tm_mday=4,\
#                              tm_hour=23, tm_min=24, tm_sec=59, tm_wday=6, tm_yday=339, tm_isdst=-1))






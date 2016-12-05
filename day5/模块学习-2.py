#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#模块分类：标准库（os,sys）
#         开源模块
#         自定义模块

#标准库：
#time、datetime模块
#Python中，通常有这几种方式来表示时间：1）时间戳 2）格式化的时间字符串 3）元组（struct_time）共九个元素。
import time,datetime
print ('time模块的：时间戳、字符串、元祖形式的时间转换')
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

print ('将元祖、字符串形式转换成Mon Dec  5 22:57:34 2016格式')
print ('''
%a    本地（locale）简化星期名称
%A    本地完整星期名称
%b    本地简化月份名称
%B    本地完整月份名称
%c    本地相应的日期和时间表示
%d    一个月中的第几天（01 - 31）
%H    一天中的第几个小时（24小时制，00 - 23）
%I    第几个小时（12小时制，01 - 12）
%j    一年中的第几天（001 - 366）
%m    月份（01 - 12）
%M    分钟数（00 - 59）
%p    本地am或者pm的相应符    一
%S    秒（01 - 61）    二
%U    一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。    三
%w    一个星期中的第几天（0 - 6，0是星期天）    三
%W    和%U基本相同，不同的是%W以星期一为一个星期的开始。
%x    本地相应日期
%X    本地相应时间
%y    去掉世纪的年份（00 - 99）
%Y    完整的年份
%Z    时区的名字（如果不存在为空字符）
%%    ‘%’字符
''')
print ('Mon Dec  5 22:57:34 2016 = %a %b %d %H:%M:%S %Y')   #linux系统下的时间字符串格式
print (time.asctime())  #time.asctime(time.struct) 将元祖形式转换成linux字符串格式显示时间 (Mon Dec  5 22:59:17 2016)
print (time.asctime(x)) #将指定的元祖形式的时间转换成linux系统下的字符串格式
print (time.ctime()) # time.ctime(sencond) 将时间戳形式转换成linux系统下的字符串格式。(Mon Dec  5 23:08:58 2016)
print (time.ctime(time.time()-120)) #将当前时间的前2分钟的时间戳形式转换成linux系统下的字符串格式

#datetime模块
print ('datatime模块重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo。')
#date类
print   ('date.max:', datetime.date.max)  #最大时间范围（9999-12-31）
print   ('date.min:', datetime.date.min)  #最小时间范围（0001-01-01）
print   ('date.today():', datetime.date.today())  #今天（2016-12-05）
print   ('date.fromtimestamp():', datetime.date.fromtimestamp(time.time())) #将时间戳转换为2016-12-05
print (datetime.date(2016, 10, 26))  #打印传递的时间
now = datetime.date(2016, 10, 26)
print (now.replace(day = 27))  #修改传递的时间（year, month, day都可以修改）
#time类
#datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] )
print (datetime.time(23, 46, 10))  #23:46:10
tm = datetime.time(23, 46, 10)
print   ('hour: %d, minute: %d, second: %d, microsecond: %d' % (tm.hour, tm.minute, tm.second, tm.microsecond)) #打印时间
tm1 = tm.replace(hour=20)  #修改时间
#datetime类
print(datetime.datetime.now()) #返回 2016-08-19 12:47:03.941925
print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2)) #时间替换













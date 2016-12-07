#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import sys,time
#python sys模块-5.py 1 2 3 4 5 运行这个文件，加上参数
#print (sys.argv)  #打印所有命令行参数列表。第一个元素是程序本身路径。['sys模块-5.py', '1', '2', '3', '4', '5']
#print (sys.argv[0]) #打印程序本身路径。 输出为：sys模块-5.py
#print (sys.argv[1]) #打印第一个参数。输出为：1
#sys.exit()        #退出程序，正常退出时exit(0)
print (sys.version)        #获取Python解释程序的版本信息
print (sys.maxsize)   #最大的Int值
print (sys.path)      #模块搜索路径
print (sys.platform)  #返回操作系统平台名称
sys.stdout.write('hello'+'\n')  #print ('hello') 当我们在Python中打印对象其实调用了 sys.stdout.write(obj+'\n')
#sys.stdin  #输入相关
#sys.stdout  #输出相关
#sys.stderr  #错误相关

#进度条
for i in range(5):
    sys.stdout.write('#')  #print ('hello')
    sys.stdout.flush()     #清空当前并输出下一个（1%清空后，显示2%....）
    time.sleep(0.5)

#进度条加强版
def rate_num(num,total):  #定义了进度条函数
    #temp = num / total   #求百分比的小数
    #temp_rate = int(temp * 100)  #求百分比
    r1 = '%d%%' %1
    print (r1)  #1% %%表示转义%的含义和linux中的\作用一致
    real_rate = '\r%s>%d%%' %("#"*num ,num)  #打印百分比 %%：转义其中一个%，\r:重新回到当前行的首个位置，覆盖之前的输出
    sys.stdout.write(real_rate)  #显示百分比
    sys.stdout.flush()  #清空当前并输出下一个（1%清空后，显示2%....）

for i in range(1,101): #进度条范围
    time.sleep(0.5)  #每隔0.5s显示一次
    rate_num(i,100)  #调用进度条函数
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/10/31 22:48'

import threading,time

#用函数方式实现多线程
def run2(n):
    print ('task:',n)
    time.sleep(2)
# 使用线程执行命令，target指定要执行的任务，args指定参数，参数要使用元祖形式。
task1 = threading.Thread(target=run2,args=('task1',)) #生成一个线程实例
task2 = threading.Thread(target=run2,args=('task2',))
#开始执行
task1.start()
task1.join()  #等待线程的执行结果，执行完了再执行下一个（串行）
task2.start()
#获取线程名
print (task1.getName())
print (task2.getName())


#用类实现多线程
class MyThreading(threading.Thread):  #必须继承threading.Thread类
    def __init__(self,n): #重写了__init__方法
        super(MyThreading,self).__init__()  #继承__init__属性
        self.n = n  #增加自己的属性

    def run(self):   #必须重写run方法（run方法里写具体执行的程序）
        print ('run task:',self.n)

t1 = MyThreading('t1')
t1.run()
t2 = MyThreading('t2')
t2.run()

#线程并发
for i in range(50):
    t = threading.Thread(target=run2,args=('t-%s' %i,))
    t.start()  #线程是并行的，不会等一个线程执行完在执行下一个

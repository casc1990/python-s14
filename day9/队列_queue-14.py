#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/11/19 20:18'

'''
队列(queue)：高效，解耦
    queue.Queue(maxsize=0) #先入先出  --默认
    queue.LifoQueue(maxsize=0) #后入先出
    queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列
    Queue.qsize()  #查看队列大小
    Queue.put('1')  #向队列存放数据
    Queue.put('2', block=True, timeout=None) #是否阻塞，超时时间
    Queue.get(block=True, timeout=None)  #取数据(取数据不能指定取什么数据，按队列的规则取)
    Queue.get_nowait()  #取数据不等待，没有了就抛出异常
    Queue.put_nowait() #同Queue.get_nowait()类似
'''

import time,queue

q = queue.Queue()
q1 = queue.LifoQueue() #后入先出
q2 = queue.PriorityQueue() #按优先级排列（数字越小，优先级越高）
q.put('1')
q.put('2')
q1.put('1')
q1.put('2')
q2.put((10,'1'))
q2.put((5,'2'))
print (q2.qsize()) #查看队列大小
print (q.get()) #输出：1
print (q1.get()) #输出：2 (get方法如果取不到数据会阻塞)
print (q2.get()) #输出：(5, '2') （数字越小，优先级越高）
print (q2.qsize())


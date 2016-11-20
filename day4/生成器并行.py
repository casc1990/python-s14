#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       #函数中出现yield，说明这个函数是一个生成器函数
       #yield相当于return,例如 yield 3 ，会把3返回；yield还会记录命令的执行位置，当下次再循环这个函数时，\
       #    会执行上次yield的之后位置的命令
       baozi = yield    #执行到这儿时，yield会返回baozi这个变量的值

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')   #同时调用2次consumer函数
    c2 = consumer('B')
    c.__next__()   #开始执行函数（打印yield之前的内容）print("%s 准备吃包子啦!" %name)
    c2.__next__()  #同上
    print("老子开始准备做包子啦!")
    for i in range(10):   #循环10次
        time.sleep(1)
        print("做了2个包子!")
        #send()函数等于__next__，但是send可以传递值给yield
        c.send(i)  #c.__next__();yield i（执行c.__next__()，并把i返回）
        c2.send(i+1)  #c2.__next__();yield i+=1
producer("alex")

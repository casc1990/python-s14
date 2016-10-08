#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
for i in range(10):
    if i <3:
        print ('loop:',i)
    else:
        continue  #continue跳到本次循环的开头，继续循环；break是跳出最内层循环体。
                  # 本例子中i<3时，会执行else，else里的continue会一直跳到for循环的开头，直到for循环结束
    print ('hehe..')

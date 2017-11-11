#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#Time ： 2017/11/11 18:26
import threading,time
import random


event = threading.Event()
def light():
    print ('\033[42;1m--green light on---\033[0m'.center(40,'*'))
    print ('\033[43;1m--yellow light on---\033[0m')
    print('\033[41;1m--yellow light on---\033[0m')



a = light()
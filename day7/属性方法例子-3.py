#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
class Flight(object):
    def __init__(self,name):
        self.flight_name = name
        self.hangban_status = 1

    def checking_status(self):
        print("checking flight %s status " % self.flight_name)
        return  self.hangban_status

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0 :
            print("flight got canceled...")
        elif status == 1 :
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter   # 修改flight_status属性需要通过@proerty.setter装饰器再装饰一下，此时需要写一个方法， 对这个flight_status进行更改。
    def flight_status(self,status):
        status_dic = {
            0 : "canceled",
            1 :"arrived",
            2 : "departured"
        }
        self.hangban_status = status
        print("\033[31;1mHas changed the flight status to \033[0m",status_dic.get(status) )

    @flight_status.deleter  # 删除
    def flight_status(self):
        print("status got removed...")

f = Flight("CA980")
f.flight_status
f.flight_status =  0 #触发@flight_status.setter
f.flight_status #再次查看状态，状态已经改变
del f.flight_status #触发@flight_status.deleter



#!/usr/bin/env python
#-*- coding:utf-8 -*-

def auth(func):
    def wrapper():
        pass

@auth
def index():
    print ('welcome access index page!')

@auth
def home():
    print ('welcome to home page!')

@auth
def bbs():
    print ('welcome to bbs page!')

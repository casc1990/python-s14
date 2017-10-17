#!/usr/bin/env python
#-*- coding:utf-8 -*-
name,passwd = 'alex','abc1234'
'''
#装饰器实现基本用户登录验证
def auth(func):
    def wrapper(*args,**kwargs):
        user = input('please your name: ').strip()
        password = input('please your password: ').strip()
        if user == name and passwd == password:
            print ('\033[32;1mUser has passwd authentication\033[0m')
            res = func(*args,**kwargs)  #run home()
            print ('--after authentication')
            return res   #返回home函数的返回值
        else:
            exit('\033[31;1mInvalid user name or password!\033[0m')
    return wrapper

def index():
    print ('welcome access index page!')

@auth
def home():
    print ('welcome to home page!')
    return 'from home'   #定义函数的返回值

@auth
def bbs():
    print ('welcome to bbs page!')
'''

#装饰器+参数实现多种认证方式登录
#总结：
    #装饰器如果有参数，需要在装饰器函数开头上再加一层函数来接收装饰器传过来的参数（第一层）
    #接收被装饰函数的装饰器函数会被执行2次（第二层）
    #接收被装饰函数参数的装饰器函数负责处理具体的装饰内容--附加功能（第三层）
def auth(auth_type):   #auth_type=file
    print ('auth_type:',auth_type)
    def outer_wrapper(func):   #func=home (这个函数会被执行两次)
        print ('func:',func)
        def wrapper(*args, **kwargs):  #args,kwargs接受用户传入给函数的任意参数
            print ('wrapper:',*args, **kwargs)
            if auth_type == 'file':
                user = input('please your name: ').strip()
                password = input('please your password: ').strip()
                if user == name and passwd == password:
                    print('\033[32;1mUser has passwd authentication\033[0m')
                    res = func(*args, **kwargs)  # run home()
                    print('--after authentication')
                    return res  # 返回home函数的返回值
                else:
                    exit('\033[31;1mInvalid user name or password!\033[0m')
            elif auth_type == 'remote':
                print ('welcone use remote authentication')

        return wrapper    # return hone （返回被装饰函数的内存对象）
    return outer_wrapper  #返回到outer_wrapper(func)开头，在执行一遍，只有这样，wrapper才会被执行

def index():
    print ('welcome access index page!')

@auth(auth_type='file')  #auth加（）会让装饰器在多执行一次被装饰的函数
def home():
    print ('welcome to home page!')
    return 'from home'   #定义函数的返回值

@auth(auth_type='remote')
def bbs():
    print ('welcome to bbs page!')

index()
home()  #run wrapper(home被调用时运行的是auth装饰器的wrapper函数)
#print (home())  #打印函数的返回值
bbs()  #run wrapper(同上)

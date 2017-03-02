#!/usr/bin/env python
#-*- coding:utf-8 -*-
#错误
'''
for i in range(10)
    print (i)
'''
print ('错误指程序在运行之前，python解释器检测到的语法错误')

#异常
lst = [1,2,3,4,5]
#print (lst[5])

print ('异常指程序运行中，遇到的内部错误')
'''
常见的异常如下：
NameError 尝试访问一个没有申明的变量
ZeroDivisionError 除数为 0
SyntaxError 语法错误
IndexError 索引超出序列范围
KeyError 请求一个不存在的字典关键字
IOError 输入输出错误（比如你要读的文件不存在）
AttributeError 尝试访问未知的对象属性
'''
'''
while 1:
    print ('这是一个求商的函数')
    c = input ("input 'c' continue, otherwise logout:")
    if c == 'c':
        a = input('first number: ')
        b = input('second number: ')
        try:      #try部分没有异常，不会走except
            print (float(a)/float(b))
            print ("**"*10)
        except ZeroDivisionError:  #try有异常，执行except相应分支的子句
            print ("The second number can't be zero!")
    else:
        break
'''
print('''如果没有异常发生，except 子句在 try 语句执行之后被忽略；
        如果try子句中有异常，该部分的其它语句被忽略，直接跳到 except 部分，
        执行其后面指定的异常类型及其子句''')
'''
class Calculator(object):
    is_raise = False
    def calc(self,express):
        try:
            return eval(express)
        except ZeroDivisionError:
            if self.is_raise:
                print ('zero can not be division')
            else:
                raise   #它的含义是将异常信息抛出
c = Calculator()
#print (c.calc("8/0"))  #执行 raise（将报错信息抛出）

c.is_raise = True  #修改对象属性
print (c.calc("4/0"))   #执行 print ('zero can not be division')

print ('raise的含义是将异常信息抛出')

while 1:
    print ("this is a division program.")
    c = input("input 'c' continue, otherwise logout:")
    if c == 'c':
        a = input("first number:")
        b = input("second number:")
    try:
        print (float(a)/float(b))
        print ("*************************")
    except ZeroDivisionError:  #ZeroDivisionError分支
        print ("The second number can't be zero!")
        print ("*************************")
    except ValueError:  #ValueError分支
        print ("please input number.")
        print ("************************")
    else:
        break
'''

'''
try:
    语句1
    ....
except 异常1：  #except多分支
    语句1
    ....
except 异常N：
    语句1
    ....
else:       #try没有异常，会走else子句
    语句1
    ....
'''
while 1:
    try:   #try无异常
        x = input("the first number:")
        y = input("the second number:")
        r = float(x)/float(y)
        print (r)
    except Exception as e:   #try异常，走except
        print (e)
        print ("try again.")
    else:    #except如果被忽略，走else
        break
print ('except Exception as e: 捕捉异常，并把异常保存给变量e')

#如果有了finally,不管前面执行的是 try,还是 except，它都要执行。因此一种说法是用 finally 用来在可能的异常后进行清理
'''
try:
do something
except:
do something
else:
do something
finally   #处理善后工作（try和except都不执行，finally也会执行）
do something
'''

while 1:
    try:
        x =1/0
    except Exception as e:  #try子句异常，走except，并打印异常
        print (e)
    finally:  #处理善后工作（try和except都不执行，finally也会执行）
        print ('del x')
        del x   #删除变量x

#断言
assert 1==1   #判断1肯定等于1，如果不是就抛出错误

print ('断言就是断定什么东西必然是什么，如果不是，就抛出错误')
class Account(object):
    def __init__(self, number):
        self.number = number
        self.balance = 0
    def deposit(self, amount):
        assert amount > 0
        self.balance += balance
    def withdraw(self, amount):
        assert amount > 0
        if amount <= self.balance:
            self.balance -= amount
        else:
            print ("balance is not enough.")

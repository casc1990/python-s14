#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#位置参数和关键字
def test(x,y,z):     #有参数的函数（形式参数）
    print (x)
    print (y)
    print (z)
a,b,c=1,2,3
print (a,b,c)
test(1,2,3)   #传递的值是实际参数
test(1,2,3)   #位置参数赋值调用（需与形式参数一一对应）
test(a,b,c)   #可以传递变量，变量的值会被函数调用（位置参数赋值调用）
test(z=3,x=1,y=2) #关键字参数赋值调用（与形式参数顺序无关，但是个数要和行参一致）
test(x=a,y=b,z=c)   #同上（虽然是顺序是一一对应，但还是关键字参数赋值调用）
test(1,2,z=3)     #位置参数和关键字参数一起出现时，会以位置参数方式传参，而且关键字参数必须写到最后面
#总结：位置参数调用：实参与形参位置一一对应
#     关键字调用：与形式参数顺序无关，但是个数要和行参一致
#     位置+关键字： 以位置参数方式传参，关键字参数必须在最后面

#默认参数（用途：提供默认值，比如软件的默认安装等等）
def connection_mysql(ip,passwd,user='root',port=3306): #默认参数放在位置参数的后面
    print (ip +'\n'+passwd,'\n'+user,'\n'+str(port))
    print ('connection mysql successful! ')

connection_mysql('192.168.1.1','123456')  #默认参数非必须传递（不传递使用默认值）
connection_mysql('192.168.1.1','123456','zhangsan',3307)  #如果传递，会覆盖默认值，以传递的值为准
connection_mysql(passwd='123456',ip='192.168.1.1',user='zhangsan')  #关键字参数赋值
#总结：默认参数非必须传递,默认参数必须放在位置参数的后面.
#用途：提供默认值，比如软件的默认安装等等）

#参数组
def test3(*args):   # *args接受N个位置参数，转换成元祖形式(args可以自定义)
    print (args)
A = [1,2,3,['hello','world'],{'name':'lisi'}]
test3(1,2,3,['hello','world'],{'name':'lisi'})    #调用test3函数，可以传递无限值(传递的值被转换成元祖)
test3(*[1,2,3,['hello','world'],{'name':'lisi'}]) # *[1,2,3,['hello','world'],{'name':'lisi'}]==*args
test3(*A)           #调用test3函数，传递列表变量
def test4(x,*args):
    print (x)      #第一个位置参数赋值给x
    print (args)   #其他赋值给args
test4(3,4,5)
#总结： *args接受N个位置参数，转换成元祖形式

def test5(**kwargs):  #**kvargs接受N个关键字参数，转换成字典格式
    print (kwargs)
    print (kwargs['name'])   #打印字典里值
    print (kwargs['age'])
    print (kwargs['sex'])
B = {'name':'alex','age':32,'sex':'F'}
test5(name='alex',age=32,sex='F')   #将关键字转换为字典的key，值为字典中的values
test5(**{'name':'alex','age':32,'sex':'F'}) #同上，输入为：{'sex': 'F', 'name': 'alex', 'age': 32}
test5(**B)   #传递字典参数

def test6(name,age=32,**kwargs):  #kwargs必须放在形式参数的最后面
    print (name)
    print (age)
    print (kwargs)

test6('alex',sex='F',hobay='tesla',age=8)   #从前向后匹配，将关键字参数赋值给**kwargs

def test7(name,age=32,*args,**kwargs):  #关键字参数放在位置参数的后面
    print (name)
    print (age)
    print (args)
    print (kwargs)
test7('alex')   #位置参数和关键字参数不传值，默认为空
test7('alex',age=44,sex='F',hobay='tesla')  #混合使用实例
#总结：**kwargs接受N个关键字参数，转换为字典（将关键字转换为字典的key，值为字典中的values）







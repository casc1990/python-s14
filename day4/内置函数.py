#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
#abs
print (abs(-1),abs(-(-0.90)))  #查看对象的绝对值
#假：0,None,[],{},(),''  注意：'  '空格为真
#bool
print (bool(1),bool(' '))  #bool判断元素是否为布尔值，空格为真
#all
print (all([1,-1,5]),all((0,1)),all({0:'a',2:1}))  #所有的元素都为真，结果才为真(如果是字典，只看key值)
#any
print (any((0,1)),any([]),any([0,0,0,-1]))  #只有有真，就为真（空为假）
#ascii
a = (ascii('[1,2]'))  #自动执行对象的__repr__方法，将传入的对象转换成字符串类型
print (type(a),a)
#进制转换
print (bin(5))  #0b101,0b表示二进制。 接收10进制的值，并把它转换成二进制。
print (oct(9))  #0o11,0o表示8进制。  接收10进制的值，并把它转换成八进制。
print (hex(10)) #0xa,0x表示16进制。  接收10进制的值，并把它转换成十六进制。
#bytes  把字符串转换成字节类型
#utf-8: 3字节   gbk：2字节  bytes=8bit
print (bytes('你好',encoding='utf-8'))  #bytes('要转换的字符串','按照什么编码')
print (bytes('你好',encoding='gbk'))  #bytes函数表示把字符串转换成字节类型。
print (bytes('ni',encoding='utf-8'))
#字节类型转换成字符串  str函数
new_str = str(bytes('你好',encoding='utf-8'),encoding='utf-8') #字节转换成字符串，要指定编码类型
print (new_str)

#callable()
def foo():
    pass
b = '123'
print (callable(foo),callable(b))  #查看对象能否被调用或者执行

#chr() ord()
print (chr(65))   #查看ascii码中编号为65的字符是什么
print (ord('y'))  #查看ascii码中字符y的编号是多少

#compile() exec() eval()
#compile(source, filename, mode[, flags[, dont_inherit]])  编译字符串或者文件为python code
#   中文说明：将source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值。
#           参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
#           参数source：字符串或者AST（Abstract Syntax Trees）对象。
#           参数model：指定编译代码的种类。可以指定为 ‘exec(执行)’,’eval(表达式)’,’single(单行执行)’。
code = "3 * 4 + 5"
code2 = "for i in range(10): print (i)" #python字符串
cmpcode = compile(code2,'',"exec")   #编译字符串为python code（必须传递3个参数）
cmpcode2 = compile(code,'','eval')
exec(cmpcode) #执行python代码或者字符串
e = eval(cmpcode2)   #表达式求值，将结果返回
print (e)
#总结：compile编译  exec执行python代码或者字符串，没有返回值  eval表达式求值，将结果返回

#dir()
print (dir(dict))  #查看对象所拥有的方法

#help()
print (help(list))  #查看对象方法的帮助信息
list1 = ['a','b','c']
help(list1.append)  #查看具体某个方法的帮助信息

#divmod() 返回商和余数的元祖形式
print (divmod(10,2))  #返回两个数相除的商和余数（元祖形式）
n1,n2 = divmod(11,2)  #通过divmod可以计算分页数（n2!=0,n1+=1）
print(n1,n2)

#enumerate
for num,i in enumerate(['a','b','c','d']):  #enumerate加序号
    print (num,":",i)

#id（）
print (id('a'))  #元素的内存地址

#isinstance()  用来判断对象是否是某个类的实例
a = 'hello'
b = ['a','b','c','d']
print (isinstance(a,str))  #a是字符串这个类的实例
print (isinstance(b,str))  #b不是字符串这个类的实例，b是列表的实例

#filter 过滤
#filter语法格式： filter(函数,需要过滤的列（必须可迭代）)  2个参数都是必须的
##filter循环第二个参数，让第二个参数的每个值都执行第一个函数，如果函数的返回值为True，表示元素合法
def f(args):  #定义过滤函数
    if args > 22:
        return True   #条件成立，返回True,(这里的True是为了通告给filter函数)
li = [11,22,33,44,55]
res = filter(f,li) #列表li中的值依次传入函数f，函数的返回值为True,追加到res中
print (res)
print (list(res))  #python3中要使用类型转换

#lambda  lambda函数也叫匿名函数，会将表达式的结果作为返回值返回
#语法格式：lambda [arg1[,arg2,arg3....argN]]:expression
add1 = lambda x,y:x+y # def add1(x,y): retrun x+y
res = add1(1,3)   #调用匿名函数
print (res)   #会将表达式的结果作为返回值返回
li = [11,22,33,44,55]
result = filter(lambda x:x>22,li)  #filter中用lambda函数，lambda可以将大于22的retrun给result
print (list(result))

#map  对元素批量执行统一操作
#语法格式：map(函数，可迭代对象)
def f2(args):  #要执行的操作
    return args + 100
li = [11,22,33,44,55]
result2 = map(f2,li)  #map函数
res2 = map(lambda x:x + 100,li) #使用lambda函数返回结果给map
print (list(result2))
print (list(res2))
#filter和map的区别：
#filter：函数返回True，将元素添加到结果中 （可循环对象里面的值）
#map：将函数返回值添加到结果中 （返回值）

#locals() globals()
print (locals()) #查看本文件中所以的局部变量
print (globals())  #查看本文件中所以的全局变量

#len() 查看元素长度
name = '小明'
print (len(name))  #python3中汉字是按个统计的，python2.7中，按字节统计

#max() min() sum()
li = [1,33,77,44]
print (max(li))  #最大值
print (min(li))  #最小值
print (sum(li))  #求和

#repr() 执行元素或者类、函数的__repr__方法，如果没有这个方法就保错
r = repr('hello')  #'hello'.__repr__()
str_r = 'hello'.__repr__()
print (r,str_r)

#reversed()  第一个元素和最后一个元素反转  执行元素或者类、函数的.reversed()方法，如果没有这个方法就保错
lst = [1,2,3,4]
lst.reverse()   #结果为：[4, 3, 2, 1] 原地修改，没有返回值
r = lst.reverse()   #原地修改，没有返回值(None)
print (r)
lst2 = [5,6,7,8]
reversed(lst2)    #等价于lst2.reverse() 原地修改，也没有返回值
print (lst,lst2)

#round() 四舍五入
r = round(1.2)  #四舍五入
t = round(1.5)
print (r,t)

#sorted() 按ascii排序
lst = [12,2,3,41]
lst3 = [22,45,1,2,6]
print (lst3)
lst.sort()    #排序
sorted(lst3)  #lst3.sort()






print (lst)

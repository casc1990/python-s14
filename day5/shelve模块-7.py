#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import shelve
#shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式,
#shelve中key必须为字符串，而值可以是python所支持的数据
#shelve最重要的函数是open，在调用它的时候（使用文件名作为参数），它会返回一个shelf对象，可以用它来存储内容。
#在使用shelve模块修改存储的对象，必须将临时变量绑定到获得的副本上，并且在它被修改后重新存储这个副本。
s = shelve.open('test.db')   #打开一个文件
s['x'] = ['a','b','c']  # 插入列表数据
s['z'] = {'name':'zhangsan','age':26} #插入字典
s['y'] = 'string'  #插入字符串
s.close()   #关闭后同步到文件。（关闭后会生成.bak,.dat,.dir结尾的三个文件，并不会生成打开的文件(test.db)）
e = shelve.open('test.db')
print (e['x'])  #查看序列化的数据
#del e['x']    #删除键值对
for i in e.items():    #items() 查看所有的键值对
    print('键[{}] : 值[{}]'.format(i[0], e[i[0]]))   #打印kv列表
e['x'].append('d')  #数据不能直接修改。切记
print (e['x'])  #数据未被修改。['a', 'b', 'c']
#修改数据
temp = e['x']   # 将变量的值绑定到临时变量上。
temp.append('d')  #修改临时变量
print (temp)
e['x'] = temp  #再将临时变量的值赋值给变量
print (e['x'])  #数据就被修改了
e.close()  #关闭文件


'''
（1）以上代码将所有内容都放到函数中会让程序更加结构化。
（2）主程序放到main函数中，只有在if __name__ == '__main__'条件成立的时候才被调用。这意味着可以在其他程序中将这个程序作为模块导入，然后调用main()函数。
（3）在main函数中打开数据库，然后将其作为参数传给另外需要它的函数。在大多数情况下最好避免使用全局变量。
（4）对读取的内容调用strip和lower函数以生成了一个修改后的版本。如果总是对用户的输入使用strip和lower函数，那么就可以让用户随意输入大小写字母和添加空格
（5）使用try/finally确保数据库能正常关闭。我们永远不知道什么时候会出错，如果程序在没有正确关闭数据库的情况下终止，那么数据库文件就有可能被损坏。
'''
def store_person(db):
    user_id = input('Enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')  # 在person里定义子字典
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone: ')
    db[user_id] = person  #完成键值对应关系，保存到数据库(就是将用户输入的用户信息保存到user_id这个key里)
def lookup_person(db):
    user_id = input('Enter ID numbers: ')  # 获取键
    values = input('What would you like to know ?(Enter name,age,phone)')    # 获取子字典的键
    print (values.capitalize() + ":",db[user_id][values])
def print_help():
    print('The available commands are:')
    print('store : stores information about a person')
    print('lookup : looks up a person from ID number')
    print('quit : save changes and exit')
    print('? : prints this message')
def enter_command():
    cmd = input('Enter command(? for help): ')
    cmd = cmd.strip().lower()
    return cmd
def main():
    database = shelve.open('test.db')
    try:
        while True:
            cmd = enter_command()
            if cmd == '?':
                print_help()
            elif cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__': main()





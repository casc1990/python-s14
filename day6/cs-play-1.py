#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

class Role(object):   #class 类名称：定义类。object：表示继承object父类。所有的类都继承object父类
    #初始化函数（也叫构建函数），类被实例化就会继承定义的这些属性。
    #name,weapon,role是被实例化时要传递的参数。life_value,money是默认值变量，如果不传递值，会使用默认值，如果传递，使用指定的值
    #def __init__(self,*args): 表示可以传递任意个数的参数，同函数
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        print (self)  #<__main__.Role object at 0x005A5B90>. self也是一个对象
        self.name = name   #self.name等于类被实例化时用户传递的name这个变量的值(实例变量)
        self.role = role  #同上
        self.weapon = weapon
        self.life_value = life_value  #如果用户没有传递life_value参数，self.life_value=100（使用默认值），如果传递了，使用指定的值
        self.money = money   #同上
        self.email = '962549026@qq.com'  #这个属性不是通过参数传入的，是我们定义的默认属性。

    def shot(self):   #类中的方法（函数）
        # 开了枪后要减子弹数
        print("shooting...")

    def got_shot(self):  #同上
        # 中枪后要减血
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):  #类中的方法（函数）--调用这个方法要传递gun_name这个变量
        # 检查钱够不够,买了枪后要扣钱
        print("%s just bought %s" % (self.name,gun_name))

r1 = Role('Alex', 'police', 'AK47') #实例化一个对象
r2 = Role('Jack', 'terrorist', 'B22',200,20000)  #实例化一个对象
print (r1.life_value) #100 调用类的属性。life_value使用了默认值
print (r2.life_value) #200 life_value使用了指定的值
print (r1.email)  #962549026@qq.com
print (r2.email)  #962549026@qq.com
r1.buy_gun('手枪') #Alex just bought 手枪. 调用类中的方法
r2.buy_gun('步枪') #Jack just bought 步枪. 调用类中的方法
print (Role)  #<class '__main__.Role'> 说明Role是一个class
print (r1)  #<__main__.Role object at 0x00635B90> 说明r1是Role的实例，r1的内存地址

#类中self的作用：
#在类的外部
#    在r1实例化过程中，r1 = Role('Alex', 'police', 'AK47') 字符串'Alex', 'police', 'AK47'通过初始化函数（ __init__() ）的参数已经存入到内存中，\
#    并且以 Role类型的面貌存在，组成了一个对象，这个对象和变量 r1 建立引用关系。这个过程也可说成这些数据附加到一个实例上\
#    这样就能够以: object.attribute 的形式，在程序中任何地方调用某个数据，例如上面的程序中以 r1.life_value 的方式得到 100 。\
#    这种调用方式，在类和实例中经常使用，点号“.”后面的称之为类或者实例的属性。
#在类的内部：
#     在类内部，就是将所有传入的数据都赋给一个变量，通常这个变量的名字是 self。注意，这是习惯，而且是共识，所以，看官不要另外取别的名字了。
#     在初始化函数中的第一个参数 self，就是起到了这个作用——接收实例化过程中传入的所有数据，这些数据是初始化函数后面的参数导入的。
#     显然，self 应该就是一个实例（准确说法是应用实例），因为它所对应的就是具体数据.

#总结：
#     其实让我们拓展了对 self 的认识，也就是它不仅仅是为了在类内部传递参数导入的数据，还能在初始化函数中，通过 self.attribute 的方式，
#     规定 self 实例对象的属性，这个属性也是类实例化对象的属性，即做为类通过初始化函数初始化后所具有的属性。所以在实例 r1 中，
#     通过 r1.email 同样能够得到该属性的数据。
#     在这里，就可以把 self 形象地理解为“内外兼修”了。或者按照前面所提到的，将 r1 和 self 对应起来，self 主内，r1 主外。
#     类的实例 r1 对应着 self，r1 通过 self 导入实例属性的所有数据。
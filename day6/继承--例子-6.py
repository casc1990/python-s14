#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

class School(object):   #定义学校类
    def __init__(self,name,addr): #初始化名字、地址、学员、老师
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []
    def enroll(self,stu_obj):  #提供注册功能并将注册的学员加入到学员列表中
        print ('为学员%s办理注册手续' %self.name)
        self.students.append(stu_obj)
    def hire(self,staff_obj):  #提供雇佣功能，将老师信息加入到老师列表中
        self.staffs.append(staff_obj)
        print("雇佣新员工%s" % staff_obj.name)

class SchoolMenber(object):  #所有人员类
    def __init__(self,name,age,sex): #初始化人员的名字、年龄、性别
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):  #预留功能
        pass

class Teacher(SchoolMenber): #老师继承SchoolMenber并添加新的属性
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary  #添加实例属性
        self.course = course
    def tell(self):  #重写tell方法
        print ('''
         -----info of Teacher:%s---
         Name:%s
         Age:%s
         Sex:%s
         Salary:%s
         Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self): #添加讲课功能
        print("%s is teaching course [%s]" % (self.name, self.course))

class Students(SchoolMenber): #学生继承SchoolMenber并添加新的属性
    def __init__(self,name,age,sex,stu_id,grade):
        super(Students, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade
    def tell(self): #重写tell方法
        print('''
                ---- info of Student:%s ----
                Name:%s
                Age:%s
                Sex:%s
                Stu_id:%s
                Grade:%s'''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self, amount): #添加交学费方法
        print("%s has paid tution for $%s" % (self.name, amount))

school = School("老男孩IT","沙河") #实例化学校类

t1 = Teacher("Oldboy",56,"MF",200000,"Linux")  #实例化老师类
t2 = Teacher("Alex",22,"M",3000,"PythonDevOps")

s1 = Students("ChenRonghua",36,"MF",1001,"PythonDevOps")  #实例化学生类
s2 = Students("徐良伟",19,"M",1002,"Linux")


t1.tell()  #调用老师的tell方法
s1.tell()  #调用学生的tell方法
school.hire(t1)  #调用学校的雇佣功能，并把s1(老师)这个类作为参数传入
school.enroll(s1) #调用学校的注册功能，并把t1(学生)这个类作为参数传入
school.enroll(s2)

print(school.students) # 打印所有的学生。（学生所对应的实例）
#输出为：[<__main__.Students object at 0x006A6170>, <__main__.Students object at 0x006A6190>]
print(school.staffs)
school.staffs[0].teach()  #打印老师这个实例里的teach属性
#输出为：Oldboy is teaching course [Linux]
for stu in school.students:  #为所有的学生叫费
    stu.pay_tuition(5000)
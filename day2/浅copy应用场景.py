#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import copy
#浅copy应用场景（联合账号）
person = ['name',['工资',1000]]
#以下3种方式都可以实现浅copy
p1 = person.copy()
p2 = person[:]
p3 = list(person)
p1[0] = 'zhangsan'   #张三套用person列表模板，生成工资模板
p2[0] = 'fengjie'    #张三媳妇套用person列表模板，生成工资模板
p1[1][1] = 800       #其中任何人花费，工资都会变
p2[1][1] = 1200
print (p1)
print (p2)
print (p3)

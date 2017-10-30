#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
__date__ = '2017/10/31 0:07'

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

#Pexpect 还不能在 Windows 的标准 python 环境中执行
import pexpect,sys

child = pexpect.spawn('ssh pengbo14@172.19.22.240')  #执行命令
fout = open('pexpect.log','w')
child.logfile = fout  #日志写入到文件
#child.logfile = sys.stdout  #日志定义到标准输出

child.expect("'s Password: ")  #匹配输出
child.sendline("passwd")   #发送内容
child.expect('#')  #匹配#
child.sendline('ls /home')
child.expect('#')

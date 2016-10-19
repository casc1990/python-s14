#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo
import sys,time
for i in range(30):
    sys.stdout.write('#')
    sys.stdout.flush()     #立即刷新到硬盘
    time.sleep(0.5)
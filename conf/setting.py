#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 10:40 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : setting.py
# @Software: PyCharm

import os
#根路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#数据库路径
BASE_DBDIR = os.path.join(BASE_DIR,'db')
#添加日志路径
BASE_LOGDIR = os.path.join(BASE_DIR,'log')

print(BASE_DIR)
print(BASE_DBDIR)
print(BASE_LOGDIR)
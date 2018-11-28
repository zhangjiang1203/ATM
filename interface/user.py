#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 10:44 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : user.py
# @Software: PyCharm

from db import db_handler

def register_handler(name,password,balance=15000):
    '''
    判断用户是否存在
    :return:
    '''
    user_dic = db_handler.select(name)
    return user_dic
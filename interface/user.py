#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 10:44 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : user.py
# @Software: PyCharm

from db import db_handler

def user_exist(name):
    '''
    判断用户是否存在
    :return:存在返回对应的字典，不存在返回None
    '''
    user_dic = db_handler.select(name)
    return user_dic

def register_handle(name,password,salary,loginCount=0):
    '''
    保存用户信息
    :return:
    '''
    user_dit = {"name":name,
                "password":password,
                "salary":float(salary),
                "loginCount":loginCount,
                "redit":salary}
    db_handler.save(user_dit)
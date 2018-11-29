#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 10:40 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : common.py
# @Software: PyCharm
from interface import user
from db import db_handler
from core import src
from functools import wraps

def login_auth(func):
    '''
    登录装饰器
    :param func:
    :return:
    '''
    def wrapper(*args, **kwargs):
        # 先判断是否登录再去执行函数
        if len(src.login_dict) > 0:
            res = func(*args, **kwargs)
        else:
            while True:
                name = input("请输入用户名:>>>").strip()
                user_dict = user.user_exist(name)
                if user_dict:
                    password = input("请输入密码:>>>").strip()
                    # 获取用户信息进行比对
                    if user_dict['loginCount'] == 3:
                        print("\033[31m该账号已锁定\033[0m")
                        break
                    if user_dict["password"] == password:
                        src.login_dict = user_dict
                        res = func(*args, **kwargs)
                        break
                    else:
                        # 修改登录次数
                        user_dict['loginCount'] += 1
                        # 刷新用户信息
                        db_handler.save(user_dict)
                        if user_dict['loginCount'] == 3:
                            print("\033[31m该账号已锁定\033[0m")
                            break
                        else:
                            print("\033[31m密码输入错误,请重试\033[0m")
                else:
                    print("\033[31m用户名不存在,请重新输入\033[0m")
        if len(src.login_dict) > 0:
            return res

    return wrapper


def record(func):
    '''
        记录用户操作装饰器
        :return:
        '''
    @wraps(func)
    def wrapper(*args,**kwargs):
        db_handler.record_user_operation(src.login_dict["name"] + " 调用 " + func.__name__)
        res = func(*args,**kwargs)
        return res
    return wrapper





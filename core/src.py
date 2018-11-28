#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 10:44 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : src.py
# @Software: PyCharm
from interface import user

def register():
    while True:
        name = input('请输入名称:>>>').strip()
        flag = user.register_handler(name)
        if flag:
            #继续输入
        else:
            print("用户已存在")



def login():
    pass

def check_balance():
    pass

def transfer():
    pass

def repay():
    pass

def withdraw():
    pass

def check_records():
    pass

def shopping():
    pass

def check_shoppingcard():
    pass


#将对应的功能和方法关联起来
fun_dic = {
    "1":register,
    "2":login,
    "3":check_balance,
    "4":transfer,
    "5":repay,
    "6":withdraw,
    "7":check_records,
    "8":shopping,
    "9":check_shoppingcard
}

def run():
    while True:
        print("""
        1 注册
        2 登录
        3 查看余额
        4 转账
        5 取款
        6 还款
        7 查看流水
        8 购物
        9 查看购买商品
        """)
        choice = input("\033[31m请选择:>>>>\033[0m").strip()
        if choice not in fun_dic: continue
        fun_dic[choice]()

if __name__ == "__main__":
    run()
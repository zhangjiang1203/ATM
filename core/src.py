#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 10:44 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : src.py
# @Software: PyCharm
from interface import user,bank,shopping
from db import db_handler
from lib import common


login_dict = {}

def register():
    '''
    用户注册
    :return:
    '''
    global login_dict
    while True:
        name = input('请输入用户名:>>>').strip()
        flag = user.user_exist(name)
        if not flag:
            while True:
                password = input("请输入密码:>>>").strip()
                confirpwd = input("再次输入密码:>>>").strip()
                if password != confirpwd:
                    print("\033[31m两次输入密码不一致,请重新输入\033[0m")
                else:
                    break
            salary = input("请输入薪资:>>>").strip()
            if salary.isdigit():
                user.register_handle(name,password,salary)
                login_dict = user.user_exist(name)
                print("注册成功")
                break
            else:
                print("\033[31m请输入数字\033[0m")
        else:
            print("用户已存在")

def login():
    '''
    登录
    :return:
    '''
    global login_dict
    while True:
        name = input("请输入用户名:>>>").strip()
        user_dict = user.user_exist(name)
        if user_dict:
            password = input("请输入密码:>>>").strip()
            #获取用户信息进行比对
            if user_dict['loginCount'] == 3:
                print("\033[31m该账号已锁定\033[0m")
                break
            if user_dict["password"] == password:
                login_dict = user_dict
                print("登录成功")
                break
            else:
                #修改登录次数
                user_dict['loginCount'] += 1
                #刷新用户信息
                db_handler.save(user_dict)
                if user_dict['loginCount'] == 3:
                    print("\033[31m该账号已锁定\033[0m")
                    break
                else:
                    print("\033[31m密码输入错误,请重试\033[0m")
        else:
            print("\033[31m用户名不存在,请重新输入\033[0m")

@common.login_auth
@common.record
def check_balance():
    '''
    查看余额
    :return:
    '''
    global login_dict
    login_dict = user.user_exist(login_dict['name'])
    salary = login_dict["salary"]
    print("\033[31m尊敬的%s 先生/女士 您当前账户余额为 %s\033[0m" %(login_dict["name"],salary))


@common.login_auth
@common.record
def transfer():
    global login_dict
    login_dict = user.user_exist(login_dict['name'])
    while True:
        to_name = input("请输入转账账户:>>>").strip()
        if user.user_exist(to_name):
            money = input("请输入转账金额:>>>").strip()
            if money.isdigit():
                bank.transfer_interface(to_name, float(money))
                break
            else:
                print("金额输入不合法，请重新输入")
        else:
            print("账户不存在，请重新输入")

@common.login_auth
@common.record
def repay():
    '''
    返款账户
    :return:
    '''
    #判断是否欠款
    global login_dict
    login_dict = user.user_exist(login_dict['name'])
    balance = login_dict["salary"]
    if balance > 0:
        print("\033[31m当前账户余额充足，没有还款信息,👏👏👏土豪尽管花👏👏👏\033[0m")
    else:
        print("\033[31m尊敬的用户 %s 您已欠费 %s，请充值\033[0m" %(login_dict['name'],balance))
        while True:
            inputMoney = input("请输入还款金额:>>>").strip().lower()
            if inputMoney.isdigit():
                bank.payback_interface(inputMoney)
                print("还款成功")
                break
            else:
                print("\033[31m金额输入不合法\033[0m")


@common.login_auth
@common.record
def withdraw():
    global login_dict
    login_dict = user.user_exist(login_dict['name'])
    print("\033[31m当前用户 %s ,当前余额 %s,本次提现要扣除千分之五的手续费\033[0m" % (login_dict["name"],login_dict["salary"]))
    if login_dict["salary"] <=0 :
        print("当前余额不知足，请充值")
        return
    while True:
        money = input("请输入提现金额:>>>").strip()
        if money.isdigit():
            bank.withdraw_interface(money)
            break
        else:
            print("金额输入不合法")



@common.login_auth
@common.record
def check_records():
    bank.get_balance_detail()

@common.login_auth
@common.record
def shopping():
    #获取最新的数据
    global login_dict
    login_dict = user.user_exist(login_dict["name"])
    shopping.shoppingAction()


@common.login_auth
@common.record
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
        5 还款
        6 取款
        7 查看流水
        8 购物
        9 查看购买商品
        """)
        choice = input("\033[31m请选择:>>>>\033[0m").strip()
        if choice not in fun_dic: continue
        fun_dic[choice]()

if __name__ == "__main__":
    run()
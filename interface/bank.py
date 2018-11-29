#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 10:59 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : bank.py
# @Software: PyCharm

from db import db_handler
from core import src

def transfer_interface(to_name,money):
    '''
    给指定用户转账
    :param to_name:
    :param account:
    :return:
    '''
    to_user_dic = db_handler.select(to_name)
    if to_user_dic:
        if src.login_dict["salary"] > money:
            src.login_dict["salary"] -= money
            to_user_dic["salary"] += money
            db_handler.save(src.login_dict)
            db_handler.save(to_user_dic)
            db_handler.bank_action_save("%s 转账 给%s  %s" %(src.login_dict["name"],to_name,float(money)))
            print("转账成功，当前用户 %s 余额 %s" %(src.login_dict["name"],src.login_dict["salary"]))
        else:
            print("\033[31m账户余额不足,转账失败\033[0m")

    else:
        print("\033[31m账户不存在\033[0m")


def payback_interface(money):
    '''
    还款
    :param money:
    :return:
    '''
    flag = True
    while flag:
        confirm = input("确定要还款吗？(y/n)").strip().lower()
        if confirm not in ['y', 'n']: continue
        # 修改账号余额，开始还款
        if confirm == "y":
            src.login_dict["salary"] += float(money)
            db_handler.save(src.login_dict)
            db_handler.bank_action_save("%s 还款 %s " %(src.login_dict["name"],float(money)))
            print("\033[31m还款成功，当前余额%s\033[0m" % (src.login_dict["salary"]))
            flag = False
        else:
            # 取消返回上一级操作
            flag = False

def withdraw_interface(money):
    '''
    提现扣除千分之五 手续费
    :param money:
    :return:
    '''
    src.login_dict["salary"] -= float(money) * (1 + 0.005)
    if src.login_dict["salary"] >0:
        print("提现成功，兄弟，钱不多，省着点花，当前余额 %s" %src.login_dict["salary"])
        db_handler.save(src.login_dict)
        db_handler.bank_action_save("%s 提现 %s 手续费 %s" %(src.login_dict["name"],float(money),float(money)*0.005))
    else:
        print("提现失败，余额不足")


def get_balance_detail():
    '''
    获取账号流水
    :return:
    '''
    db_handler.check_balance()
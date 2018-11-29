#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 2:30 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : db_handler.py
# @Software: PyCharm

#引入类库
import os
import json
import time
from conf import setting
from core import src

def select(name):
    '''
    验证用户是否存在
    :param name:
    :return:
    '''
    path = os.path.join(setting.BASE_DBDIR,"%s.json" %name)
    if os.path.exists(path):
        with open(path,"r",encoding='utf-8') as f:
            return json.load(f)
    else:
        return None

def save(user_dic):
    '''
    保存用户信息
    :param user_dic:
    :return:
    '''
    path = os.path.join(setting.BASE_DBDIR,"%s.json" %user_dic["name"])
    with open(path,"w",encoding='utf-8') as f:
        json.dump(user_dic,f)
        f.flush()#立刻写入硬盘


def bank_action_save(bank_action):
    '''
    保存用户的流水操作
    :param bank_action:
    :return:
    '''
    timeStr = time.strftime("%Y-%m-%d %X ")
    path = os.path.join(setting.BASE_LOGDIR,"%s.log" %src.login_dict["name"])
    if os.path.exists(path):
        with open(path,"r",encoding='utf-8') as f_read,open("tempBalance.log","w+",encoding='utf-8') as f_write:
            for line in f_read:
                f_write.write(line)
            f_write.write(timeStr + '  ' + bank_action + "\n")
            f_write.flush()
            os.remove(path)
            os.rename('tempBalance.log', path)
    else:
        with open(path,'w',encoding='utf-8') as f_write:
            f_write.write(timeStr + '  ' + bank_action + "\n")

def check_balance():
    '''
    查看个人账号流水
    :return:
    '''
    path = os.path.join(setting.BASE_LOGDIR, "%s.log" %src.login_dict["name"])
    if os.path.exists(path):
        with open(path,"r",encoding='utf-8') as f_read:
            print('账号流水'.center(80, "*"))
            for line in f_read:
                print(line)
            print("end".center(80,"*"))
    else:
        print("当前暂无流水记录")


def record_user_operation(record):
    '''
    保存用户操作记录
    :param record:
    :return:
    '''
    path = os.path.join(setting.BASE_LOGDIR, "appOperationLog.txt")
    timeStr = time.strftime("%Y-%m-%d %X ")
    if os.path.exists(path):
        with open(path,"r",encoding='utf-8') as f_read,open("tempBalance.txt","w+",encoding='utf-8') as f_write:
            for line in f_read:
                f_write.write(line)
            f_write.write(timeStr + '  ' + record +  "\n")
            f_write.flush()
            os.remove(path)
            os.rename('tempBalance.txt', path)
    else:
        with open(path,'w',encoding='utf-8') as f_write:
            f_write.write(timeStr + '  ' + record + "\n")

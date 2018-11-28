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
from lib import common
from conf import setting

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
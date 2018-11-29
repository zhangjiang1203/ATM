#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 10:10 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : manager.py
# @Software: PyCharm
import os
import sys
from core import src


if __name__ == "__main__":
    # print("开始执行")
    # #每次都获取最上面的路径地址
    # print(os.path.abspath(__file__))
    # print(os.path.dirname(os.path.abspath(__file__)))
    # #往上面找两层
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    src.run()

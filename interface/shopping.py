#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 5:37 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : shopping.py
# @Software: PyCharm
from core import src

product_list = [['Iphone7',5800],
                ['Coffee',30],
                ['疙瘩汤',10],
                ['Python Book',99],
                ['Bike',199],
                ['ViVo X9',2499]]

def shoppingAction():
    shopFlag = True
    shopCar = {}
    user_name = src.login_dict["name"]
    user_balance = src.login_dict["salary"]
    print("\033[32m尊敬的用户 %s 你的余额为%s,预祝你购物愉快\033[0m" % (user_name, user_balance))

    while shopFlag:
        for index, shop in enumerate(product_list):
            print(index, shop)
        choice = input("请输入商品编号进行购买，输入q退出:>>>").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < 0 or choice >= len(product_list): continue
            # 添加商品，展示用户余额信息。若是余额不够就提示用户金钱不足
            goods = product_list[choice]
            # 修改金额
            good_price = goods[1]
            good_name = goods[0]
            if user_balance >= good_price:
                if good_name in shopCar:
                    # 之前已经添加到购物车
                    shopCar[good_name]["count"] += 1
                else:
                    shopCar[good_name] = {"price": good_price, "count": 1}
                user_balance -= goods[1]
                # 更新用户余额
                src.login_dict["salary"] = user_balance
                # 输出购买数据
                print("\033[34m%s已添加到购物车，剩余金额%s\033[0m" % (good_name, str(user_balance)))
            else:
                print("\033[31m余额不足，还差%s元，请充值🤣🤣🤣🤣\033[0m" % (good_price-user_balance))
        else:
            if choice.lower() == "q":
                if len(shopCar) == 0:
                    shopFlag = False
                    break
                print("\033[31m已购买商品\033[0m".center(80, "*"))
                print("\033[31mid          商品           数量          单价          总价\033[0m")
                total = 0
                for i, key in enumerate(shopCar):
                    print("\033[31m%s%18s%10s%13s%13s\033[0m" % (i, key, shopCar[key]["count"],
                                                                 shopCar[key]["price"],
                                                                 shopCar[key]["price"] * shopCar[key]["count"]))
                    total += shopCar[key]["price"] * shopCar[key]["count"]

                print("\033[31mend\033[0m".center(80, "*"))
                while shopFlag:
                    confirm = input("确定要购买吗？(y/n)").strip().lower()
                    if confirm not in ['y', 'n']: continue
                    # 修改账号余额，清空购物车
                    if confirm == "y":
                        users = loginM.getUseraccount()
                        for user in users[:]:
                            if user["account"] == user_name:
                                print("\033[31m此次购物总花费: %s  你的余额为: %s\033[0m" % (total, user_balance))
                                users.remove(user)
                                user["salary"] = user_balance
                                users.append(user)
                                loginM.changAllAccount(users)
                                shopFlag = False
                                shopCar = {}
                                continue
                    else:
                        # 清空购物车
                        shopCar = {}
                        shopFlag = False
            else:
                print("\033[31m请输入商品编号\033[0m")
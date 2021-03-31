# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 14.py
"""获取最大值函数:"""


def max(a, b):
    """获取最大值函数"""
    if a < b:
        return b
    elif a > b:
        return a
    else:
        return a


if __name__ == "__main__":
    a = input("输入a:")
    b = input("输入b:")
    print("最大值是:{}".format(max(a, b)))


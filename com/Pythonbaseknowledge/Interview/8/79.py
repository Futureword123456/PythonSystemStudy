# -*- coding: utf-8 -*-
# @Time : 2021/3/15 0015
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 79.py
"""求1+2!+3!+...+20!的和。"""


def f(n):
    """计算阶乘"""
    sun = 1
    for i in range(1, n + 1):
        sun = sun * i
    return sun


def su(n):
    rest = 0
    for i in range(1, n + 1):
        rest += f(i)
    return rest


if __name__ == "__main__":
    print(su(20))
    print(f(4))

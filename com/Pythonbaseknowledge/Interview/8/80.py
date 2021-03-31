# -*- coding: utf-8 -*-
# @Time : 2021/3/15 0015
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 80.py
"""利用递归方法求5!。"""


def f(n):
    """用递归的方法计算阶乘"""
    if n == 0:
        sun = 1
    else:
        sun = n * f(n - 1)
    return sun


if __name__ == "__main__":
    print(f(5))

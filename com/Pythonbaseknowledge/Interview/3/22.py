# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 22.py
"""最大公约数算法
最大公因数，也称最大公约数、最大公因子，指两个或多个整数共有约数中最大的一个
"""


def dfc(a, b):
    m = 1
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            m = i
    return m


if __name__ == "__main__":
    print(dfc(4,8))

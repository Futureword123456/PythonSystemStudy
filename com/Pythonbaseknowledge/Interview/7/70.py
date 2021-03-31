# -*- coding: utf-8 -*-
# @Time : 2021/3/14 0014
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 70.py
"""判断一个数是否是素数"""
from math import sqrt

"""素数：除了1和它本身不在有其他公因数的数 说明这个数就不是素数"""


def alone():
    """判断是否是素数"""
    # 1、在某一个范围的数中得到一个数
    count = 0
    flag = 0
    for i in range(101, 201):
        flag = 1
        k = int(sqrt(i + 1))
        for j in range(2, int(i/2)):
            if i % j == 0:
                flag = 0
                break
        if flag:
            count = count + 1
            print(i, end=" ")

    print(count)
    # 2、用这个数除以得到一个余数，余数是零就不是素数


if __name__ == "__main__":
    alone()

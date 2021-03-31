# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 20.py
"""阿姆斯特朗数
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。

1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
"""
import math


def ArmstrongNumber(n):
    for i in range(1, n):
        bits = i % 10
        ten = int((i % 100) / 10)
        ohb = int(i / 100)
        n = len(str(i))
        rest = math.pow(bits,n) + math.pow(ten,n) + math.pow(ohb, n)
        if i == rest:
            print(i,end=" ")


if __name__ == "__main__":
    ArmstrongNumber(1000)

# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 6.py

"""
圆的面积公式为 ：
公式中 r 为圆的半径。
"""
import math


def CircleArea(r):
    return math.pi * r * r


if __name__ == "__main__":
    r = float(input("输入半径:"))
    print("圆的面积:{:.3}".format(CircleArea(r)))

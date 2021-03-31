# -*- coding: utf-8 -*-
# @Time : 2021/3/12 0012
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 65.py

"""输入三个整数x,y,z，请把这三个数中的最大值。"""


def Max(a, b, c):
    if b > a:
        a = b
    elif c > a:
        a = c
    return a


if __name__ == "__main__":
    x1 = int(input("输入数:"))
    x2 = int(input("输入数:"))
    x3 = int(input("输入数:"))
    print(Max(x1,x2,x3))

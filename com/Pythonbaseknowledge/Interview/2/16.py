# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 16.py
"""输出指定范围内的素数:素数
（prime number）又称质数，有无限个。除了1和它本身以外不再被其他的除数整除。

以下实例可以输出指定范围内的素数："""
from pygal.util import swap

"""判断两个数之间是否的质数数量"""


def alone(a, b):
    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    flag = 0
                    break
            else:
                print("{}是质数".format(num), end=",")


def aloneAll(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
        alone(a, b)
    else:
        alone(a, b)


if __name__ == "__main__":
    a = int(input("输入a:"))
    b = int(input("输入b:"))
    aloneAll(a, b)

# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 17.py
"""阶乘实例:
整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
"""


def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum = sum*i
    return sum


if __name__ == "__main__":
    a = int(input("输入a:"))
    if a<0:
        print("负数没有阶乘")
    else:
        print("{0}的阶乘是{1}".format(a,factorial(a)))

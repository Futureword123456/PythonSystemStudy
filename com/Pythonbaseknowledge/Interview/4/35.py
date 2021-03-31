# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 35.py
"""计算计算公式 13 + 23 + 33 + 43 + …….+ n3
实现要求：
输入 : n = 5
输出 : 225
公式 : 13 + 23 + 33 + 43 + 53 = 225
输入 : n = 7
输入 : 784
公式 : 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784"""


def cacle(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum


if __name__ == "__main__":
    print(cacle(5))

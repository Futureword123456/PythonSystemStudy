# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 44.py
"""Python 计算列表元素之和"""
list1 = [11, 5, 17, 18, 23]
# print(sum(list1))

"""统计列表的和"""


def sum1(lst):
    total = 0
    for i in lst:
        total = total + i
    return total


if __name__ == "__main__":
    list1 = [11, 5, 17, 18, 23]
    print(sum1(list1))

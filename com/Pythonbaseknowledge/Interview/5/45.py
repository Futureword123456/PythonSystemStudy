# -*- coding: utf-8 -*-
# @Time : 2021/3/9 0009
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 45.py
"""Python 计算列表元素之积"""


def Take(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for i in lst1:
        sum1 = sum1 + i
    for j in lst2:
        sum2 = sum2 + j
    return sum1 + sum2


if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(Take(list1, list2))

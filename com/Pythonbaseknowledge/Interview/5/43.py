# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 43.py
"""Python 计算元素在列表中出现的次数"""
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
print(lst.count(10))


def cout(num):
    cout = 0
    for i in lst:
        if i == num:
            cout = cout + 1
    return cout


if __name__ == "__main__":
    print(cout(10))

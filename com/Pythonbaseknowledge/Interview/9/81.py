# -*- coding: utf-8 -*-
# @Time : 2021/3/16 0016
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 81.py
"""顺序查询"""


def serach(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


if __name__ == "__main__":
    lst = [1, 6, 9, 6, 3, 5,  2]
    print(serach(lst,2))
    print(lst[serach(lst,2)])


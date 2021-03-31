# -*- coding: utf-8 -*-
# @Time : 2021/3/16 0016
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 82.py
"""折半查询"""


def Bsearch(arr, low, high, x):
    # mid = int((low + high) / 2)
    if low <= high:
        mid = int(low + (high - low) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return Bsearch(arr, low, mid - 1, x)
        else:
            return Bsearch(arr, mid + 1, high, x)
    else:
        return -1


if __name__ == "__main__":
    lst = [2, 6, 3, 4, 10, 40, 5]
    x = 10
    rest = Bsearch(lst, 1, len(lst), x)
    print(rest)

# -*- coding: utf-8 -*-
# @Time : 2021/3/12 0012
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 63.py
"""选择排序"""


def SelectSort(arr):
    for i in range(0, len(arr)):
        minindex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
            """两个值交换"""
        # arr[i], arr[minindex] = arr[minindex], arr[i]
        temp = arr[i]
        arr[i] = arr[minindex]
        arr[minindex] = temp


if __name__ == "__main__":
    lst = [5, 6, 8, 9, 4, 3, 1]
    SelectSort(lst)
    print(lst)

# -*- coding: utf-8 -*-
# @Time : 2021/3/12 0012
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 64.py
"""冒泡排序"""


def BubbleSort(arr):
    for i in range(0, len(arr)):
        """最后一个元素已经排好序了"""
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                """交换"""
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    lst = [5, 6, 8, 9, 4, 3, 1]
    BubbleSort(lst)
    print(lst)

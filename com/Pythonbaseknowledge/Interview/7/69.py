# -*- coding: utf-8 -*-
# @Time : 2021/3/13 0013
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 69.py
"""shell排序"""


def shell_Sort(arr):
    n = len(arr)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            while i - step >= 0 and arr[i - step] > arr[i]:
                arr[i - step], arr[i] = arr[i], arr[i - step]
                i -= step
        step = step // 2


if __name__ == "__main__":
    ls = [1, 6, 9, 6, 3, 5, 1, 2]
    shell_Sort(ls)
    print(ls)

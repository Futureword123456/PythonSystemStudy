# -*- coding: utf-8 -*-
# @Time : 2021/3/11 0011
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 58.py
"""python线性查找指按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止。"""


# n表示总的元素个数，x表示需要查找的元素
def search(arr, n, x):
    # 1、遍历整个列表
    pos = 0
    for i in range(0, n):
        # 2、如果相等则进行返回
        if arr[i] == x:
            pos = i
        else:
            pos = -1
    return pos


if __name__ == "__main__":
    arr = [2, 3, 4, 5, 9, 6, 2, 10, 40]
    x = 40
    print(search(arr, len(arr), x))

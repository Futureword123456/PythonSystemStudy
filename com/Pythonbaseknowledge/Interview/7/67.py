# -*- coding: utf-8 -*-
# @Time : 2021/3/13 0013
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 67.py

# 排序


def merge_sort(arr):
    # 分解---递归
    # 递归
    if len(arr) == 1:
        return arr
    # m = int((l + (r - 1)) / 2)
    mid = int(len(arr) // 2)
    print(mid)
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    # 游标
    i = 0  # left
    j = 0  # right
    # 汇总的容器
    results = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j = j + 1
    results += left[i:]
    results += right[j:]
    return results


if __name__ == "__main__":
    l1 = [1, 6, 9,6,3,5,1,2]
    rest = merge_sort(l1)
    print(rest)

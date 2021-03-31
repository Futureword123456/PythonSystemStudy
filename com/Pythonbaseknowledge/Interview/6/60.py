# -*- coding: utf-8 -*-
# @Time : 2021/3/11 0011
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 60.py
"""Python 快速排序
挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面
（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
"""


def Quick(arr, low, higt):
    """快速排序"""
    i = low
    j = higt
    if low < higt:
        key = arr[low]  # 标志元素
        while i < j:
            """后面的值大于key就需要向前移动，否者就需要交换元素"""
            while i < j and key <= arr[j]:
                j = j - 1
            if i < j:
                """后面的元素j和前面的i交换"""
                arr[i] = arr[j]
                """交换后前面的i就开始往后移动"""
                i = i + 1
            """前面的i小于后面的key"""
            while i < j and key > arr[i]:
                i = i + 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
            arr[i] = key
            Quick(arr, low, i - 1)
            Quick(arr, i + 1, higt)


if __name__ == "__main__":
    lst = [5, 8, 9, 6, 2, 4, 8]
    Quick(lst, 0, len(lst) - 1)
    print(lst)

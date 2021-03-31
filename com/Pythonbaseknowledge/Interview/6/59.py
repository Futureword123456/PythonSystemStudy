# -*- coding: utf-8 -*-
# @Time : 2021/3/11 0011
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 59.py

"""Python 插入排序"""
""""(1)首先对数组的前两个数据进行从小到大的排序。

(2)接着将第3个数据与排好序的两个数据比较，将第3个数据插入到合适的位置。

(3)然后，将第4个数据插入到已排好序的前3个数据中。

(4)不断重复上述过程，直到把最后一个数据插入合适的位置。最后，便完成了对原始数组的从小

到大的排序。"""


def insertion(arr):
    """遍历整个列表"""
    for i in range(1, len(arr)):
        key = arr[i]  # 待排序的数组
        j = i - 1
        # arr[j]是已经排好序的那一小部分
        while j >= 0 and key < arr[j]:
            # 向后移动一个位置给需要插入的数据
            arr[j + 1] = arr[j]
            #
            j = j - 1
            # 插入到合适的位置
        arr[j + 1] = key


if __name__ == "__main__":
    lst = [5,8,9,6,2,4,10]
    insertion(lst)
    print(lst)
    for i in lst:
        print(i,end=" ")

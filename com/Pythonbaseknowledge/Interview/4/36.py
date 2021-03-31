# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 36.pyi

"""定义一个整型数组，并将指定个数的元素翻转到数组的尾部。"""
n = int(input("输入数字:"))
arr = [1, 2, 3, 4, 5, 6, 7]
# print(arr[0:n])
list1 = arr[0:n]
for i in range(1,n+1):
    arr.pop(0)
for j in list1:
    arr.append(j)
# print(arr)
for i in arr:
    print(i,end=" ")


# def leftRotate(arr, d, n):
#     for i in range(d):
#         leftRotatebyOne(arr, n)
#
#
# def leftRotatebyOne(arr, n):
#     temp = arr[0]
#     for i in range(n - 1):
#         arr[i] = arr[i + 1]
#     arr[n - 1] = temp
#
#
# def printArray(arr, size):
#     for i in range(size):
#         print("%d" % arr[i], end=" ")
#
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# leftRotate(arr, 2, 7)
# printArray(arr, 7)
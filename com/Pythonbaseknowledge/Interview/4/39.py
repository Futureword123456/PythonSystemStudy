# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 39.py
"""Python 翻转列表"""
l = [1, 2, 5, 9, 8]
print(l[::-1])
l.reverse()
print(l)


# print(l)
def reverse(list1):
    for i in range(1, len(list1) + 1):
        return list1[i+3::-1]


if __name__ == "__main__":
    l = [1, 2, 5, 9, 8]
    print(reverse(l))

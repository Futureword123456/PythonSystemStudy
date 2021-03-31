# -*- coding: utf-8 -*-
# @Time : 2021/3/9 0009
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 47.py
"""Python 移除字符串中的指定位置字符"""
"""可以把字符串转为列表"""


def removestring(str1, n):
    str2 = ""
    for i in range(1, len(str1) + 1):
        if i != n:
            """不等于就把剩下的加起来"""
            str2 = str2 + str1[i - 1]
    print(str2)


def removestring1(str1, n):
    lst = []
    for i in range(1,len(str1)+1):
        lst.append(i)
    lst.pop(n-1)
    for i in lst:
        print(i,end="")



if __name__ == "__main__":
    lst = "123456"
    removestring(lst, 2)
    removestring1(lst, 2)

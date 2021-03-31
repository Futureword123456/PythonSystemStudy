# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 37.py

"""Python 将列表中的头尾两个元素对调"""


def change(mylist):
    mylist[0], mylist[-1] = mylist[-1], mylist[0]
    return mylist


if __name__ == "__main__":
    list1 = [1, 5, 3, 6, 8]
    print(change(list1))

# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 38.py

"""Python 将列表中的指定位置的两个元素对调"""


def change(mylist, post1, post2):
    mylist[post1], mylist[post2] = mylist[post2], mylist[post1]
    return mylist


if __name__ == "__main__":
    l = [1,2,5,9,8]
    print(change(l,1,3))
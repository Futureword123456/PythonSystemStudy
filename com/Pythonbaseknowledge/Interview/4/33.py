# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 33.py
"""Python 约瑟夫生者死者小游戏
30 个人在一条船上，超载，需要 15 人下船。

于是人们排成一队，排队的位置即为他们的编号。

报数，从 1 开始，数到 9 的人下船。

如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
"""

mylist = [1] * 30
counter = 0  # 数到9下船
index = 0  # 表示数数的下标
downNo = 0  # 表示已经确定下船的人数
while True:
    if mylist[index] == 0:
        index += 1
        if index == 30:
            index = 0
        continue
    counter += 1
    if counter == 9:
        mylist[index] = 0
        counter = 0
        print("{}下船了".format(index + 1))
        downNo += 1
        if downNo == 15:
            break
    index += 1
    if index == 30:
        index = 0

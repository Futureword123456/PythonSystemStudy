# -*- coding: utf-8 -*-
# @Time : 2021/3/12 0012
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 66.py

"""输入三个整数x,y,z，请把这三个数由小到大输出。"""
"""思路:把三个数全部放在一个列表中，在用sort()函数直接排序后输出"""
l = []
"""只是循环三次输入"""
for _ in range(0,3):
    x = int(input("输入三个数:"))
    l.append(x)
l.sort()
for i in l:
    print(i,end=" ")

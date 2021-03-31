# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 3.py
import math
"""计算一个数的平方根和平方"""
a = float(input("输入一个数:"))
rest = math.sqrt(a)
rest1 = math.pow(a,2)
print("数{0}的开平方根是{1}".format(a,rest))
print("数{0}的平方是{1}".format(a,rest1))
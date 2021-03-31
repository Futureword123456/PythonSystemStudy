# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 4.py

"""通过用户输入数字，并计算二次方程："""
import math

a = float(input("输入a:"))
b = float(input("输入b:"))
c = float(input("输入c:"))
d = (b * b) - (4 * a * c)
if d > 0:
    x1 = (-b) + math.sqrt(d) / (2 * a)
    x2 = (-b) - math.sqrt(d) / (2 * a)
    print("结果是{0:.3f},{1:.3f}".format(x1,x2))
else:
    print("没有符合条件的数据结果")

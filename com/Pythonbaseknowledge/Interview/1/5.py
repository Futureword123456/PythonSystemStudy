# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 5.py

""""用户输入三角形三边长度，并计算三角形的面积："""
import math
try:
    a = float(input("输入a:"))
    b = float(input("输入b:"))
    c = float(input("输入c:"))
    p = (a + b + c) / 2
    area = math.sqrt((p - a) * (p - b) * (p - c))
    print("三角形的面积是{:.3}".format(area))
except Exception as e:
    print("请输入数字")



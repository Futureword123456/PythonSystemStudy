# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 9.py
"""输入两个变量，并相互交换"""

a = float(input("输入a:"))
b = float(input("输入b:"))
print("交换之前a是{}:".format(a))
print("交换之前b是{}:".format(b))
temp = a
a = b
b = temp
print("交换之后a是{}:".format(a))
print("交换之后b是{}:".format(b))

# -*- coding: utf-8 -*-
# @Time : 2021/1/7 0007 9:51
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample3.py
# 位运算符
a = 60  # 对应二进制数是00111100
b = 13  # 对应二进制数是00001101
c = 0
c = a & b
# 00001100 = 12
print(c)
c = a | b
#
print("a|b=:", c)

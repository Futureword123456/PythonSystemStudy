# -*- coding: utf-8 -*-
# @Time : 2021/1/3 0003 13:28
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample2.py
# 等值判断

if 1 != 1:
    print("1不等于1")
else:
    print("1等于")
b = 1 == 1
print(b)
print(1 == 1.0)
print("abc".lower() == "Abc".lower())
print(" abc".strip() == "abc")
print(str(1) == "1")
print(1 == int("1"))

# 数字与bool表达式的比较
print(0 == False)
print(1 == True)
if 3 - 1:
    print("成立")
else:
    print("不成立")

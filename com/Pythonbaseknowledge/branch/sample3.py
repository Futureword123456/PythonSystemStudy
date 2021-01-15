# -*- coding: utf-8 -*-
# @Time : 2021/1/3 0003 14:17
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample3.py

a = 4 > 1  # True
b = 5 < 2  # False
c = 8 == 8  # True
d = 9 < 6  # False
print(a and b)
print(a and c)
print(a or b)
print(b or d)
print(not a)
print(not b)

# 逻辑运算符优先级是not>and>or
r1 = a and b or c and not d
print(r1)  # True
r2 = (a and (not b or c)) and d
print(r2)

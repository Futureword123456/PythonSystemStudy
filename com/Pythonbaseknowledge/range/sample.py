# -*- coding: utf-8 -*-
# @Time : 2021/1/12 0012 16:33
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample.py
# 创建序列
r1 = range(10, 20)
print(r1)
print(type(r1))
# 取值
print(r1[0])
print(r1[3:6])

# 增加步长
r2 = range(10, 20, 2)
print(r2)  # 10,12,14,16,18
print(r2[4])
print(r2[0:2])
for i in range(10, 20, 2):
    print(i, end="|")

# 成员运算符In,序列中数据结构通用
print(10 in range(10, 20))
print(10 not in range(10, 20))

# 1+2+3+4+。。。。100
sum = 0
for i in range(0, 101):
    sum = sum + i
print(sum)

# -*- coding: utf-8 -*-
# @Time : 2021/3/15 0015
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 77.py
"""有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。"""
sum = 0
mid = 0
a = 2
b = 1
for _ in range(0, 21):
    sum += mid
    mid = a / b
    t = a
    a = a + b
    b = t
print(sum)
if __name__ == "__main__":
    pass

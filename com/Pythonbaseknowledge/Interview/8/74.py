# -*- coding: utf-8 -*-
# @Time : 2021/3/14 0014
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 74.py
"""一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数"""
from sys import stdout
for j in range(2, 1001):
    Tn = []
    s = j  # 总数
    n = -1  # 因子数
    for i in range(1, j):
        if j % i == 0:  # 说明i是因子
            n = n + 1
            s = s - i  # 剩余的数
            Tn.append(i)
    # print(Tn[i-1])
    # 把因子加入队列
    if s == 0:
        print(j)
        for i in range(n):
            stdout.write(str(Tn[i]))
            stdout.write(' ')
        print(Tn[n])
if __name__ == "__main__":
    pass

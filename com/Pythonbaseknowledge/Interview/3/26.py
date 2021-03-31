# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 26.py
"""递归的方式来生成斐波那契数列："""


def recur_fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


if __name__ == "__main__":
    m = int(input("请输入需要输出几项斐波那契数列:"))
    fibo = []
    for i in range(1, m + 1):
        fibo.append(recur_fibo(i))

    print("斐波那契数列是:{0}".format(fibo))

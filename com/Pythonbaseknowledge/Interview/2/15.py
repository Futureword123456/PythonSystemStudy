# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 15.py
"""质数判断:
一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），
换句话说就是该数除了1和它本身以外不再有其他的因数
"""


def alone(a):
    flag = 1
    if a > 1:
        for i in range(2, a):
            """输入的数除以一个数等于零，就说明不是质数"""
            if a % i == 0:
                flag = 0
                print("{0}不是质数".format(a))
                break
            if flag:
                print("{0}是质数".format(a))
    else:
        print("质数是大于等于一的数，请重新输入")


if __name__ == "__main__":
    a = int(input("输入a:"))
    alone(a)

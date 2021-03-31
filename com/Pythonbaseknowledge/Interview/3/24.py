# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 24.py
"""实现简单计算器实现，包括两个数基本的加减乘除运算："""


class Arithmetic(object):
    """四则运算类"""

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self, first, second):
        return first + second

    def subtract(self, first, second):
        return first - second

    def multiply(self, first, second):
        return first * second

    def divide(self, first, second):
        if second == 0:
            print("除数不能为零")
        else:
            return first / second


if __name__ == "__main__":

    first = float(input("输入第一个数:"))
    second = float(input("输入第二个数:"))
    # print("请选择运算符(+、-、*/):")
    arithmetic = Arithmetic(first,second)
    sign = input("请选择运算符(+、-、*/)")
    if sign == "+":
        print(arithmetic.add(first, second))
    elif sign == "-":
        print(arithmetic.subtract(first, second))
    elif sign == "*":
        print(arithmetic.multiply(first, second))
    elif sign == "/":
        print(arithmetic.divide(first, second))
    else:
        print("请输入正确的运算符(+、-、*、/)")

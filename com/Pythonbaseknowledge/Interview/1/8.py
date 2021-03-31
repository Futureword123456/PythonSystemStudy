# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 8.py
"""摄氏温度转华氏温度 摄氏温度c f=c*9/5+32"""


def f(c):
    rest = c * 9 / 5 + 32
    return rest


if __name__ == "__main__":
    c = float(input("输入一个摄氏温度c:"))
    print(f(c))

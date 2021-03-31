# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 23.py
import time

from Interview.utils.test_times import time_calc


@time_calc
def dfc(a, b):
    m = 1
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            m = i
    return a * b / m


if __name__ == "__main__":
    print(dfc(4, 8))

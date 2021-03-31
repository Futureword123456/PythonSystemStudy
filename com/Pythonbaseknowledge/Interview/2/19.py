# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 19.py
"""斐波那契数列:
 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：
 第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
 """


def fab(n):
    """斐波那契数列"""
    list = []  # 前面两项
    for i in range(0,n+1):
        if i <= 1:
            list.append(1)
        else:
            """最后的结果是到说2个值的和"""
            list.append(list[-2] + list[-1])
    return list


if __name__ == "__main__":
    print(fab(9))

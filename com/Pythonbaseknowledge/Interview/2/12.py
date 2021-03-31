# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 12.py

"""判断一个数字是否为奇数或偶数"""

try:
    a = int(input("输入a:"))
    if a % 2 == 0:
        print("{0}是偶数".format(a))
    else:
        print("{0}是奇数".format(a))
except Exception as e:
    print("请输入自然数")

# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 10.py

"""通过使用 if...elif...else 语句判断数字是正数、负数或零："""
a = float(input("输入a:"))
if a > 0:
    print("{}是正数".format(a))
elif a < 0:
    print("{}是负数".format(a))
else:
    print("{}是0".format(a))
if __name__ == "__main__":
    pass

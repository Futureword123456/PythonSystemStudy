# -*- coding: utf-8 -*-
# @Time : 2021/3/6 0006
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 13.py
"""用于判断用户输入的年份是否为闰年："""
try:
    year = int(input("输入年份:"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("{}是瑞年".format(year))
    else:
        print("{}不是瑞年".format(year))
except Exception as e:
    print("请输入正确是年份")

if __name__ == "__main__":
    pass

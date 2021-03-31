# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 30.py
"""Python 计算每个月天数"""
import calendar

print("Python3 实例--Python 计算每个月天数")
monthdays = calendar.monthrange(2021, 4)
print(monthdays)
# 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），
# 第二个元素是这个月的天数
# 以上实例输出的意思为 2016 年 9 月份的第一天是星期四，该月总共有 30 天。
if __name__ == "__main__":
    pass

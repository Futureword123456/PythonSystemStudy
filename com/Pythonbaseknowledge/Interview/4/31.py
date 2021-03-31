# -*- coding: utf-8 -*-
# @Time : 2021/3/8 0008
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 31.py
"""Python 获取昨天日期"""
import datetime


def getyesterday():
    days = datetime.date.today()
    """
    datetime.timedelta对象代表两个时间之间的时间差
    两个date或datetime对象相减就可以返回一个timedelta对象。
    """
    day = datetime.timedelta(days=1)
    return days-day


if __name__ == "__main__":
    print(getyesterday())
print(datetime.datetime.now())
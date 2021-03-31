# -*- coding: utf-8 -*-
# @Time : 2021/3/10 0010
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 56.py
"""Python 将字符串的时间转换为时间戳"""
import time

a1 = "2019-5-10 23:40:00"
timeArray = time.strptime(a1,"%Y-%m-%d %H:%M:%S")
print(timeArray.tm_mday)
print(timeArray)

# 转换为时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)
# 格式转换 - 转为 /
a2 = "2019/5/10 23:40:00"
"""Python time strptime() 函数根据指定的格式把一个时间字符串解析为时间元组。"""
timeArray = time.strptime(a2,"%Y/%m/%d %H:%M:%S")
"""Python time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数 format 决定。"""
othsertime = time.strftime("%Y/%m/%d %H:%M:%S",timeArray)
print(othsertime)

if __name__ == "__main__":
    pass
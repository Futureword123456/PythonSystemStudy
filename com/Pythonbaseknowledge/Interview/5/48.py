# -*- coding: utf-8 -*-
# @Time : 2021/3/9 0009
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 48.py
"""Python 判断字符串是否存在子字符串"""


def check(string, sub_str):
    """find()等于-1表示不存在,等于2表示存在"""
    if string.find(sub_str) == 2:
        print("存在")
    else:
        print("不存在")


if __name__ == "__main__":
    string = "abcdefg"
    sub_str = 'ced'
    check(string, sub_str)

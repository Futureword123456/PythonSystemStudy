# -*- coding: utf-8 -*-
# @Time : 2021/3/9 0009
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 50.py
import re

""" 使用正则表达式提取字符串中的 URL"""


def Find(str):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
    return url


if __name__ == "__main__":
    str1 = "长江大学 https://www.runoob.com/python3/ uyasvd"
    print(Find(str1))

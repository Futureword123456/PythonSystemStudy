# -*- coding: utf-8 -*-
# @Time : 2021/1/25 0025
# @Author : yang
# @Email : 2635681517@qq.com
# @File : use_group.py
import re


def test_group():
    content = 'hello, world'
    patten = re.compile(r'world')
    rest = patten.search(content)
    print(rest)
    if rest is not None:
        print(rest.group())
        # groups的使用
        print(rest.groups())


def test_idCard():
    """"身份证正则匹配"""
    # p = re.compile(r'(\d{6})(\d{4})(\d{2})(\d{2})(\d{2})(\d{1})([0-9]|X)')
    p = re.compile(r'(\d{6})(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})(\d{2})(?P<sex>\d{1})([0-9]|X)')
    # 两个身份证号码
    id1 = '52232819981209491X'
    id2 = '522328199812094936'
    rest1 = p.search(id1)
    print(rest1.group(7))
    print(rest1.groups())
    # groupdict
    print(rest1.groupdict())



if __name__ == "__main__":
    test_idCard()

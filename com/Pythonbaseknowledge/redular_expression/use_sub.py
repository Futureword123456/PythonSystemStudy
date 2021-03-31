# -*- coding: utf-8 -*-
# @Time : 2021/1/25 0025
# @Author : yang
# @Email : 2635681517@qq.com
# @File : use_sub.py
import re

"""使用正则表达式进行替换
replace
"""
s = 'one1tow28three3154four4five'
p = re.compile(r'\d+')
rest = p.sub("#", s)
print(rest)

rest1 = s.replace('1', "#").replace('28', "@")
print(rest1)
# 使用正则表达式更换
s2 = 'hello world'
p2 = re.compile(r'(\w+) (\w+)')
print(p2.groups)
result = p2.sub(r'\2 \1', s2)
print(result.upper())


# 替换并改变内容
# def f(m):
#     return m.group(2).upper()+ m.group(1)
#
#
# rest_change = p2.sub(f, s2)
# print(rest_change)

if __name__ == "__main__":
    pass

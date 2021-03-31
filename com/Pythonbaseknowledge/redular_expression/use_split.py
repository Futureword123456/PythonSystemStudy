# -*- coding: utf-8 -*-
# @Time : 2021/1/25 0025
# @Author : yang
# @Email : 2635681517@qq.com
# @File : use_split.py
import re
"""
使用split分割
"""
s = 'one1tow28three3154four4five'
p = re.compile(r'\d+')
rest = p.split(s)
print(rest)
if __name__ == "__main__":
    pass

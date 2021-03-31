# -*- coding: utf-8 -*-
# @Time : 2021/1/25 0025
# @Author : yang
# @Email : 2635681517@qq.com
# @File : use_findall.py
import re

content = 'one1tow2three3four4five5six8seven8eight6nine651'
# 只需要找出一下字符串中的数字
p = re.compile(r'[a-z]+', re.I)
rest = p.findall(content)
print(rest)

# 不编译
all_result = re.findall(r'[a-z]+', content, re.I)
print(all_result)

if __name__ == "__main__":
    pass

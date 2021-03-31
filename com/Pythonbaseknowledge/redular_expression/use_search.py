# -*- coding: utf-8 -*-
# @Time : 2021/1/25 0025
# @Author : yang
# @Email : 2635681517@qq.com
# @File : use_search.py
import re

content = 'hello world'
# 使用search
p = re.compile(r'world')
rest = p.search(content)
print(rest.group())

rest_match = p.match(content)
print(rest_match)

# 使用函数进行调用
rest_fun = re.search(r'world', content)
print(rest_fun)

if __name__ == "__main__":
    pass

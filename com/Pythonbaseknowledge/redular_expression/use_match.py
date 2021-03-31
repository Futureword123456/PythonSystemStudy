# -*- coding: utf-8 -*-
# @Time : 2021/1/25 0025
# @Author : yang
# @Email : 2635681517@qq.com
# @File : use_match.py
import re

# 将正则表达式编译
patten = re.compile(r'hello', re.I)
print(dir(patten))
print(patten.findall('hello'))
# 通过match进行匹配
rest = patten.match('Hello world!')
print(rest)

print("===================================")
print(dir(rest))
print('string:', rest.string)
print('re:', rest.re)
print('groups:', rest.groups())

if __name__ == "__main__":
    pass

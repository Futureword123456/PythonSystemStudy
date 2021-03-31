# -*- coding: utf-8 -*-
# @Time : 2021/3/9 0009
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 49.py
"""计算字符串的长度"""


def leng(string1):
    count = 0
    for _ in string1:
        count = count + 1
    return count
    print(count)


def leng1(string1):
    rest = 0
    for i in range(1, leng(string1) + 1):
        rest = rest + 1
    print(rest)


string1 = 'yang '
print(len(string1))
if __name__ == "__main__":
    string1 = 'yang  '
    # leng(string1)
    leng1(string1)

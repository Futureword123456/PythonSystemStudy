# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 8:52
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample2.py
# 利用range遍历其他序列
c = 'abcdefg'
for i in range(0, len(c)):
    letter = c[i]  # 字符串的提取用中括号[]
    print(letter, end="|")

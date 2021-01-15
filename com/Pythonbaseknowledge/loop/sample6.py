# -*- coding: utf-8 -*-
# @Time : 2021/1/5 0005 17:39
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample6.py
# 查找100以内的质数
j = 2
while j <= 1000:
    num = j
    i = 2
    is_prime = True  # 标识当前数值是否是质数
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i = i + 1
    if is_prime:
        print("{}是质数".format(num))
    j = j + 1

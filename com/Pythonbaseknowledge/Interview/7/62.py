# -*- coding: utf-8 -*-
# @Time : 2021/3/11 0011
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 62.py
num = input("输入一个数:")
results = ['是回文数', '不是回文数', '输入的不是数字']
result = ''
if num.isdigit():
    num = str(num)
    for i in range(len(num) // 2):
        if num[i] == num[len(num) - i - 1]:
            continue
        else:
            print(num, results[1])
            result = results[1]
        break
    if result != results[1]:
        print(num, results[0])
else:
    print(results[2])


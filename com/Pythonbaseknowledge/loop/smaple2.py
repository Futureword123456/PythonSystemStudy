# -*- coding: utf-8 -*-
# @Time : 2021/1/5 0005 10:37
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : smaple2.py
# 阶乘计算器
num = input("请输入要计算的数值（1-100）：")
num = int(num)
if 1 <= num <= 100:
    i = 1
    result = 1
    while i <= num:
        #print(i)
        result = result * i
        if i % 5 == 0:
            # print(str(i)+":"+str(result))
            print("{}:{}".format(i, result))
        i = i + 1
        # 不使用缩进的代码代表while循环后继续执行语句
    print("最总结果{}".format(result))
else:
    print("请输入1-100有效数字")

# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 9:05
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample4.py
# 如何判断质数
result = []
while True:
    num = input("请输入一个整数(输入0结束程序):")
    prime = True
    for i in range(2, int(num)):
        print(i)
        if int(num) % i == 0:
            prime = False
            break
    if prime == True:
        print("{}是质数".format(num))
        result.append("{}".format(num))
        print("质数列表:{}".format(result))
    else:
        print("{}不是质数".format(num),end="|")
    if num == '0':
        break

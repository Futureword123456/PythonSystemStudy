# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 9:57
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample5.py

result = []
for j in range(2,1000):
    #num = input("请输入一个整数(输入0结束程序):")
    prime = True
    for i in range(2, int(j)):
        #print(i)
        if int(j) % i == 0:
            prime = False
            break
    if prime == True:
        print("{}是质数".format(j))
        result.append("{}".format(j))
        print("质数列表:{}".format(result))
    else:
        print("{}不是质数".format(j),end="|")


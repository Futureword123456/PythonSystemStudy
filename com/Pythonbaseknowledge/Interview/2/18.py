# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 18.py

""" 九九乘法表"""
for i in range(1,10):
    for j in range(1,i+1):
        print("{0}*{1}={2}".format(i,j,i*j),end=' ')
    print()
if __name__ == "__main__":
    pass
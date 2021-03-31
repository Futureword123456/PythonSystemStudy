# -*- coding: utf-8 -*-
# @Time : 2021/3/15 0015
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 76.py
"""
打印出如下图案（菱形）:

   *
  ***
 *****
*******
 *****
  ***
   *
"""
from sys import stdout

for i in range(0,4):
    # 1、控制空格
    for j in range(0,2-i+1):
        stdout.write(' ')
    # 2、控制*号
    for j in range(0,2*i+1):
        stdout.write('*')
    print('')
for i in range(0,3):
    for j in range(0,i+1):
        stdout.write(' ')
    for j in range(0,4-2*i+1):
        stdout.write('*')
    print('')
if __name__ == "__main__":
    pass
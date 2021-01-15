# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 9:00
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample3.py
# 斐波那契额数列

# 1,1,2,3,4,8,13.....
result = []
for i in range(0, 50):
    if i == 0 or i == 1:
        result.append(1)
    else:
        result.append(result[i - 2] + result[i - 1])
print(result)

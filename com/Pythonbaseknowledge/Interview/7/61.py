# -*- coding: utf-8 -*-
# @Time : 2021/3/11 0011
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 61.py
"""有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？"""
count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print("数是:{0}{1}{2}".format(i, j, k))
                count = count + 1
print(count)
if __name__ == "__main__":
    pass

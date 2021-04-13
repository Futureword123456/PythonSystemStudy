# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 0011 20:39
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : numpyTest1.py
# @Software: PyCharm
import numpy as np

# [3,4]表示3行4列
lst = np.arange(1, 13).reshape([3, 4])
print(lst)
print(np.arange(1, 13))
from numpy.linalg import *

# print(np.eye(3))
lst = np.array([[1, 2, 5], [4, 5, 6], [5, 9, 6]])
print(lst)
print("inv:")
print(inv(lst))
print('T:')
print(lst.transpose())
print("Det:")
print(det(lst))
print(eig(lst))
# y = np.array([5, 6.], [2, 6.])
# print(solve(lst, y))
print("FFT:")
print(np.fft.fft(np.array([1, 1, 1, 1, 1, 1, 1, ])))
print(np.corrcoef([1, 0, 1], [0, 2, 1]))  # 皮尔逊相关系数计算
print(np.poly1d([3, 1, 3]))  # 生成一元多次函数

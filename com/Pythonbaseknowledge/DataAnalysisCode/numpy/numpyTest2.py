# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 0012 9:32
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : numpyTest2.py
# @Software: PyCharm
import numpy as np
from numpy.matrixlib import mat

lst = [1, 2, 3, 4, 5]
print(lst)
# 创建一维的数组
array_1 = np.array(lst)
print(array_1)
lst2 = [5, 6, 7, 8, 6]
array_2 = np.array([lst, lst2])
print("二维数组：")
print(array_2)
# shape返回数组的属性
print("shape:", array_2.shape)
# 元素个数
print(array_2.size)
# 元素数据类型
print(array_2.dtype)
array_3 = np.array([[1.0, 2, 3], [4.0, 5, 6]])
print(array_3)
print(array_3.dtype)
# 创建array
array_4 = np.arange(1, 10, 2)
print(array_4)
# 创建全0的矩阵
print("创建全0的矩阵:")
print(mat(np.zeros([2, 5])))
print(np.zeros([2]))
print("单位矩阵：")
print(np.eye(3))
print(np.eye(5).dtype)
a = np.arange(1, 10)
print(a)
# 不包含前面包含后面
print("a[0:5]", a[0:5])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(b)
print(b[1][2])

c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 5]])
print(c)
print(c[1][3])

print("创建随机数组")
print("随机正态分布：")
print(np.random.randn(10))
print("随机10以内数据:")
print(np.random.randint(10))
print("随机的一维数组：")
print(np.random.randint(10, size=10))
print(np.random.randint(10, size=10).reshape(2, 5))
a = np.random.randint(10, size=10).reshape(2, 5)
b = np.random.randint(10, size=10).reshape(2, 5)
print(a)
print(b)
print("数组的加法：")
print(a + b)
print("数组的减法：")
print(a - b)
print(a * b)
# print(a/b)
print("mat：")
print(np.mat([[1, 2, 3], [4, 5, 6]]))

a = np.random.randint(10, size=10).reshape(2, 5)
b = np.random.randint(10, size=10).reshape(2, 5)
print(a)
print(b)
A = np.mat(a)
print(type(a))
print(type(A))
B = np.mat(b)

print(b)
print(A + B)
print("unique:")
print("元组中唯一原始是:", np.unique(a))

print(a)
print("所有元素的和:", sum(a))
print("行的元素和是：", sum(a[1]))
print("列的元素和是:", sum(a[:, 1]))
print(a.max())
print(max(a[1]))

print("序列化:")
import pickle

x = np.arange(10)
print(x)
# 把随机产生的元组保存到本地
f = open('x.pkl', 'wb')
pickle.dump(x, f)
print(pickle.load(f))
print(np.save('one_array', x))

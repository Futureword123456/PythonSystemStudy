# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 0012 21:25
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : reindex.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Series的index
s1 = Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
print(s1)
s2 = s1.reindex(index=['A', 'B', "C", 'D', 'E'], fill_value=10)
print(s2)
s3 = Series(['A', 'B', 'C'], index=[1, 5, 10])
print(s3)
s4 = s3.reindex(index=range(15), method='ffill')
print(s4)

df1 = DataFrame(np.random.rand(25).reshape([5, 5]), index=['A', 'B', 'D', 'E', 'F'],
                columns=['c1', 'c2', 'c3', 'c4', 'c5'])
print(df1)
df2 = df1.reindex(index=['A', 'B', 'C', 'D', 'E', 'F'])
print('df2:', df2)
df3 = df2.reindex(columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6'])
print(df3)

s5 = s1.reindex(index=['A', 'B'])
print(s5)

df4 = df1.reindex(index=['A', 'C'])
print("df4:", df4)
print("drop:")

s6 = s1.drop('C')
print(s6)

df5 = df1.drop(index='B')
print(df1)
print(df1.drop(columns=['c2', 'c5']))
print("df5:", df5)
print(df1.drop(['E', 'D'], axis=0))

# df6 = df1.drop('B', axis=0)
# print(df6)

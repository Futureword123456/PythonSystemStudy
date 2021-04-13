# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 0013 10:26
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : NaN.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s = pd.Series([1, 2, np.nan, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
s1 = s.reindex(index=['A', 'B', 'C', 'D', 'E'])
print(s)
print(s1.isnull())
# 删除nan
print(s.dropna())

df = DataFrame([[1, 3, 5], [np.nan, np.nan, 4], [np.nan, 8, np.nan], [7, np.nan, 9]])
print(df)
print(df.notnull())
# axis=0表示只要在一行里面存在0的都会被删除
# how='all'表示一行里面都是NaN才会删除
# how='any'表示一行里面存在NaN就会删除
df1 = df.dropna(axis=0,how='any')
print(df1)

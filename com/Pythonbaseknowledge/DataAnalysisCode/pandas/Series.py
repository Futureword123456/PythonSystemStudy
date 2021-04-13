# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 0012 10:47
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : Series.py
# @Software: PyCharm
import numpy as np
import pandas as pd

n1 = pd.Series([[5, 6, 7, 8], [1, 2, 3, 4]])
print(n1)
print('n1.values',n1.values)
print('n1.index',n1.index)
n2 = pd.Series(np.arange(10))
print(n2)
n3 = pd.Series({"1": 1, '2': 2, "3": 3})
print(n3)
print(n3.values)
print(n3.index)

n4 = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
print(n4)
print(n4.values)
print(n4.index)

print(n4[n4 > 2])
print(n4.to_dict())
index_1 = ['A', 'B', 'C', 'D', 'E']
n5 = pd.Series(n4, index=index_1)
print(n5)
print(pd.isnull(n5))
print(pd.notnull(n5))
n5.name = 'demo'


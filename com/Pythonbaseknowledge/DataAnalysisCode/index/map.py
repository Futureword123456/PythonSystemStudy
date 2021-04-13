# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 0013 14:21
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : map.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df1 = DataFrame({'城市': ['北京', '上海', '广州'], '人口': [1000, 1500, 2000]})
print(df1)
df1['GDP'] = Series([1000, 6000, 4500])
print(df1)

gdp_map = {'北京': 1000, '上海': 2000, '广州': 5000}
print(gdp_map)
df1['GDP'] = df1['城市'].map(gdp_map)
print(df1)

s1 = Series(np.arange(10))
s2=s1.replace({1:np.nan})
s3 = s1.replace([1,2,3],[10,20,30])
print(s3)

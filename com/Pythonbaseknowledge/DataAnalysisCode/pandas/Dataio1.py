# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 0012 16:18
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : Dataio1.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = pd.read_excel('Data.xlsx')
# df5 = df.head()
df5 = df
df5.to_csv("df5.csv")
# print(df5)
# # df5 = pd.read_csv('df5.csv')
# # print(df5)
# df0 = df5[['employee_no', 'real_name']]
# print(df0)


sub_df = df5[['employee_no', 'real_name', 'employee_unit']]
# print(sub_df)
# sub = sub_df.iloc[2:6, 0:3]
# print(sub)
# print(sub.loc[3:3,:'real_name'])
s = sub_df.loc[3:8, :]
print(s)

s1 = s.loc[7:7, :]
# s2 = s1.loc[7:7, :]
print(s1['employee_unit'])

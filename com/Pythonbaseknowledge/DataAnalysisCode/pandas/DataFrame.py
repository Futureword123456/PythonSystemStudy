# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 0012 14:53
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : DataFrame.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = pd.read_excel(r'Data.xlsx')
print(type(df))
# 获取列
print(df.head())
print(df.columns)
print(df.give_workld)
print("操作数据:")
df_new = DataFrame(df, columns=['employee_no', 'real_name', 'give_workld'])
print(df_new)
# 有汉字处理方法
print(df['real_name'])
df_new = DataFrame(df, columns=['employee_no', 'real_name', 'give_workld', 'study'])
print(df_new)
# 给空值赋值
df_new['study'] = range(1, 10)
print(df_new)

df_new['study'] = np.arange(1, 10)
print(df_new)

df_new['study'] = pd.Series(np.arange(1, 10))
print(df_new)
# 填充空格

df_new['study'] = pd.Series([100, 200], index=[1, 2])
print(df_new)

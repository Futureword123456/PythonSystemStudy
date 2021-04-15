# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 0015 14:23
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : 分组和透视功能实战.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('../homework/usa_flights.csv')
# 获取厌恶时间最长top10
df.sort_values('arr_delay', ascending=False)
print(df[:10])
"""计算延误和未延误所占比例
"""
s1 = df['cancelled'].value_counts()
print(s1)

df['delayed'] = df['arr_delay'].apply(lambda x: x > 0)
print(df)
delayed = df['delayed'].value_counts()
print(delayed[1] / (delayed[0] + delayed[1]))

"""每个航空公司延误情况
"""
delay_group = df.groupby(['unique_carrier', 'delayed'])
df_delay = delay_group.size().unstack()
print(df_delay)
import matplotlib.pyplot as plt
df_delay.plot(kind='barh',stacked=True,figsize=[16,6],colormap='winter')
plt.show()
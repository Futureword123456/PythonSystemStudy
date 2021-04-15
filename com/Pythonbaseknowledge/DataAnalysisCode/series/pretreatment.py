# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 0014 11:02
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : pretreatment.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
import matplotlib.pyplot as plt

"""# 通过apply进行数据的预处理"""
# print("通过apply进行数据的预处理:")
# df = pd.read_csv('../homework/apply_demo.csv')
# print(df.head())
#
# print(df.size)
# # 产生7978个a
# s1 = Series(['a'] * 7978)
# print(s1)
# # 把a添加到df中并且标签是A
# df['A'] = s1
# print(df.head())
# # print(s2)
# # 把a全部转化为A
# df1 = df['A'].apply(str.upper)
# # 把转换后的A 放在DateFrame后面
# df['A'] = df1
# print(df.head())
#
# ls = df['data'][0].strip().split(' ')
# ls1 = df.loc[0:0, :]
# l0 = list(ls1['data'])
# l2 = []
# for i in l0:
#     s = i.split(' ')
#     s = s[1:len(s)]
#     print(s)
#     # l2.append(i.split(' '))
# # print(l2)
# print(ls)
#
#
# #
# #
# def foo(line):
#     items = line.strip().split(" ")
#     return Series([items[1], items[3], items[5]])
#
#
# #
# df_item = df['data'].apply(foo)
# print('df_item', df_item)
# df1 = df_item.rename(columns={0: 'Symbol', 1: 'Seqno', 2: 'Price'})
# print('df1.head()', df1.head())
# df_new = df1.combine_first(df)
#
# del df_new['data']
# del df_new['A']
# print(df_new.head())
# df_new.to_csv('df_new.csv')

""" 数据的清理,去除重复"""
# print('数据的清理')
# df = pd.read_csv('df_new.csv')
#
# del df['Unnamed: 0']
# print(df.head())
# print(len(df['Seqno'].unique()))
# # 查看重复值
# print(df['Seqno'].duplicated())
# # 删除重复值
# print(df['Seqno'].drop_duplicates())
# # 删除重复行
# print(df.drop_duplicates(['Seqno'],keep='last'))
"""# 时间序列操作基础"""
# print('时间序列操作基础:')
# t1 = datetime(2020, 2, 14)
# print(t1)
# date_list = [
#     datetime(2020, 2, 14),
#     datetime(2018, 3, 14),
#     datetime(2018, 8, 19),
#     datetime(2016, 7, 24),
#     datetime(2019, 2, 4),
#     datetime(2010, 5, 9),
# ]
# print(date_list)
# s1 = Series(np.random.randn(6), index=[date_list])
# print(s1)
# print(s1[1])
# print(s1[datetime(2018, 3, 14)])
# date_list_new = pd.date_range('2016-1-1', periods=100, freq='5h')
# s2 = Series(np.random.randn(100),index=date_list_new)
# print(s2)
# print(date_list_new)
"""# 时间序列数据的采样和画图"""
# print("时间序列数据的采样和画图:")
# t_range = pd.date_range('2016-1-1', '2016-12-31')
# # print(t_range)
# s1 = Series(np.random.randn(len(t_range)), index=t_range)
# # 计算平均值
# print(s1['2016-01'].mean())
# # 按月计算每个月的平均值
# s1_month = s1.resample('M').mean()
# print(s1_month)
# s1_honor = s1.resample('H').ffill()
# print(s1_honor)
#
"""画图"""
# t_range = pd.date_range('2016-1-1', '2016-12-31', freq='H')
# stock_df = DataFrame(index=t_range)
#
# stock_df['ALIBB'] = np.random.randint(80, 160, size=len(t_range))
# stock_df['TENXUN'] = np.random.randint(30, 100, size=len(t_range))
#
# print(stock_df.head())
#
# weekly_df = DataFrame()
# weekly_df['ALIBB'] = stock_df['ALIBB'].resample('W').mean()
# weekly_df['TENXUN'] = stock_df['TENXUN'].resample('W').mean()
# print(weekly_df)
#
# weekly_df.plot()
# plt.show()


""" 数据分箱技术Binning"""
# print(' 数据分箱技术Binning:')
# print('Series分')
# # 产生数据
# score_list = np.random.randint(30, 100, size=20)
# print(score_list)
# # 分箱间隔i
# bins = [0, 59, 70, 80, 100]
# # 得到一个分割后的对象
# score_cut = pd.cut(score_list, bins)
# print(score_cut)
# # 取出每个对象的有的人数
# conut = pd.value_counts(score_cut)
# print(conut)
#
# df = DataFrame()
# df['score'] = score_list
# df['student'] = [pd.util.testing.rands(3) for i in range(20)]
# df['Categories'] = pd.cut(df['score'], bins, labels=['LOW', 'OK', 'GOOD', 'GREAT'])
#
# print(df)

"""数据分组技术GroupBy"""
# print("数据分组技术GroupBy:")
# df = pd.read_csv('../homework/city_weather.csv')
# print(df)
# g = df.groupby(df['city'])
# print(g.describe())
# print(g.agg('max'))
# # print(g.groups)
# # print('g.get_group', g.get_group('BJ'))
# #
# bj = g.get_group('BJ')
# print('bj.mean():', bj.mean())
# print(g.mean())
# print(g.min())
# print(g.max())
# print(dict(list(g))['BJ'])
# for name, group_df in g:
#     print(name, group_df)

"""4-12 数据聚合技术Aggregation"""

# def foo(x):
#     return x.max() - x.min()
#
#
# print(g.agg(foo))
# print(g)


""" 4-13 透视表"""
df = pd.read_excel('../homework/sales-funnel.xlsx')
df.to_csv('sales-funnel.csv')
print(df.head())
# 生成一个透视表
print(pd.pivot_table(df, index=['Manager', 'Rep'], values=['Price', 'Quantity'], fill_value=0, columns=['Product'],
                     aggfunc='sum'))

# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 0013 14:40
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : Series_nad_pandas.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#
# s1 = Series([1, 2, 3], index=['A', 'B', 'C'])
# s2 = Series([5, 6, 4, 8], index=['B', 'C', 'D', 'E'])
# print(s1 + s2)
# print(s2)
# print(s1)
#
# print('DataFrame:')
# df1 = DataFrame(np.arange(4).reshape([2, 2]), index=['A', 'B'], columns=['北京', '上海'])
# print(df1)
# df2 = DataFrame(np.arange(9).reshape([3, 3]), index=['A', 'B', 'C'], columns=['北京', '上海', '广州'])
# print(df2)
# print(df1 + df2)
# df3 = DataFrame([[1, 2, 3], [4, 5, np.nan], [np.nan, 8, np.nan]], index=['A', 'B', 'C'], columns=['c1', 'c2', 'c3'])
# print(df3)
# # 默认求列的和
# print(df3.sum())
# # 求行的和
# print(df3.sum(axis=1))
# #
# print(df3)
# print(df3.min())
# # 行的最小值
# print(df3.min(axis=1))
# print(df3.describe())
#
# print('Series的排序')
# s1 = Series(np.random.randn(10))
# print(s1)
# print(s1.values)
# print(s1.index)
# s2 = s1.sort_values(ascending=False)
# print(s2)
# s3 = s1.sort_index()
# print(s3)
#
# print('DataFrame排序：')
# df = DataFrame(np.random.randn(40).reshape([8, 5]), columns=['A', 'B', 'C', 'D', 'E'])
# print(df)
# print(df['A'].sort_index())
# print(df.sort_values('A'))
# #作业
# csv_input = '../homework/movie_metadata.csv'
# csv = pd.read_csv(csv_input)
# print(csv[['movie_title', 'director_name', 'imdb_score']].sort_values('imdb_score',ascending=False).to_csv('imdb.csv'))
# # DataFrame重命名
# df1 = DataFrame(np.arange(9).reshape([3, 3]), index=['BJ', 'SH', 'GZ'], columns=['A', 'B', 'C'])
# print(df1)
"""# # 重命名"""
# print(df1.rename(index=str.lower, columns=str.lower))
# df2 = df1.rename(index={'BJ': 'beijing'}, columns={"A": 'a'})
# print(df2)
# lst = [1, 2, 3, 4]
# lst1 = ['1', '2', '3', '4']
# # 列表解析把lst = [1,2,3,4]直接转换为lst1 = ['1', '2', '3', '4']
# lst2 = [str(x) for x in lst]
# print(lst2)
#
# lst3 = list(map(str, lst))
# print(lst3)
#
#
# def test_map(x):
#     return x + '_ABC'
#
#
# print(df1.index.map(test_map))
# print(df1.rename(index=test_map,columns=test_map))
"""#
# # DataFrame的merger操作"""
# df1 = DataFrame({'key': ['X', 'Y', 'Z', 'X'], 'value1': [1, 2, 3, 4]})
# print(df1)
# df2 = DataFrame({'key': ['X', 'B', 'C'], 'value2': [4, 5, 6]})
# print(df2)
# print(pd.merge(df1, df2, on='key'))
# # print(pd.merge(df1, df2, on='value1'))
# print(pd.merge(df1, df2, on='key', how='inner'))
# print(pd.merge(df1, df2, on='key', how='left'))
# print(pd.merge(df1, df2, on='key', how='right'))
# print(pd.merge(df1, df2, on='key', how='outer'))

"""# Concatenate和Combine"""
# print("Concatenate和Combine:")
# arr1 = np.arange(9).reshape([3, 3])
# arr2 = np.arange(9).reshape([3, 3])
# # axis=1链接到行(结果会增加列)，axis=0链接到列
# arr3 = np.concatenate([arr1, arr2], axis=1)
# print(arr3)
# s1 = Series([1, 2, 3], index=['X', 'Y', 'Z'])
# s2 = Series([4, 5, 6], index=['A', 'B', 'C'])
# print(pd.concat([s1, s2], axis=1))
# df1 = DataFrame(np.random.randn(9).reshape([3, 3]), columns=['A', 'B', 'C'], index=['A', 'B', 'C'])
# print(df1)
# df2 = DataFrame(np.random.randn(9).reshape([3, 3]), columns=['A', 'B', 'X'], index=['A', 'B', 'X'])
# print(df2)
# print(pd.concat([df1, df2]))
print('Combine:')
s1 = Series([2, np.nan, 5, np.nan], index=['A', 'B', 'C', 'D'])
s2 = Series([7, 6, 5, np.nan], index=['X', 'Y', 'Z', 'M'])
print(s1)
print(s2)
print(s1.combine_first(s2))
df1 = DataFrame({
    'X': [4, np.nan, 5],
    'Y': [5, 9, 4],
    'Z': [np.nan, 8, 4]
})

df2 = DataFrame({
    'A': [np.nan, 5, 5],
    'B': [5, 9, 4],
})
print(df1)
print(df2)
print(df1.combine_first(df2))

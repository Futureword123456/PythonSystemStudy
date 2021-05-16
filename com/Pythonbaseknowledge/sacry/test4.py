# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 0026 16:20
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : test4.py
# @Software: PyCharm

import pandas as pd
from io import StringIO

# csv_data = '''A,B,C,D
# 1,2,3,4
# 5,6,,8
# 0,11,12,'''
#
# df = pd.read_csv(StringIO(csv_data))
# print(df)
#
#
# # axis=0 列  axis = 1 行
#
# #
# df = pd.DataFrame([['green', 'M', 10.1, 'class1'],
#                    ['red', 'L', 13.5, 'class2'],
#                    ['blue', 'XL', 15.3, 'class1']])
# df.columns = ['color', 'size', 'price', 'classlabel']
# print(df)
# #
# size_mapping = {'XL': 3, 'L': 2, 'M': 1}
# df['size'] = df['size'].map(size_mapping)
# print(df)
#
# ## 遍历Series
# for idx, label in enumerate(df['classlabel']):
#     print(idx, label)
#
# # 1, 利用LabelEncoder类快速编码,但此时对color并不适合,
# # 看起来,好像是有大小的
# from sklearn.preprocessing import LabelEncoder
#
# class_le = LabelEncoder()
# color_le = LabelEncoder()
# df['classlabel'] = class_le.fit_transform(df['classlabel'].values)
# # df['color'] = color_le.fit_transform(df['color'].values)
# print(df)
#
# # 2, 映射字典将类标转换为整数
# import numpy as np
#
# class_mapping = {label: idx for idx, label in enumerate(np.unique(df['classlabel']))}
# df['classlabel'] = df['classlabel'].map(class_mapping)
# print('2,', df)
#
# # 3,处理1不适用的
# # 利用创建一个新的虚拟特征
# from sklearn.preprocessing import OneHotEncoder
#
# pf = pd.get_dummies(df[['color']])
# df = pd.concat([df, pf], axis=1)
# df.drop(['color'], axis=1, inplace=True)
# print(df)

import pandas as pd
import numpy as np

df = pd.DataFrame({'key1': list('aabba'), 'key2': ['one', 'two', 'one', 'two', 'one'], 'data1': np.random.randn(5),
                   'data2': np.random.rand(5)})
print(df)

df.groupby('key1')[['data1']]
### 得到一个groupby的对象，用list取出：
df_list = list(df.groupby('key1')[['data1']])
print(df_list)

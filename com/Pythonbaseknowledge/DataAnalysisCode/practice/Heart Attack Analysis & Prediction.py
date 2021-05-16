# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 0016 15:32
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : Heart Attack Analysis & Prediction.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

for dirname, _, filename in os.walk('data'):
    for filename in filename:
        print(os.path.join(dirname, filename))

df_heart = pd.read_csv('data/heart.csv')
df_heart.name = 'Heart DF'


# print(df_heart.head())
# print(df_heart.info())
# print(df_heart.describe())


def get_shape(df):
    df_name = df.name
    print('Shape of {} is{}'.format(df_name, df.shape))


get_shape(df_heart)

df_o2Saturation = pd.read_csv('data/o2Saturation.csv')
df_o2Saturation.name = 'o2Saturation DF'
print(df_o2Saturation.head())
get_shape(df_o2Saturation)
"""分组统计性别是数量"""
print(df_heart['sex'].value_counts())
df_heart['sex'] = df_heart['sex'].astype('object', copy=False)
print(df_heart['cp'].unique())

print(df_heart['fbs'].value_counts())
print(df_heart['restecg'].value_counts())
print(df_heart['exng'].value_counts())

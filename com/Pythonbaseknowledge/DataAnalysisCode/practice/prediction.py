# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 0016 16:20
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : prediction.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
# understanding data
df = pd.read_csv('data/heart.csv')
print(df.shape)
"""Preview of the first 5 rows of the data"""

print(df.head())
"""Checking the number of unique values in each column"""
dict = {}
for i in list(df.columns):
    dict[i] = df[i].value_counts().shape[0]
counts = pd.DataFrame(dict, index=['unique count']).transpose()
print(counts)
cat_cols = ['sex', 'exng', 'caa', 'cp', 'fbs', 'restecg', 'slp', 'thall']
con_cols = ["age", "trtbps", "chol", "thalachh", "oldpeak"]
"""Separating the columns in categorical and continuous"""
print(con_cols)
print(df[con_cols].describe().transpose())

"""missing values 查看缺失值"""
print(df.isnull().sum())
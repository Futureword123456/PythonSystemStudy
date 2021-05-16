# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 0025 16:17
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : test1.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from IPython.display import display
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Arial']})

# 检查Python版本
from sys import version_info
if version_info.major != 3:
    raise Exception('请使用Python 3 来完成此项目')

lianjia_df = pd.read_csv('lianjia.csv')
print(lianjia_df.info())
print(lianjia_df.describe())


df = lianjia_df.copy()



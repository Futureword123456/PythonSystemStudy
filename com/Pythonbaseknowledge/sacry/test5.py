# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 0028 9:55
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : test5.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
excel_file_path = 'paper_publish.xls'
new_df = pd.read_excel(excel_file_path)
columns = ['employee_no', 'publish_time']
df = pd.DataFrame(new_df, columns=columns)
publish_time_list = []
for pub_time_list in list(df['publish_time']):
    publish_time_list.append((pub_time_list[0:7]))
df['publish_time'] = publish_time_list
df1 = df.groupby('publish_time').first().reset_index()
df2 = df.groupby('publish_time')['employee_no'].count().to_frame().reset_index()
df2.rename(columns={"employee_no": "nums"}, inplace=True)
df3 = df2.drop([0], axis=0)
print(df3)
train = df3[0:100]
test = df3[100:]

test['publish_time'] = pd.to_datetime(test['publish_time'], format='%Y-%m')
test.index = test['publish_time']
test = test.resample('M').mean()

train['publish_time'] = pd.to_datetime(train['publish_time'], format='%Y-%m')
train.index = train['publish_time']
train = train.resample('M').mean()

train.nums.plot(figsize=(15, 8), title='month', fontsize=14)
test.nums.plot(figsize=(15, 8), title='month', fontsize=14)
plt.show()



# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 0028 14:49
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : test6.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
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
train = df3[0:100]
test = df3[100:]
print(df3)



# y_hat_avg = test.copy()
# fit1 = sm.tsa.statespace.SARIMAX(train.Count, order=(2, 1, 4), seasonal_order=(0, 1, 1, 7)).fit()
# y_hat_avg['SARIMA'] = fit1.predict(start="2013-11-1", end="2013-12-31", dynamic=True)
# plt.figure(figsize=(16, 8))
# plt.plot(train['Count'], label='Train')
# plt.plot(test['Count'], label='Test')
# plt.plot(y_hat_avg['SARIMA'], label='SARIMA')
# plt.legend(loc='best')
# plt.show()
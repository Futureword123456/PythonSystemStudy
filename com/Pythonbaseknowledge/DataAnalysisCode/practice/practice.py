# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 0016 10:38
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : practice.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import datetime
import matplotlib.pyplot as plt
from pyecharts.charts import Bar, Line
import pandas_datareader as pdr

# start = datetime(2018, 1, 1)
# alibaba = pdr.get_data_yahoo('BABA', start=start)
# amazon = pdr.get_data_yahoo('AMZN', start=start)
# print(alibaba.tail())
#
# alibaba.to_csv('BABA.csv')
# amazon.to_csv('AMZN.csv')

# print(alibaba.head())
# print(alibaba.shape)
# print(alibaba.tail())
# print(alibaba.describe())
# print(alibaba.info())


"""股票市场分析实战之历史趋势分析"""
alibaba = pd.read_csv('BABA.csv')
amazon = pd.read_csv('AMZN.csv')
#
alibaba['Adj Close'].plot()
amazon['Adj Close'].plot()
alibaba['Volume'].plot(legend=True)

alibaba['High-Low']=alibaba['High']-alibaba['Low']
# alibaba['High-Low'].plot()
# plt.show()
print(alibaba.head())

alibaba['daly return']=alibaba['Adj Close'].pct_change()
# alibaba['daly return'].plot(figsize=(10,4),linestyle='--',marker='o')
# plt.show()
alibaba['daly return'].plot(kind='hist')
plt.show()

ali = alibaba['Volume']
lst = list(ali)
# print(list(ali))
line = Line()
bar = Bar()

start_date = '2010'
end = datetime.datetime.now()
print(end)
date = datetime.datetime.strptime(start_date, '%Y')

start = (date + datetime.timedelta(days=365)).strftime("%Y")
date_list_new = pd.date_range(start, end).strftime("%Y").to_list()
list2 = list(set(date_list_new))
print(list2)
line.add_xaxis(date_list_new)
line.add_yaxis("Volume", lst[0:11])
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render("mycharts.html")


# top_tech = pd.read_csv('top5.csv')
# print(top_tech.head())
# top_tech[['AAPL', 'MSFT', 'FB']].plot()
# plt.show()
# top_tech_dr = top_tech.pct_change()
# print(top_tech_dr.head())


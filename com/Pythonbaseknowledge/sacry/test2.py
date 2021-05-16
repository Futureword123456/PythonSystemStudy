# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 0024 21:25
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : test2.py
# @Software: PyCharm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# excel_file_path = 'paper_publish.xls'
# new_df = pd.read_excel(excel_file_path)

excel_file_path = 'lianjia.csv'
new_df = pd.read_csv(excel_file_path)
print(new_df.head(2))
# 检查缺失值的情况
# print(new_df.info())
# 得出详细信息
# print(new_df.describe())

# 得到每一平方米的价格
new_df['PerPrice'] = new_df['Price'] / new_df['Size']

# 重新摆放列的位置
columns = ['Region', 'District', 'Garden', 'Layout', 'Floor', 'Year', 'Size', 'Elevator', 'Direction', 'Renovation',
           'PerPrice', 'Price']
print("重新摆放列的位置:")
df = pd.DataFrame(new_df, columns=columns)
# 对于区域特征，我们可以分析不同区域房价和数量的对比。
# 对二手房区域分组对比二手房数量和每平米房价
df_house_count = df.groupby('Region')['Price'].count().sort_values(ascending=False).to_frame().reset_index()
print(df_house_count)
df_house_mean = df.groupby('Region')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(list(df_house_mean['Region']))
bar.add_yaxis("区域和二手房数量对比", list(df_house_mean['PerPrice']))
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render("mycharts.html")
# bar.render()


print(df.loc[df['Size'] < 10])
print(df.loc[df['Size'] > 1000])
# 选择移除
df = df[(df['Layout'] != '叠拼别墅') & (df['Size'] < 1000)]
print(df)

df['Renovation'].value_counts()
print(df['Renovation'].value_counts())
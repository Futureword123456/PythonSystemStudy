# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 0012 15:55
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : DataIo.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = pd.read_excel(r'Data.xlsx')
df.to_clipboard()
# 写入excel--->csv文件
df.to_csv('df.csv', index=False)
# 读取csv文件内容
df1 = pd.read_csv('df.csv')
print(df1)

# 转换为csv--->json
print(df1.to_json())
# 转换为json--->csv
print(pd.read_json(df1.to_json()))
# csv-->html
print(df1.to_html('df1.html'))
# csv--->excel
print(df1.to_excel('df1.xlsx'))






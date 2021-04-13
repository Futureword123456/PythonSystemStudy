# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 0007 20:58
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : test3.py
# @Software: PyCharm
# Dataset 1 - Customer Table
import pandas as pd
dfA = pd.DataFrame({'Customer_ID':[1, 2, 3, 4, 5],
                    'Name': ['GitHub', 'Medium', 'Towardsdatascience', 'Google', 'Microsoft'],
                    'City': ['New York', 'Washington', 'Los Angeles', 'San Francisco', 'San Francisco']})
print(dfA)

# Dataset 2 - Orders
dfB = pd.DataFrame({'Order_ID': [1, 2, 3, 4, 5, 6, 7],
                    'Order_date': pd.date_range('20190401', periods=7),
                    'Amount':[440, 238, 346, 637, 129, 304, 892],
                    'Customer_ID':[4, 3, 4, 1, 2, 5, 5]})
print(dfB)



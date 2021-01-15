# -*- coding: utf-8 -*-
# @Time : 2021/1/11 0011 11:37
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample1.py

# 1、的使用{}创建
dict1 = {}  # 空字典
print(type(dict1))

dict2 = {"name": "王芬", "sex": "男",
         "hiredate": "1779-12-03", "grade": 'A',
         'job': '销售', 'salary': 1000,
         'walfare': 100}
print(dict2)
# 2、利用dict函数创建字典
dict3 = dict(name='王芬', sex='男', hiredate='1998-56-23')
print(dict3)
dict4 = dict.fromkeys(['name', 'sex', 'hiredate', 'grade'], 0)
print(dict4)

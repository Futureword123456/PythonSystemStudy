# -*- coding: utf-8 -*-
# @Time : 2021/1/6 0006 10:59
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample2.py
# 成员运算符与身份运算符
sheet = ['张三', '李四', '王五']
if '张三' in sheet:
    print("张三在听课")
else:
    print("张三以旷课")

a = 5
b = a
c = 5.0
print(a is b)
print(a == c)
print(a is c)  # 内存地址比较

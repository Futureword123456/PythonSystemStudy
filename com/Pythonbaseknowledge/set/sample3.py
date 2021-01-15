# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 14:09
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample3.py
# 集合间的关系运算
s1 = {1, 2, 3, 4, 5, 6}
s2 = {6, 5, 4, 3, 2, 1}
# ==是判断两个集合是否相等
print(s1 == s2)
# issubse判断是否是子集
s3 = {4, 5, 6, 7}
s4 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s3.issubset(s4))
# 判断是否是父集
print(s4.issuperset(s3))
s5 = {6}
s6 = {1, 3, 5, 7, 9}
# isdisjoint函数判断两个集合是否存在重复元素
# Ture代表不存在重复元素，False代表存在重复元素
print(s5.isdisjoint(s6))

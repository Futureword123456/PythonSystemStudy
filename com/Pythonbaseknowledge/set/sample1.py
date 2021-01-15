# -*- coding: utf-8 -*-
# @Time : 2021/1/13 0013 10:53
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample1.py
# 集合的创建
collect = {'哲学', '经济学', '法学', '教育学'}
print(collect)
# set()内置函数从其他数据结构转换
collect2 = {"经济学", "哲学", "金融学", '历史学', "文学"}
print(collect2)
# 使用set创建字符串集合
collect3 = set("中华人民共和国")
print(collect3)
# 空集合
# collect4 = {}
collect4 = set()
print(type(collect4))

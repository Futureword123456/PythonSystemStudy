# -*- coding: utf-8 -*-
# @Time : 2021/1/9 0009 17:48
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample4.py
# 列表的反转与排序
persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
persons.reverse()
print(persons)

numbers = [21, 65, 45, 89, 32, 56, 48, 79, 32, 14]
numbers.sort(reverse=True)  # sort()用于排序，reverse=True代表降序排列
print(numbers)  # 输出降序序列

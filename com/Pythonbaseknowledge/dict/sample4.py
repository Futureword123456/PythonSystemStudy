# -*- coding: utf-8 -*-
# @Time : 2021/1/11 0011 12:15
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample4.py
# 字典的grade常用操作
emp1 = {'name': 'jacky', 'grade': 'B'}
emp2 = {'name': 'Lily', 'grade': 'A'}
# setdefault
#  lt设置默认值，如果某个key已存在则忽略，不存在则设置
emp1.setdefault('grade', 'C')
emp2.setdefault('grade', 'C')
# 一种设置默认值的方法
# if 'grade' not in emp2:
#     emp2['grade'] = 'C'
print(emp2)
print(emp1)

# 获取字典的视图
# (1)keys代表获取所有的键
ks = emp1.keys()
print(ks)
print(type(ks))
# (2)values代表获取所有的值
vs = emp1.values()
print(vs)
print(type(vs))
# (3items代表获取所有的键值对
its = emp1.items()
print(its)  # 返回的都是一个元组
print(type(its))
emp1['haredate'] = '1980-12-03'
print(ks)
print(vs)
print(its)
# 3、利用字典格式化字符串
# 老版本的字符串格式化
emp_str = "姓名:%(name)s,评级:%(grade)s,入职时间:%(haredate)s" % emp1
print(emp_str)
# 新版本的格式化方法
emp_str1 = "姓名:{name},评级:{grade},入职时间:{haredate}".format_map(emp1)
print(emp_str1)


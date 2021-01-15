# -*- coding: utf-8 -*-
# @Time : 2021/1/11 0011 11:59
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample3.py
# 字典的更新

employee = {"name": "王芬", "sex": "男",
            "hiredate": "1779-12-03", "grade": 'A',
            'job': '销售', 'salary': 1000,
            'warefare': 100}
print(employee)
# 直接更新（对单个进行更新）
employee['grade'] = 'B'
print(employee)
employee.update(salary=1200, warefare=150)  # 可以一次性对读个key,value进行更新
print(employee)
# 字典的增加操作与 更新操作一样，有则更新，无则增加
employee['dept'] = '研发部'
print(employee)
# 有更新
employee['dept'] = '市场部'
print(employee)
employee.update(weight=80, dept='财务部')
print(employee)
# 删除操作(与删除操作函数)
# 1、pop(参数是key不是value)函数最常用
employee.pop('weight')
print(employee)
# 2、popitem删除最后一个kv
kv = employee.popitem()
# kv = employee.popitem()
print(kv)
print(employee)

# 3、clear清空字典
employee.clear()
print(employee)

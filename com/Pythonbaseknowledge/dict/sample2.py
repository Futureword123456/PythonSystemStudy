# -*- coding: utf-8 -*-
# @Time : 2021/1/11 0011 11:47
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample2.py
# 字典的取值操作

employee = {"name": "王芬", "sex": "男",
            "hiredate": "1779-12-03", "grade": 'A',
            'job': '销售', 'salary': 1000,
            'walfare': 100}
# 字典的取值(用key获取值（value）)
name = employee['name']
print(name)
salary = employee['salary']
print(salary)

print(employee.get('job'))
print(employee.get('dept', '其他部门'))

# in成员运算符
print('name' not in employee)
print('dept' not in employee)

# 遍历字典
for key in employee:
    v = employee[key]
    print(v)

# for key, value in employee.items():  # items包含键值对
#     print(key, value)

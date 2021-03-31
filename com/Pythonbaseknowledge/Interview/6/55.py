# -*- coding: utf-8 -*-
# @Time : 2021/3/10 0010
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 55.py
"""合并字典"""
employee = {"name": "王芬", "sex": "男",
            "hiredate": "1779-12-03", "grade": 'A',
            'job': '销售', 'salary': 1000,
            'warefare': 100}
key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
"""使用update()函数合并"""
employee.update(key_value)
print(employee)
print("======================")
"""使用**添加函数"""
rest = {**employee,**key_value}
print(rest)
if __name__ == "__main__":
    pass
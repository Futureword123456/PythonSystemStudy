# -*- coding: utf-8 -*-
# @Time : 2021/1/11 0011 18:01
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample6.py
# 处理员工数据
source = "7782,CLARK,MANAGER,SALES,5000$7934,MILLER,SALESMAN,SALES,3000$7369,SMITH,ANALYST,RESEARCH,2000"
employee_list = source.split("$")
print(employee_list)
all_emp = {}  # 用于保存所有解析后的员工信息，key是元素编号，value是包含完整的员工信息的字典
for i in range(0, len(employee_list)):
    # print(i)
    e = employee_list[i].split(",")
    print(e)
    # 创建员工的字典
    employee = {"no": e[0], 'name': e[1], 'job': e[2], 'department': e[3], 'salary': e[4]}
    print(employee)
    all_emp[employee['no']] = employee
print(all_emp)

empno = input("请输入员工编号:")
emp = all_emp.get(empno)
if empno in all_emp:
    print("工号:{no},姓名:{name},岗位:{job},部门:{department},工资:{salary}".format_map(emp))
else:
    print("员工信息不存在")
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 0011 18:28
# @Author : 杨华钟
# @Email : 2635681517@qq.com
# @File : sample7.py
# 元的数据的处理
source = "7782,CLARK,MANAGER,SALES,5000$7934,MILLER,SALESMAN,SALES,3000$7369,SMITH,ANALYST,RESEARCH,2000"
emplayee_list = source.split("$")
print(emplayee_list)
# 拿到所有员工的数据
all_emp = {}
for i in range(0, len(emplayee_list)):
    # print(i)
    e = emplayee_list[i].split(",")
    print(e)
    # 创建员工字典
    employee = {"no": e[0], 'name': e[1], 'job': e[2], 'department': e[3], 'salary': e[4]}
    # print(employee)
    all_emp[employee['no']] = employee
print(all_emp)
while True:
    empno = input("请输入员工编号(输入0结束程序):")
    emp = all_emp.get(empno)  # 用输入的员工编号
    if empno not in all_emp:
        print("该员工不存在!@!,请重新输入！")
    else:
        print("工号:{no},姓名:{name},岗位:{job},部门:{department},工资:{salary}".format_map(emp))
    if empno == "0":
        print("程序结束")
        break
